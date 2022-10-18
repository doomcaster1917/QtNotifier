import datetime
import threading
from PyQt6.QtGui import QPainter
import vk_api.exceptions
from PyQt6 import uic, QtCore, QtGui, QtWidgets
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QUrl, QCoreApplication, QEvent
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMessageBox
import time, sys, os
from PyQt6.QtWidgets import *
from Bot_rrp import Ui_MainWindow
import re
from vk_api import VkApi
import vk_api
import random
import requests
from models import session, User

nikita_id = 284359812
natasha_id = 302427147

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.hidden = False

        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.vk_button.clicked.connect(self.auth_user)
        self.ui.vk_button_2.clicked.connect(self.auth_user)

        self.ui.start_send_button.clicked.connect(self.start_send)
        self.u = 'f'

        self.ui.ExitBtn.clicked.connect(lambda: self.close())
        self.ui.ExitBtn_2.clicked.connect(lambda: self.close())
        self.ui.HideBtn.clicked.connect(lambda: self.showMinimized())
        self.ui.HideBtn_2.clicked.connect(lambda: self.showMinimized())

        self.ui.chat_name_input.textChanged.connect(self.show_chat_name)


        self.ui.auth_btn.clicked.connect(self.openMenu)
        self.sound_effects('sounds/korotkiy-spokoynyiy-zvuk-shitya-na-shveynoy-mashinke.wav')


        self.ui.vk_auth.hide()
        self.ui.sending_workspace.hide()

        self.opacity(self.ui.vk_auth)
        self.opacity(self.ui.sending_workspace)
        self.ui.Login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Введите логин", None))
        self.ui.Password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Введите пароль", None))
        self.ui.chat_name_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Введите id диалога", None))
        self.ui.Input_message.setPlaceholderText(QCoreApplication.translate("MainWindow", u'Введите текст сообщения', None))
        self.ui.sending_workspace.setGeometry(QtCore.QRect(0, 0, 1171, 651))

        self.ui.progressBar.setMaximum(0)

        self.text = ''

    def opacity(self, part):
        op = QGraphicsOpacityEffect()
        op.setOpacity(0.8)  # 0 to 1 will cause the fade effect to kick in
        part.setGraphicsEffect(op)
        part.setAutoFillBackground(True)

    def auth_user(self):

        self.button_clicked()

        bd_query = session.query(User).first()
        if bd_query:
            login = bd_query.login
            password = bd_query.password
        else:
            login, password = None, None



        if login and password:
            ok = self.vk_auth(login=login, password=password)
            if ok:
                print(ok)
                self.ui.prestart_widget.hide()
                self.ui.sending_workspace.show()
        else:
            self.ui.prestart_widget.show()



    def openMenu(self):

        if self.vk_auth():
            self.ui.prestart_widget.hide()
            self.ui.sending_workspace.show()




    def vk_auth(self, login=None, password=None):
        try:
            self.sound_effects('sounds/bryanchanie-kryishkoy.wav')

            if login and password:
                self.vk_session = VK_sender(login=login, password=password)
                print('Auth ok')

            else:

                login = re.sub('Логин:', '', self.ui.Login.text()).strip()
                password = re.sub('Пароль:', '', self.ui.Password.text()).strip()
                print(login)
                self.vk_session = VK_sender(login=login, password=password)
                print('Auth ok')
                new_user = User(login=login, password=password)
                session.add(new_user)
                session.commit()
                print(f'Зареган юзер, login:{login} password:{password}')
            return True


        except Exception as err:
            msg = QMessageBox()
            print(f'err is {err}')
            if isinstance(err, vk_api.exceptions.BadPassword|vk_api.exceptions.LoginRequired):
                session.query(User).filter_by(login=login).delete()
                msg.setWindowTitle(f'Неверные логин или пароль')
                msg.setStandardButtons(QMessageBox.StandardButton.Yes)
                msg.exec()



            elif isinstance(err, vk_api.Captcha):

                self.captcha_notification(err)

            elif isinstance(err, vk_api.TwoFactorError):
                self.two_factor()



            return False



    def two_factor(self):
        msg = QMessageBox()
        code = QtWidgets.QLineEdit(msg)

        msg.setWindowTitle(f'Двухфакторная идентификация')
        msg.setText(f'   Введите код из смс \n   или последние 4 цифры  \n   звонившего вам номера')
        msg.setStyleSheet("QLabel{min-width: 170px; min-height: 210px}")

        code.setGeometry(QtCore.QRect(60, 170, 150, 40))
        msg.setStandardButtons(QMessageBox.StandardButton.Yes)

        msg.exec()


        if msg.clickedButton():
            key = code.text()
            remember_device = True
            print(key)
            return key, remember_device

    def captcha_notification(self, captcha: vk_api.Captcha) -> str|int:

        captcha.get_url()
        image_content = requests.get(captcha.url).content
        msg = QMessageBox()
        pixmap = QPixmap()
        pixmap.loadFromData(image_content)
        pixmap = pixmap.scaledToWidth(340)
        msg.setIconPixmap(pixmap)
        key_input = QtWidgets.QLineEdit(msg)
        key_input.setGeometry(QtCore.QRect(35, 147, 180, 30))
        msg.setStandardButtons(QMessageBox.StandardButton.Yes)
        msg.setDefaultButton(QMessageBox.StandardButton.Yes)
        msg.exec()
        if msg.clickedButton():
            key = key_input.text()

            return captcha.try_again(key)

    def show_chat_name(self, chat_id):

        if self.vk_session.define_chat_users(chat_id):
            users, name = self.vk_session.define_chat_users(chat_id)
            print(name)
            self.ui.chat_name_label.setText(name)
        else:
            if chat_id:
                self.ui.chat_name_label.setText('Чата не существует')
            else:
                self.ui.chat_name_label.setText('Введите номер чата')



    def sound_effects(self, filename: str):
        self.sound_effect = QSoundEffect()
        self.sound_effect.setSource(QUrl.fromLocalFile(filename))
        self.sound_effect.play()


    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()



    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()


    def button_clicked(self):

        if self.ui.prestart_widget.isHidden():
            if self.hidden == True:
                self.ui.sending_messages.hide()

                self.hidden = False
                self.sound_effects('sounds/korotkiy-spokoynyiy-zvuk-shitya-na-shveynoy-mashinke.wav')
            else:
                self.ui.sending_messages.show()
                self.hidden = True
                self.sound_effects('sounds/bryanchanie-kryishkoy.wav')
        else:
            if self.hidden == True:
                self.ui.vk_auth.hide()

                self.hidden = False
                self.sound_effects('sounds/korotkiy-spokoynyiy-zvuk-shitya-na-shveynoy-mashinke.wav')
            else:
                self.ui.vk_auth.show()
                self.hidden = True
                self.sound_effects('sounds/bryanchanie-kryishkoy.wav')


    def start_send(self, n=None):

        self.sound_effects('sounds/bryanchanie-kryishkoy.wav')

        chat_id = self.ui.chat_name_input.text()
        users, _ = self.vk_session.define_chat_users(chat_id)
        max_num = len(users)
        self.ui.Input_message.hide()
        msg_text = self.ui.Input_message.toPlainText()

        self.ui.progressBar.show()
        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMaximum(max_num)

        text = ''
        for num, user_id in enumerate(users):
            time.sleep(2)
            self.ui.progressBar.setValue(num + 1)
            user_name = self.vk_session.vk.users.get(user_ids=user_id)
            uniq_id = datetime.datetime.now().microsecond
            print(uniq_id)
            self.vk_session.vk.messages.send(message=str(msg_text), peer_id=user_id, random_id=uniq_id)
            text += f"Сообщение выслано пользователю {user_name[0]['first_name']}{user_name[0]['last_name']} \n"
            self.ui.PrintBrowser.setText(text)

class MyEvent(QEvent):
    def myEvent(self, event):
        super(MyEvent)
        QEvent.registerEventType()

class VK_sender(VkApi):

    def __init__(self, login, password):

        super(VK_sender, self).__init__(login=login, password=password, app_id=2685278,
                                        client_secret="hHbJug59sKJie78wjrH8",
                                        captcha_handler=GUI().captcha_notification, auth_handler=GUI().two_factor)

        self.auth()
        self.vk = self.get_api()

        bd_query = session.query(User).first()
        if not bd_query:
            newUser = User(login=login, password=password)
            session.add(newUser)
            session.commit()





    def check_api(self):
        self.vk = self.get_api()
        return True




    #------------Определяем id участников конфы вк ------------------------
    def define_chat_users(self, chat_id):
        try:
            chat_info = self.vk.messages.getChat(chat_id=chat_id, random_id=random.randint(0, 10000))
            users = chat_info["users"]
            name = chat_info["title"]


            return users, name
        except:
            return False

    #-----------Отправляем сообщения участникам чата-----------------------
    def sending_messages(self):
        text = 'Это тестовое сообщение от разрабатываемого бота, прошу отнестись с пониманием'

        users = self.define_chat_users()
        for target_id in users:
             try:
                  while 1<5:
                    print(self.vk.messages.send(user_id=natasha_id, message=text, random_id=random.randint(0, 10000)))

                    #time.sleep(4)
             except vk_api.Captcha as err:
                  self.captcha_handler(err)


             except vk_api.ApiError as err:

                 if err.code == 902: ...

                 print(err.error['error_code'])
             pass







app = QApplication(sys.argv)
window = GUI()
window.show()
sys.exit(app.exec())