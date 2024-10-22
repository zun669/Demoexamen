from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QDialog, QWidget)

from PyQt5.uic import loadUi 

import sqlite3

class dialog (QDialog):
    def __init__(self):
        super(dialog, self).__init__()
        loadUi ('dialog2.ui', self)
        self.PasswordField.setEchoMode(QtWidgets.QLineEdit.Password) 
        self.SignInButton.clicked.connect(self.signupfunction) 
       

        self.AvtorButton.clicked.connect(self.sign_out)
        self.AvtorButton.hide()
        self.stackedWidget.currentChanged.connect(self.hiddenButton)

    def signupfunction(self): 
        
        user = self.LoginField.text() 
        password = self.PasswordField.text() 
        print(user, password) 

        if len(user)==0 or len(password)==0: 
            self.ErrorField.setText("Заполните все поля") 
        else:
            self.ErrorField.setText(" ")
            conn = sqlite3.connect("uchet.db") 
            cur = conn.cursor() 

            cur.execute('SELECT typeID FROM users WHERE login=(?) and password=(?)', [user, password]) 
            typeUser = cur.fetchone() 
            if typeUser == None:
                self.ErrorField.setText("Пользователь с такими данными не найден")
            elif typeUser[0] == 1:
                self.stackedWidget.setCurrentWidget(self.Manager)
                self.lybaya = Manager()
            elif typeUser[0] == 2:
                self.stackedWidget.setCurrentWidget(self.Master)
                self.lybaya = Master()
            elif typeUser[0] == 3:
                self.stackedWidget.setCurrentWidget(self.Operator)
                self.lybaya = Operator()
            elif typeUser[0] == 4:
                self.stackedWidget.setCurrentWidget(self.Zakazchik)
                self.lybaya = Zakazchik()            

            conn.commit() 
            conn.close() 
    
    def hiddenButton(self):
        if self.stackedWidget.currentWidget() == self.Avtorisation:  
            self.AvtorButton.hide()
        else:
            self.AvtorButton.show()
    
    def sign_out(self):
        self.stackedWidget.setCurrentWidget(self.Avtorisation)

class Manager(QDialog):
    def __init__(self):        
        super(Manager, self).__init__()
        print("Проверка открытия страницы менеджера")

class Master(QDialog):
    def __init__(self):        
        super(Master, self).__init__()
        print("Проверка открытия страницы мастера")

class Operator(QDialog):
    def __init__(self):        
        super(Operator, self).__init__()
        print("Проверка открытия страницы оператора")

class Zakazchik(QDialog):
    def __init__(self):        
        super(Zakazchik, self).__init__()
        print("Проверка открытия страницы заказчика")
         
        