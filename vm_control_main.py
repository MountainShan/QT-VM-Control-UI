from PyQt5 import QtWidgets
from vm_control_ui import Ui_VMController
import sys


class VMController(QtWidgets.QMainWindow):
    def __init__(self):
        super(VMController, self).__init__()
        self.ui = Ui_VMController()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = VMController()
    window.show()
    sys.exit(app.exec_())