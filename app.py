import sys
from PySide2.QtWidgets import QApplication

from ui_components import Main_Window

def main():
    try:
        myApp = QApplication(sys.argv)
        myWin = Main_Window()
        myWin.show()
        myApp.exec_()
    except NameError:
        print("Name Error...",sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])

if __name__ == '__main__':
    main()