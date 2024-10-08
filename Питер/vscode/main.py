from PyQt5 import QtWidgets
from PyQt5.QtWidgets import ( QApplication ) 

import sys 
from PyQt5.QtGui import QPixmap, QIcon
from dialog2 import dialog

app = QApplication(sys.argv)

welcome = dialog()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)

icon = QIcon()
icon.addPixmap(QPixmap("logopiter.png"), QIcon.Normal, QIcon.Off)
widget.setWindowIcon(icon)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("You close application")

