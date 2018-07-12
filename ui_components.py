import sys
from PySide2.QtWidgets import QMainWindow,QApplication,QHBoxLayout,QStackedWidget,QFormLayout
from PySide2.QtWidgets import QWidget,QFrame,QDesktopWidget,QLabel,QLineEdit,QPushButton
from PySide2.QtCore import Qt
from PySide2.QtGui import QImage,QPixmap

class Main_Window(QMainWindow):
    def __init__(self):
        super(Main_Window,self).__init__()
        self.setWindowTitle("Welcome Window")
        #self.setGeometry(350,250,550,400)
        self.fg = self.frameGeometry()
        self.cp = QDesktopWidget().availableGeometry().center()
        self.fg.moveCenter(self.cp)
        self.move(self.fg.topLeft())
        self.setFixedSize(550,400)

        self.setUp_GUI()

    def setUp_GUI(self):
        '''Generate all UI Elements'''
        #MenuBar
        self.Create_MenuBar()
        #StatusBar
        self.Create_StatusBar()
        #ToolBar
        self.Create_ToolBar()
        #DockWidget
        self.Create_DockWidget()
        #CentralWidget
        self.Create_CentralWidget()

    #MenuBar
    def Create_MenuBar(self):
        return
    #StatusBar
    def Create_StatusBar(self):
        return
    #ToolBar
    def Create_ToolBar(self):
        return
    #DockWidget
    def Create_DockWidget(self):
        return
    #CentralWidget
    def Create_CentralWidget(self):
        self.Main_Widget = Main_Widget()
        self.setCentralWidget(self.Main_Widget)

class Main_Widget(QWidget):
    def __init__(self,parent=None):
        super(Main_Widget,self).__init__(parent)
        self.setUp_UI()

    def setUp_UI(self):
        self.layout = QHBoxLayout()
        self.stack = QStackedWidget(parent=self)
        self.welcome = Welcome_Widget()
        self.stack = QStackedWidget(parent=self)
        self.welcome.login.Button_Login.clicked.connect(
            self.check_user_details)
        self.user = User_Widget(parent=self)
        self.user.Button_Quit.clicked.connect(self.user_quit)
        self.stack.addWidget(self.welcome)
        self.stack.addWidget(self.user)
        self.layout.addWidget(self.stack)

    def check_user_details(self):
        self.stack.setCurrentWidget(self.user)

    def user_quit(self):
        self.stack.setCurrentWidget(self.welcome)

class Welcome_Widget(QWidget):
    def __init__(self,parent=None):
        super(Welcome_Widget,self).__init__(parent)
        self.setUp_UI()

    def setUp_UI(self):
        self.image = Image_Widget(self)
        self.line = QFrame()
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.login = Login_Widget(self)
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.image)
        self.layout.addWidget(self.line)
        self.layout.addWidget(self.login)

        self.setLayout(self.layout)

class Image_Widget(QWidget):
    def __init__(self,parent=None):
        super(Image_Widget,self).__init__(parent)
        self.setUp_GUI()

    def setUp_GUI(self):
        self.label = QLabel()
        self.image = QImage('images\sec_cyber.jpg')
        # To scale image for example and keep its Aspect Ration
        #self.image.scaled(10,10,aspectRatioMode=Qt.IgnoreAspectRatio,transformMode=Qt.FastTransformation)
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)
        self.setFixedSize(260,360)
        self.setLayout(self.layout)

class Login_Widget(QWidget):
    '''Our Login Display Window'''
    def __init__(self,parent=None):
        '''Constructor Function'''
        super(Login_Widget,self).__init__(parent)
        self.setUp_Login_UI()

    def setUp_Login_UI(self):
        self.Login_Form = QFormLayout()
        self.setFixedSize(260,360)
        self.Label_User_Name = QLabel("User Name:")
        self.Label_User_Password = QLabel("Password")
        self.Txt_User_Name = QLineEdit()
        self.Txt_User_Password = QLineEdit()
        self.Txt_User_Password.setEchoMode(QLineEdit.Password)
        self.Button_Login = QPushButton("Login")
        self.Login_Form.addRow(self.Label_User_Name,self.Txt_User_Name)
        self.Login_Form.addRow(self.Label_User_Password,self.Txt_User_Password)
        self.Login_Form.addRow(self.Button_Login)
        self.Login_Form.setFormAlignment(Qt.AlignCenter)
        self.setLayout(self.Login_Form)

class User_Widget(QWidget):
    def __init__(self, parent):
        super(User_Widget, self).__init__(parent)
        self.init_UI()

    def init_UI(self):
        self.Button_Quit = QPushButton('Quit', parent=self)