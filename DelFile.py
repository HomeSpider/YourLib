import sys, os, datetime, time
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, qApp, QApplication,  QHBoxLayout,  QVBoxLayout, QTextEdit, QLabel, QPushButton, QPlainTextEdit, QLineEdit, QFrame, QScrollArea, QGridLayout, QComboBox, QMessageBox
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QSignalMapper
from PyQt5.QtGui import QIcon, QFont, QColor, QMouseEvent

import sqlite3

class DelFile(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 600)
        self.move(300, 100)
        self.setWindowTitle('Delete File')
        self.setWindowIcon(QIcon('trash.png'))

        self.pal = self.palette()
        self.pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QColor("#C8E9E9"))
        self.setPalette(self.pal)

        self.page()

    def page(self):

        self.pagesC = 0
        self.conn=sqlite3.connect("files.db")
        self.cursor=self.conn.cursor()
        sql=self.cursor.execute("""select * from worktable """)

        self.counter = 0
        self.listwork = []
        listwork = []
        n = 0

        for i in sql.fetchall():
            listwork.append(i)

        for i in listwork:
            while self.counter <= 6:
                self.counter = self.counter+1
                try:
                    self.listwork.append(listwork[n])
                except:
                    self.listwork.append(["No Data", "Meow <3"])
                n+=1
                if self.counter%6==0:
                    self.createpage(self.listwork)
                    self.listwork.clear()

    def next (self):
        self.pagesC = self.pagesC+1
        n = 0
        k = 6
        
        self.conn=sqlite3.connect("files.db")
        self.cursor=self.conn.cursor()
        sql=self.cursor.execute("""select * from worktable """)

        listn = []

        for i in sql.fetchall():
            listn.append(i)
            
        num = len(listn)/6
        print(num)
        self.counter3 = 0

        if self.pagesC>num:
            self.DelW = DelW("No page is found.")
            self.DelW.show()
            self.pagesC = self.pagesC-1
        else:
            for i in listn:
                if self.counter3 == n:
                    self.counter3 = self.counter3+1
                    try:
                        self.listwork.append(listn[n])
                    except:
                        self.listwork.append(["No Data", "Meow <3"])
                    if self.counter3 == k*self.pagesC:
                        if self.pagesC == self.l:
                            self.l=self.l+1
                            break
                        elif self.pagesC<self.l:
                            self.listwork.clear()
                            self.l=self.l+1
                n = n+1
        

        print(self.listwork)
        d=0
        self.notext()

        for i in self.listwork:
            if d==0:
                self.label.setText("<b>{}</b>: {}".format(i[0], i[1]))
            elif d==1:
                self.label2.setText("<b>{}</b>: {}".format(i[0], i[1]))
            elif d==2:
                self.label3.setText("<b>{}</b>: {}".format(i[0], i[1]))
            elif d==3:
                self.label4.setText("<b>{}</b>: {}".format(i[0], i[1]))
            elif d==4:
                self.label5.setText("<b>{}</b>: {}".format(i[0], i[1]))
            elif d==5:
                self.label6.setText("<b>{}</b>: {}".format(i[0], i[1]))
            d+=1
            
        print(self.pagesC)
        self.nump.setText("{}".format(self.pagesC))

        self.update()
        self.listwork.clear()

    def back (self):
        self.pagesC=self.pagesC-1
        if self.pagesC == 0:
            self.DelW = DelW("No page is found.")
            self.DelW.show()
            self.pagesC+=1
        else:
            self.conn=sqlite3.connect("files.db")
            self.cursor=self.conn.cursor()
            sql=self.cursor.execute("""select * from worktable """)

            listn = []
            n = 0
            k = 6
            print("page = ",self.pagesC)
            self.counter2 = 0

            for i in sql.fetchall():
                listn.append(i)

            for i in listn:
                if self.counter2 == n:
                    self.counter2 = self.counter2+1
                    try:
                        self.listwork.append(listn[n])
                    except:
                        self.listwork.append(["No Data", "Meow <3"])
                    if self.counter2 == k*self.pagesC:
                        if self.pagesC == self.l-1:
                            self.l=self.l-1
                            print(self.listwork)
                            break
                        elif self.pagesC<self.l:
                            self.listwork.clear()
                            self.l=self.l-1
                n = n+1
            
            print(self.listwork)
            self.notext()
            d = 0
            for i in self.listwork:
                if d==0:
                    self.label.setText("<b>{}</b>: {}".format(i[0], i[1]))
                elif d==1:
                    self.label2.setText("<b>{}</b>: {}".format(i[0], i[1]))
                elif d==2:
                    self.label3.setText("<b>{}</b>: {}".format(i[0], i[1]))
                elif d==3:
                    self.label4.setText("<b>{}</b>: {}".format(i[0], i[1]))
                elif d==4:
                    self.label5.setText("<b>{}</b>: {}".format(i[0], i[1]))
                elif d==5:
                    self.label6.setText("<b>{}</b>: {}".format(i[0], i[1]))
                d+=1

            self.nump.setText("{}".format(self.pagesC))
            self.listwork.clear()
            self.update()

    def notext (self):
        self.label.setText("<b>No data</b>: Meow <3")
        self.label2.setText("<b>No data</b>: Meow <3")
        self.label3.setText("<b>No data</b>: Meow <3")
        self.label4.setText("<b>No data</b>: Meow <3")
        self.label5.setText("<b>No data</b>: Meow <3")
        self.label6.setText("<b>No data</b>: Meow <3")

    def createpage(self, listwork):
        self.l = 2
        self.d = 1
        self.pagesC+=1
        n=0
        print(listwork)

        for i in listwork:
            if n==0:
                self.label = QLabel("<b>{}</b>: {}".format(i[0], i[1]))
            elif n==1:
                self.label2 = QLabel("<b>{}</b>: {}".format(i[0], i[1]))
            elif n==2:
                self.label3 = QLabel("<b>{}</b>: {}".format(i[0], i[1]))
            elif n==3:
                self.label4 = QLabel("<b>{}</b>: {}".format(i[0], i[1]))
            elif n==4:
                self.label5 = QLabel("<b>{}</b>: {}".format(i[0], i[1]))
            elif n==5:
                self.label6 = QLabel("<b>{}</b>: {}".format(i[0], i[1]))
            n+=1
        
        self.label.setFont(QFont('TimesNewRoman', 18))
        self.label.setMaximumSize(450, 600)
        self.label.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')
        self.label.mousePressEvent = self.delete

        self.label2.setFont(QFont('TimesNewRoman', 18))
        self.label2.setMaximumSize(450, 600)
        self.label2.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')
        self.label2.mousePressEvent = self.delete2

        self.label3.setFont(QFont('TimesNewRoman', 18))
        self.label3.setMaximumSize(450, 600)
        self.label3.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')
        self.label3.mousePressEvent = self.delete3

        self.label4.setFont(QFont('TimesNewRoman', 18))
        self.label4.setMaximumSize(450, 600)
        self.label4.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')
        self.label4.mousePressEvent = self.delete4

        self.label5.setFont(QFont('TimesNewRoman', 18))
        self.label5.setMaximumSize(450, 600)
        self.label5.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')
        self.label5.mousePressEvent = self.delete5

        self.label6.setFont(QFont('TimesNewRoman', 18))
        self.label6.setMaximumSize(450, 600)
        self.label6.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')
        self.label6.mousePressEvent = self.delete6

        hbox1 = QHBoxLayout()
        self.button1 =  QPushButton("<")
        self.button1.clicked.connect(self.back)
        hbox1.addWidget(self.button1)
        self.nump = QLabel("{}".format(self.pagesC))
        self.nump.setAlignment(Qt.AlignCenter)
        hbox1.addWidget(self.nump)
        self.button2 =  QPushButton(">")
        self.button2.clicked.connect(self.next)
        hbox1.addWidget(self.button2)

        hbox2 = QHBoxLayout()
        self.button3 =  QPushButton("Delete All")
        self.button3.clicked.connect(self.deletion)
        hbox2.addWidget(self.button3)
        self.button4 =  QPushButton("Close")
        self.button4.clicked.connect(self.close)
        hbox2.addWidget(self.button4)

        vbox1 = QVBoxLayout(self)
        vbox1.addLayout(hbox2)
        vbox1.addWidget(self.label)
        vbox1.addWidget(self.label2)
        vbox1.addWidget(self.label3)
        vbox1.addWidget(self.label4)
        vbox1.addWidget(self.label5)
        vbox1.addWidget(self.label6)
        vbox1.addLayout(hbox1)

        self.update()
        self.repaint()
        print(self.pagesC)

    def delete (self, event):
        self.delconf(self.label)
    def delete2 (self, event):
        self.delconf(self.label2)
    def delete3 (self, event):
        self.delconf(self.label3)
    def delete4 (self, event):
        self.delconf(self.label4)
    def delete5 (self, event):
        self.delconf(self.label5)
    def delete6 (self, event):
        self.delconf(self.label6)
    
    def delconf(self, label):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Question)
        msg.setWindowTitle('Deletion')
        msg.setText('Do you really want to delete data?')

        self.worklabel = label

        yes = msg.addButton('Yes', QMessageBox.AcceptRole)
        yes.clicked.connect(self.delone)
        no = msg.addButton('No', QMessageBox.RejectRole)
        no.clicked.connect(msg.close)

        msg.setDefaultButton(yes)
        msg.show()

    def delone(self):
        self.worklabel.hide()
        self.delSQL(self.worklabel.text())

    def delSQL(self, label):
        n=0
        for i in label.split(":"):
            if n == 0:
                name = i.strip()[3:][:-4]
            n+=1
        self.conn=sqlite3.connect("files.db")
        self.cursor=self.conn.cursor()
        sql=self.cursor.execute("""delete from worktable 
                                where Name = "{}" """.format(name)) 
        self.conn.commit()

        self.DelW = DelW("File is deleted.")
        self.DelW.show()

    def deletion (self):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Question)
        msg.setWindowTitle('Deletion')
        msg.setText('Do you really want to delete all?')

        yes = msg.addButton('Yes', QMessageBox.AcceptRole)
        yes.clicked.connect(self.delTrue)
        no = msg.addButton('No', QMessageBox.RejectRole)
        no.clicked.connect(msg.close)

        msg.setDefaultButton(yes)
        msg.show()

    def delTrue(self):
        self.conn=sqlite3.connect("files.db")
        self.cursor=self.conn.cursor()
        sql=self.cursor.execute(""" DELETE from worktable """)
        self.conn.commit()

        self.DelW = DelW("File is deleted.")
        self.DelW.show()

        self.notext()
        self.update()

        self.close()

class DelW(QWidget):
    def __init__(self, name):
        super().__init__()

        self.setWindowFlags(QtCore.Qt.Popup)
        self.resize(180, 50)
        self.move(600, 400)

        self.label = QLabel("{}".format(name), self)

        self.label.setFont(QFont('TimesNewRoman', 18))
        self.label.setAlignment(Qt.AlignCenter)

        self.pal = self.palette()
        self.pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QColor("#FFFFFF"))
        self.setPalette(self.pal)

        vbox = QVBoxLayout()
        button = QPushButton("OK", self)
        button.clicked.connect(self.close)
        vbox.addWidget(self.label)
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(button)
        vbox.addLayout(hbox)
        self.setLayout(vbox)