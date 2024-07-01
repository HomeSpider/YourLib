import sys, os, datetime, time
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, qApp, QApplication,  QHBoxLayout,  QVBoxLayout, QTextEdit, QLabel, QPushButton, QPlainTextEdit, QLineEdit, QFrame, QScrollArea, QGridLayout, QComboBox
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QSignalMapper
from PyQt5.QtGui import QIcon, QFont, QColor, QMouseEvent 
import sqlite3


class OpenFile(QWidget):
    def __init__(self, open=0):
        super().__init__()
        self.resize(800, 600)
        self.move(300, 100)
        self.name = 'Notebook'
        self.setWindowTitle(self.name)
        self.setWindowIcon(QIcon('notebook.jpg'))

        self.pal = self.palette()
        self.pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QColor("#C8E9E9"))
        self.setPalette(self.pal) 

        vbox = QVBoxLayout(self)

        hbox1 = QHBoxLayout(self)
        self.namelbl = QLabel("Choose File Name:")
        self.namelbl.setFont(QFont('TimesNewRoman', 10))
        self.namelbl.setAlignment(Qt.AlignCenter)
        hbox1.addWidget(self.namelbl)
        self.name = QComboBox(self)
        self.namecom = QPushButton("Open File", self)
        self.namecom.clicked.connect(self.com)

        hbox2 = QHBoxLayout(self)
        self.namelbl2 = QLabel("Change File Name:")
        self.namelbl2.setFont(QFont('TimesNewRoman', 10))
        self.namelbl2.setAlignment(Qt.AlignCenter)
        hbox2.addWidget(self.namelbl2)
        self.namet = QLineEdit(self)
        hbox2.addWidget(self.namet)

        self.conn=sqlite3.connect("files.db")
        self.cursor=self.conn.cursor()

        sql=self.cursor.execute("""select Name from worktable """)

        list1=[]

        for i in sql.fetchall():
            for j in i:
                if j != '0' or j == "''":
                    list1.append(j)

        for i in list1:
            while list1.count(i)>1:
                list1.pop(list1.index(i))

        for i in list1:
            self.name.addItem(i)

        hbox1.addWidget(self.name)
        hbox1.addWidget(self.namecom)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.note = QTextEdit(self)
        self.note.resize(775, 600)
        self.note.setAlignment(Qt.AlignLeft)
        self.note.setCurrentFont(QFont('TimesNewRoman'))
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.note)
        vbox.addWidget(self.scroll)

        self.tegslbl = QLabel("Enter Tegs:")
        self.tegslbl.resize(5, 600)
        self.tegslbl.setFont(QFont('TimesNewRoman', 12))
        self.tegslbl.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.tegslbl)

        hbox = QHBoxLayout(self)
        self.tegs = QLineEdit(self)
        hbox.addWidget(self.tegs)
        
        self.tegs1 = QLineEdit(self)
        hbox.addWidget(self.tegs1)

        self.tegs2 = QLineEdit(self)
        hbox.addWidget(self.tegs2)

        self.tegs3 = QLineEdit(self)
        hbox.addWidget(self.tegs3)

        self.tegs4 = QLineEdit(self)
        hbox.addWidget(self.tegs4)

        self.tegs5 = QLineEdit(self)
        hbox.addWidget(self.tegs5)
        vbox.addLayout(hbox)

        hbox3 = QHBoxLayout(self)
        hbox3.addStretch(1)
        self.button1 =  QPushButton("Save", self)
        self.button1.clicked.connect(self.Save)
        hbox3.addWidget(self.button1)
        vbox.addLayout(hbox3)

        self.basecheck()

        if open!=0:
            self.name.setCurrentText(open)
            self.com()

    def com(self):
        search = self.name.currentText()
        sql=self.cursor.execute("""select * from worktable 
                                    where Name = "{}" """.format(search))
        list2 = []
        for i in sql.fetchall():
            for j in i:
                list2.append(j)
        
        self.namet.setText(list2[0])
        self.note.setText(list2[1])
        self.tegs.setText(list2[3])
        self.tegs1.setText(list2[4])
        self.tegs2.setText(list2[5])
        self.tegs3.setText(list2[6])
        self.tegs4.setText(list2[7])
        self.tegs5.setText(list2[8])

        self.update()

    def coopfile(self, nname, ttext):

        time.sleep(15)

        self.name.setText(nname)
        self.note.setText(ttext)
        self.update()

    def Save(self):

        self.nametext = self.namet.text()
        self.text = self.note.toPlainText()
        self.teg = self.tegs.text()
        self.teg1 = self.tegs1.text()
        self.teg2 = self.tegs2.text()
        self.teg3 = self.tegs3.text()
        self.teg4 = self.tegs4.text()
        self.teg5 = self.tegs5.text()
        self.namew = self.name.currentText()
        
        self.conn=sqlite3.connect("files.db")
        self.cursor=self.conn.cursor()

        time = datetime.datetime.now()
        print(time)

        sql = self.cursor.execute(""" UPDATE worktable 
                                    SET Name = "{}", Text = "{}", 
                                    Tegs = "{}", Tegs1 = "{}", 
                                    Tegs2 = "{}", Tegs3 = "{}", 
                                    Tegs4 = "{}", Tegs5 = "{}" 
                                    WHERE Name = "{}" """.format(self.nametext, self.text, self.teg, self.teg1, self.teg2, self.teg3, self.teg4, self.teg5, self.namew))
        self.conn.commit()

        self.SaveW = SaveW()
        self.SaveW.show()
        self.notext()
        
    def notext(self):
        self.name.clear()
        self.note.clear()
        self.tegs.clear()
        self.tegs1.clear()
        self.tegs2.clear()
        self.tegs3.clear()
        self.tegs4.clear()
        self.tegs5.clear()
        self.update()
        self.close()

    def basecheck(self):
        self.table = Tables()

class Tables():
    def __init__(self):
        
        self.conn=sqlite3.connect("files.db")
        self.cursor=self.conn.cursor()

        sql=self.cursor.execute(""" create table if not exists worktable (Name Text, Text Text, Time Text, Tegs Text, Tegs1 Text, Tegs2 Text, Tegs3 Text, Tegs4 Text, Tegs5 Text)""")
        self.conn.commit()

class SaveW(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(QtCore.Qt.Popup)
        self.resize(180, 50)
        self.move(600, 400)

        self.label = QLabel("File is saved.", self)

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