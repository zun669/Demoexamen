from PyQt5 import QtWidgets
from PyQt5.QtWidgets import ( QDialog )

class Operator(QDialog):
    def __init__(self):        
        super(Operator, self).__init__()
        print("Проверка открытия страницы оператора")