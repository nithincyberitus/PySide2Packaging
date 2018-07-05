# UI Imports
from .windowLayout_class import Layout_Main_Window
# PySide2 Imports
from PySide2.QtWidgets import QMainWindow,QDesktopWidget

class Main_Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle("DigiLock")
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
        self.Create_Toolbar()
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
    def Create_Toolbar(self):
        return
    #DockWidget
    def Create_DockWidget(self):
        return
    #CentralWidget
    def Create_CentralWidget(self):
        self.Main_Layout = Layout_Main_Window()
        self.setCentralWidget(self.Main_Layout)

if __name__ == '__main__':
    pass