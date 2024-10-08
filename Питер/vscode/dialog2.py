from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QDialog, QWidget)

from PyQt5.uic import loadUi 

class dialog (QDialog):
    def __init__(self):
        super(dialog, self).__init__()
        loadUi ('dialog2.ui', self)
         
        