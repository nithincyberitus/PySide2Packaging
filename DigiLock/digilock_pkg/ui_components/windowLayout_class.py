# UI Imports
from .childLayouts_class import Layout_Child_1,Layout_Child_2
# PySide2 Imports
from PySide2.QtWidgets import QWidget,QHBoxLayout,QFrame
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