import sys
#UI Imports
from ui_components.mainWindow_class import Main_Window
#PySide2 Imports
from PySide2.QtWidgets import QApplication

def Main_Logic():
    try:
        myApp = QApplication(sys.argv)
        myWin = Main_Window()
        myWin.show()
        myApp.exec_()
    except NameError:
        print("Name Error:",sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])

if __name__ == '__main__':
    Main_Logic()