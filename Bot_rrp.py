# Form implementation generated from reading ui file 'Bot_rrp.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1170, 646)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1171, 651))
        self.stackedWidget.setStyleSheet("background-image: url(RightSizePictures/art.jpeg);\n"
"border-radius: 59;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.prestart_widget = QtWidgets.QWidget()
        self.prestart_widget.setObjectName("prestart_widget")
        self.vk_button = QtWidgets.QPushButton(self.prestart_widget)
        self.vk_button.setGeometry(QtCore.QRect(20, 360, 191, 191))
        self.vk_button.setStyleSheet("QPushButton {\n"
" background: url(RightSizePictures/image 1.png)\n"
"\n"
"}\n"
"QPushButton:hover {    \n"
"background: url(RightSizePictures/vk_hover.png)\n"
"}")
        self.vk_button.setText("")
        self.vk_button.setObjectName("vk_button")
        self.vk_auth = QtWidgets.QFrame(self.prestart_widget)
        self.vk_auth.setGeometry(QtCore.QRect(260, 140, 865, 411))
        self.vk_auth.setStyleSheet("background: rgb(47, 112, 157)")
        self.vk_auth.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.vk_auth.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.vk_auth.setObjectName("vk_auth")
        self.Login = QtWidgets.QLineEdit(self.vk_auth)
        self.Login.setGeometry(QtCore.QRect(50, 120, 771, 41))
        self.Login.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(246, 97, 81);\n"
"border-radius: 20px;\n"
"background-color: #FFF;\\n\n"
"}")
        self.Login.setObjectName("Login")
        self.Password = QtWidgets.QLineEdit(self.vk_auth)
        self.Password.setGeometry(QtCore.QRect(50, 210, 771, 41))
        self.Password.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(246, 97, 81);\n"
"border-radius: 20px;\n"
"background-color: #FFF;\\n\n"
"}")
        self.Password.setObjectName("Password")
        self.auth_btn = QtWidgets.QPushButton(self.vk_auth)
        self.auth_btn.setGeometry(QtCore.QRect(230, 320, 401, 51))
        self.auth_btn.setStyleSheet("QPushButton{\n"
"background-image: url(RightSizePictures/Enter_btn.png);\n"
"background-repeat: no-repeat;\n"
"}\n"
"QPushButton:hover {\n"
"background:url(RightSizePictures/Enter_btn_hover.png);\n"
"background-repeat: no repeat;\n"
"}")
        self.auth_btn.setText("")
        self.auth_btn.setObjectName("auth_btn")
        self.label = QtWidgets.QLabel(self.vk_auth)
        self.label.setGeometry(QtCore.QRect(60, 40, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        self.tg_button = QtWidgets.QPushButton(self.prestart_widget)
        self.tg_button.setGeometry(QtCore.QRect(20, 150, 191, 191))
        self.tg_button.setStyleSheet("QPushButton {\n"
" background: url(RightSizePictures/tg.png)\n"
"\n"
"}\n"
"QPushButton:hover {    \n"
"background: url(RightSizePictures/tg_hover.png)\n"
"}")
        self.tg_button.setText("")
        self.tg_button.setObjectName("tg_button")
        self.ExitBtn_2 = QtWidgets.QPushButton(self.prestart_widget)
        self.ExitBtn_2.setGeometry(QtCore.QRect(1050, 0, 81, 71))
        self.ExitBtn_2.setStyleSheet("\n"
"QPushButton{\n"
"background: url(RightSizePictures/exit_button.png);\n"
"background-repeat: no repeat;\n"
"}\n"
"QPushButton:hover {\n"
"background: url(RightSizePictures/exit_button_hover.png);\n"
"background-repeat: no repeat;\n"
"}")
        self.ExitBtn_2.setText("")
        self.ExitBtn_2.setObjectName("ExitBtn_2")
        self.HideBtn_2 = QtWidgets.QPushButton(self.prestart_widget)
        self.HideBtn_2.setGeometry(QtCore.QRect(980, 10, 71, 61))
        self.HideBtn_2.setStyleSheet("QPushButton{\n"
"background: url(RightSizePictures/hide_button.png);\n"
"background-repeat: no repeat;\n"
"}\n"
"QPushButton:hover {\n"
"background: url(RightSizePictures/hide_button_hover.png);\n"
"background-repeat: no repeat;\n"
"}")
        self.HideBtn_2.setText("")
        self.HideBtn_2.setObjectName("HideBtn_2")
        self.stackedWidget.addWidget(self.prestart_widget)
        self.sending_workspace = QtWidgets.QWidget()
        self.sending_workspace.setObjectName("sending_workspace")
        self.sending_messages = QtWidgets.QFrame(self.sending_workspace)
        self.sending_messages.setGeometry(QtCore.QRect(260, 140, 865, 411))
        self.sending_messages.setStyleSheet("background: rgb(47, 112, 157)")
        self.sending_messages.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.sending_messages.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.sending_messages.setObjectName("sending_messages")
        self.PrintBrowser = QtWidgets.QTextBrowser(self.sending_messages)
        self.PrintBrowser.setGeometry(QtCore.QRect(240, 30, 591, 281))
        self.PrintBrowser.setStyleSheet("")
        self.PrintBrowser.setObjectName("PrintBrowser")
        self.Part_name = QtWidgets.QLabel(self.sending_messages)
        self.Part_name.setGeometry(QtCore.QRect(50, 20, 174, 33))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.Part_name.setFont(font)
        self.Part_name.setStyleSheet("color: white;")
        self.Part_name.setObjectName("Part_name")
        self.chat_name_input = QtWidgets.QLineEdit(self.sending_messages)
        self.chat_name_input.setGeometry(QtCore.QRect(20, 130, 191, 51))
        self.chat_name_input.setStyleSheet("background: white;\n"
"border-radius: 15;")
        self.chat_name_input.setObjectName("chat_name_input")
        self.start_send_button = QtWidgets.QPushButton(self.sending_messages)
        self.start_send_button.setGeometry(QtCore.QRect(20, 320, 191, 71))
        self.start_send_button.setStyleSheet("\n"
"QPushButton{\n"
"border-image: url(RightSizePictures/start_send_button.png);\n"
"background-repeat: no repeat;\n"
"}\n"
"QPushButton:hover {\n"
"border-image: url(RightSizePictures/start_send_button_hover.png);\n"
"background-repeat: no repeat;\n"
"}\n"
"")
        self.start_send_button.setText("")
        self.start_send_button.setObjectName("start_send_button")
        self.progressBar = QtWidgets.QProgressBar(self.sending_messages)
        self.progressBar.setGeometry(QtCore.QRect(240, 330, 591, 61))
        self.progressBar.setStyleSheet("background: rgb(255, 255, 255)")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.chat_name_label = QtWidgets.QLabel(self.sending_messages)
        self.chat_name_label.setGeometry(QtCore.QRect(20, 210, 191, 71))
        self.chat_name_label.setStyleSheet("border: 4px solid black;\n"
"border-radius: 10;\n"
"\n"
"background-color: rgb(119, 118, 123)")
        self.chat_name_label.setText("")
        self.chat_name_label.setText("")
        self.chat_name_label.setObjectName("chat_name_label")
        self.Input_message = QtWidgets.QTextEdit(self.sending_messages)
        self.Input_message.setGeometry(QtCore.QRect(240, 40, 581, 271))
        self.Input_message.setStyleSheet("background: white; border-radius: 0")
        self.Input_message.setObjectName("Input_message")
        self.vk_button_2 = QtWidgets.QPushButton(self.sending_workspace)
        self.vk_button_2.setGeometry(QtCore.QRect(20, 360, 191, 191))
        self.vk_button_2.setStyleSheet("QPushButton {\n"
" background: url(RightSizePictures/image 1.png)\n"
"\n"
"}\n"
"QPushButton:hover {    \n"
"background: url(RightSizePictures/vk_hover.png)\n"
"}")
        self.vk_button_2.setText("")
        self.vk_button_2.setObjectName("vk_button_2")
        self.tg_button_2 = QtWidgets.QPushButton(self.sending_workspace)
        self.tg_button_2.setGeometry(QtCore.QRect(20, 150, 191, 191))
        self.tg_button_2.setStyleSheet("QPushButton {\n"
" background: url(RightSizePictures/tg.png)\n"
"\n"
"}\n"
"QPushButton:hover {    \n"
"background: url(RightSizePictures/tg_hover.png)\n"
"}")
        self.tg_button_2.setText("")
        self.tg_button_2.setObjectName("tg_button_2")
        self.ExitBtn = QtWidgets.QPushButton(self.sending_workspace)
        self.ExitBtn.setGeometry(QtCore.QRect(1050, 0, 81, 71))
        self.ExitBtn.setStyleSheet("\n"
"QPushButton{\n"
"background: url(RightSizePictures/exit_button.png);\n"
"background-repeat: no repeat;\n"
"}\n"
"QPushButton:hover {\n"
"background: url(RightSizePictures/exit_button_hover.png);\n"
"background-repeat: no repeat;\n"
"}")
        self.ExitBtn.setText("")
        self.ExitBtn.setObjectName("ExitBtn")
        self.HideBtn = QtWidgets.QPushButton(self.sending_workspace)
        self.HideBtn.setGeometry(QtCore.QRect(980, 10, 71, 61))
        self.HideBtn.setStyleSheet("QPushButton{\n"
"background: url(RightSizePictures/hide_button.png);\n"
"background-repeat: no repeat;\n"
"}\n"
"QPushButton:hover {\n"
"background: url(RightSizePictures/hide_button_hover.png);\n"
"background-repeat: no repeat;\n"
"}")
        self.HideBtn.setText("")
        self.HideBtn.setObjectName("HideBtn")
        self.stackedWidget.addWidget(self.sending_workspace)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Регистрация"))
        self.Part_name.setText(_translate("MainWindow", "Рассылка"))