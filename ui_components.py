from PySide2.QtWidgets import QMainWindow,QWidget,QFrame,QDesktopWidget,QHBoxLayout,QLabel,QFormLayout,QLineEdit,QPushButton
from PySide2.QtCore import Qt,SIGNAL
from PySide2.QtGui import QImage,QPixmap

class Main_Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Login Window")
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
        self.Main_Layout = Layout_Main_Window()
        self.setCentralWidget(self.Main_Layout)

class Layout_Main_Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.Main_Layout = QHBoxLayout()
        self.Child_1 = Layout_Child_1()
        self.Child_2 = Layout_Child_2()
        self.Main_Layout.addWidget(self.Child_1)
        self.line = QFrame()
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.Main_Layout.addWidget(self.line)
        self.Main_Layout.addWidget(self.Child_2)
        self.setLayout(self.Main_Layout)

class Layout_Child_1(QFrame):
    def __init__(self):
        QFrame.__init__(self)
        self.setUp_GUI()

    def setUp_GUI(self):
        self.label = QLabel()
        self.image = QImage('images\sec_cyber.jpg')
        # To scale image for example and keep its Aspect Ration
        #self.image.scaled(0,0,aspectRatioMode=Qt.IgnoreAspectRatio,transformMode=Qt.FastTransformation)
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)


class Layout_Child_2(QWidget):
    '''Our Login Display Window'''
    def __init__(self):
        '''Constructor Function'''
        QWidget.__init__(self)
        self.setUp_Login_UI()

    def setUp_Login_UI(self):
        self.Login_Form = QFormLayout()
        self.setFixedSize(250,250)
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
        self.connect(self.Button_Login,SIGNAL("clicked()"),self.Check_Login_Details)

    def Check_Login_Details(self):
        
        self.username = self.Txt_User_Name.text()
        self.password = self.Txt_User_Password.text()

        url = 'http://127.0.0.1:5000/auth/user'
        
        payload = {'username':self.username,'password':self.password}
        
        resp = requests.post(url,params=payload)
        #print(resp.status_code)

        if resp.status_code == 200:
            # Go to New Window
            pass
        else:
            #Show Error
            pass
