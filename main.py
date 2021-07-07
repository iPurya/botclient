# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import telebot
import threading

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(991, 509)
        self.BotClient = QtWidgets.QWidget(self)
        self.BotClient.setObjectName("BotClient")
        self.BotClientLayout = QtWidgets.QHBoxLayout(self.BotClient)
        self.BotClientLayout.setContentsMargins(0, 0, 0, 0)
        self.BotClientLayout.setSpacing(0)
        self.BotClientLayout.setObjectName("BotClientLayout")
        self.MainLayout = QtWidgets.QHBoxLayout()
        self.MainLayout.setContentsMargins(5, 5, 5, 5)
        self.MainLayout.setSpacing(5)
        self.MainLayout.setObjectName("MainLayout")
        self.dialogFrame = QtWidgets.QFrame(self.BotClient)
        self.dialogFrame.setObjectName("dialogFrame")
        self.dialogLayout = QtWidgets.QVBoxLayout(self.dialogFrame)
        self.dialogLayout.setContentsMargins(0, 0, 0, 0)
        self.dialogLayout.setSpacing(10)
        self.dialogLayout.setObjectName("dialogLayout")
        self.groupBox = QtWidgets.QGroupBox(self.dialogFrame)
        self.groupBox.setObjectName("groupBox")
        self.loginGroupLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.loginGroupLayout.setContentsMargins(5, 0, 0, 0)
        self.loginGroupLayout.setSpacing(5)
        self.loginGroupLayout.setObjectName("loginGroupLayout")
        self.loginLabel = QtWidgets.QLabel(self.groupBox)
        self.loginLabel.setObjectName("loginLabel")
        self.loginGroupLayout.addWidget(self.loginLabel)
        self.TokenInput = QtWidgets.QLineEdit(self.groupBox)
        self.TokenInput.setObjectName("TokenInput")
        self.loginGroupLayout.addWidget(self.TokenInput)
        self.loginButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setObjectName("loginButton")
        self.loginGroupLayout.addWidget(self.loginButton)
        self.dialogLayout.addWidget(self.groupBox)
        self.chatsList = QtWidgets.QListWidget(self.dialogFrame)
        self.chatsList.setObjectName("chatsList")
        self.dialogLayout.addWidget(self.chatsList)
        self.dialogLayout.setStretch(0, 1)
        self.dialogLayout.setStretch(1, 9)
        self.MainLayout.addWidget(self.dialogFrame)
        self.chatFrame = QtWidgets.QFrame(self.BotClient)
        self.chatFrame.setObjectName("chatFrame")
        self.chatLayout = QtWidgets.QVBoxLayout(self.chatFrame)
        self.chatLayout.setContentsMargins(0, 0, 0, 0)
        self.chatLayout.setSpacing(5)
        self.chatLayout.setObjectName("chatLayout")
        self.userInfoFrame = QtWidgets.QFrame(self.chatFrame)
        self.userInfoFrame.setStyleSheet("background-color: rgb(255,255,255)")
        self.userInfoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.userInfoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userInfoFrame.setObjectName("userInfoFrame")
        self.userInfoGridLayout = QtWidgets.QGridLayout(self.userInfoFrame)
        self.userInfoGridLayout.setContentsMargins(10, 2, 2, 2)
        self.userInfoGridLayout.setHorizontalSpacing(10)
        self.userInfoGridLayout.setVerticalSpacing(0)
        self.userInfoGridLayout.setObjectName("userInfoGridLayout")
        self.userPic = QtWidgets.QLabel(self.userInfoFrame)
        self.userPic.setMinimumSize(QtCore.QSize(50, 50))
        self.userPic.setMaximumSize(QtCore.QSize(50, 50))
        self.userPic.setText("")
        self.userPic.setPixmap(QtGui.QPixmap("default_pic.jpg"))
        self.userPic.setScaledContents(True)
        self.userPic.setObjectName("userPic")
        self.userInfoGridLayout.addWidget(self.userPic, 0, 0, 2, 1)
        self.infoLabel = QtWidgets.QLabel(self.userInfoFrame)
        self.infoLabel.setText("")
        self.infoLabel.setObjectName("infoLabel")
        self.userInfoGridLayout.addWidget(self.infoLabel, 0, 2, 2, 1)
        self.userInfoLabel = QtWidgets.QLabel(self.userInfoFrame)
        self.userInfoLabel.setObjectName("userInfoLabel")
        self.userInfoGridLayout.addWidget(self.userInfoLabel, 0, 1, 2, 1)
        self.userInfoGridLayout.setColumnStretch(0, 1)
        self.userInfoGridLayout.setColumnStretch(1, 2)
        self.userInfoGridLayout.setColumnStretch(2, 6)
        self.chatLayout.addWidget(self.userInfoFrame)
        self.chatHistoryFrame = QtWidgets.QFrame(self.chatFrame)
        self.chatHistoryFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.chatHistoryFrame.setObjectName("chatHistoryFrame")
        self.chatHistoryLayout = QtWidgets.QVBoxLayout(self.chatHistoryFrame)
        self.chatHistoryLayout.setContentsMargins(0, 0, 0, 0)
        self.chatHistoryLayout.setSpacing(0)
        self.chatHistoryLayout.setObjectName("chatHistoryLayout")
        self.textEdit = QtWidgets.QTextEdit(self.chatHistoryFrame)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.chatHistoryLayout.addWidget(self.textEdit)
        self.chatLayout.addWidget(self.chatHistoryFrame)
        self.sendFrame = QtWidgets.QFrame(self.chatFrame)
        self.sendFrame.setObjectName("sendFrame")
        self.sendLayout = QtWidgets.QHBoxLayout(self.sendFrame)
        self.sendLayout.setContentsMargins(0, 0, 0, 0)
        self.sendLayout.setSpacing(5)
        self.sendLayout.setObjectName("sendLayout")
        self.sendText = QtWidgets.QTextEdit(self.sendFrame)
        self.sendText.setObjectName("sendText")
        self.sendLayout.addWidget(self.sendText)
        self.sendButton = QtWidgets.QPushButton(self.sendFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.sendButton.setSizePolicy(sizePolicy)
        self.sendButton.setObjectName("sendButton")
        self.sendLayout.addWidget(self.sendButton)
        self.chatLayout.addWidget(self.sendFrame)
        self.chatLayout.setStretch(0, 1)
        self.chatLayout.setStretch(1, 8)
        self.chatLayout.setStretch(2, 1)
        self.MainLayout.addWidget(self.chatFrame)
        self.MainLayout.setStretch(0, 1)
        self.MainLayout.setStretch(1, 2)
        self.BotClientLayout.addLayout(self.MainLayout)
        self.setCentralWidget(self.BotClient)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginLabel.setText(_translate("MainWindow", "Token:"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.sendButton.setText(_translate("MainWindow", "Send"))


class MyWin(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.loginButton.clicked.connect(self.login_handle)
        self.telebot = None
        self.infoLabel.setText("Please login first!")
        self.bot_id = None
        self.bot_name = None
        self.bot_username = None
    def login_handle(self,event):
        if self.loginButton.text() == "Login":
            inp = self.TokenInput.text()
            try:
                self.telebot = telebot.TeleBot(inp)
                me = self.telebot.get_me()
                self.bot_id, self.bot_name, self.bot_username = me.id, me.first_name, me.username
                self.userInfoLabel.setText(f"{me.first_name}\n@{me.username}\n{me.id}")
                self.infoLabel.setText("")
                self.textEdit.setText(f"Logged in as {me.first_name}")
                self.loginButton.setText("Logout")
                self.TokenInput.setEnabled(False)
            except telebot.apihelper.ApiTelegramException:
                self.textEdit.setText(f"Token invalid!")
        else: #logout
            self.infoLabel.setText("Please login first!")
            self.textEdit.setText(f"Logged out")
            self.loginButton.setText("Login")
            self.TokenInput.setEnabled(True)
            self.telebot.stop_bot()
    def set_profile_pic()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MyWin()
    ui.show()
    sys.exit(app.exec_())
