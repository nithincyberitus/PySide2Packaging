# Request Imports

#PySide 2 Imports
from PySide2.QtWidgets import QWidget,QFrame,QLabel,QHBoxLayout,QFormLayout,QLineEdit,QPushButton
from PySide2.QtGui import QImage,QPixmap
from PySide2.QtCore import SIGNAL

class Layout_Child_1(QFrame):
    def __init__(self):
        QFrame.__init__(self)
        self.setUp_GUI()

    def setUp_GUI(self):
        self.label = QLabel()
        self.image = QImage("images/sec_thumb.jpg")
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)


class Layout_Child_2(QWidget):
    def __init__(self):
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
        else:
            #Show Error