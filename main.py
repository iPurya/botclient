import threading
import collections
import functools
import inspect
import os
import re
import sys
import time
import tkinter
import tkinter.constants
import tkinter.scrolledtext
import tkinter.ttk

import telebot
# Some configuration for the app
TITLE = 'Bot Cli'
SIZE = '640x280'
REPLY = re.compile(r'\.r\s*(\d+)\s*(.+)', re.IGNORECASE)
DELETE = re.compile(r'\.d\s*(\d+)', re.IGNORECASE)
EDIT = re.compile(r'\.s(.+?[^\\])/(.*)', re.IGNORECASE)


def allow_copy(widget):
    widget.bind('<Control-c>', lambda e: None)
    widget.bind('<Key>', lambda e: "break")


class App(tkinter.Tk):
    def __init__(self, bot, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = bot
        self.me = None

        self.title(TITLE)
        self.geometry(SIZE)

        # Signing in row; the entry supports phone and bot token
        self.sign_in_label = tkinter.Label(self, text='Enter Token:')
        self.sign_in_label.grid(row=0, column=0)
        self.sign_in_entry = tkinter.Entry(self)
        self.sign_in_entry.grid(row=0, column=1, sticky=tkinter.EW)
        self.sign_in_entry.bind('<Return>', self.sign_in)
        self.sign_in_button = tkinter.Button(self, text='Sign in',
                                             command=self.sign_in)
        self.sign_in_button.grid(row=0, column=2)
        self.code = None

        tkinter.Label(self, text='Target chat:').grid(row=1, column=0)
        self.chat = tkinter.Entry(self)
        self.chat.grid(row=1, column=1, columnspan=2, sticky=tkinter.EW)
        self.columnconfigure(1, weight=1)
        self.chat.focus()
        self.chat_id = None

        self.log = tkinter.scrolledtext.ScrolledText(self)
        allow_copy(self.log)
        self.log.grid(row=2, column=0, columnspan=3, sticky=tkinter.NSEW)
        self.rowconfigure(2, weight=1)
        
        self.message_ids = []

        self.sent_text = collections.deque(maxlen=10)

        tkinter.Label(self, text='Message:').grid(row=3, column=0)
        self.message = tkinter.Entry(self)
        self.message.grid(row=3, column=1, sticky=tkinter.EW)
        self.message.bind('<Return>', self.send_message)
        tkinter.Button(self, text='Send',
                       command=self.send_message).grid(row=3, column=2)

    def stop_bot(self):
        #Stop Bot if running..
        try:
            self.bot.stop_bot()
        except: pass
    def start_bot(self):
        try:
            self.bot.polling(True)
        except: pass
    def sign_in(self, event=None):
        
        
        self.sign_in_label.configure(text='Loading...')
        self.sign_in_entry.configure(state=tkinter.DISABLED)
        try:
            self.bot = telebot.TeleBot(self.sign_in_entry.get())
            self.me = self.bot.get_me()
            self.bot.add_message_handler({'function': self.on_message,'filters': {}})
            self.sign_in_label.configure(text=self.me.first_name)
            self.sign_in_button.configure(text="Log out",command=self.log_out)
            threading.Thread(target=self.start_bot,daemon=True).start()
        except Exception as e:
            self.sign_in_label.configure(text='Wrong Token!')
            self.sign_in_entry.configure(state=tkinter.NORMAL)
            self.sign_in_entry.delete(0, tkinter.END)
            self.sign_in_entry.focus()
    
    def log_out(self,event=None):
        self.stop_bot()
        self.sign_in_label.configure(text='Enter Token:')
        self.sign_in_button.configure(text="Sign in",command=self.sign_in)
        self.sign_in_entry.configure(state=tkinter.NORMAL)
        self.sign_in_entry.focus()
    def on_message(self,msg):
        print(msg.text)
    


if __name__ == "__main__":
    app = App()
    try:
        while True:
            app.update()
            time.sleep(0.05)
    except KeyboardInterrupt:
        pass
    except tkinter.TclError as e:
        if 'application has been destroyed' not in e.args[0]:
            raise