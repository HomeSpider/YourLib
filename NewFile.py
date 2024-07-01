import sys, os, datetime, time
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, qApp, QApplication,  QHBoxLayout,  QVBoxLayout, QTextEdit, QLabel, QPushButton, QPlainTextEdit, QLineEdit, QFrame, QScrollArea, QGridLayout, QComboBox
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QSignalMapper
from PyQt5.QtGui import QIcon, QFont, QColor, QMouseEvent 
import sqlite3


class NFile(QWidget):
    def __init__(self, change):
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
        self.namelbl = QLabel("Enter File Name:")
        self.namelbl.setFont(QFont('TimesNewRoman', 10))
        self.namelbl.setAlignment(Qt.AlignCenter)
        hbox1.addWidget(self.namelbl)
        self.name = QLineEdit(self)
        hbox1.addWidget(self.name)
        vbox.addLayout(hbox1)

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

        if change == 1:
            self.ChangeName() 

    def coopfile(self, nname, ttext):

        time.sleep(15)

        self.name.setText(nname)
        self.note.setText(ttext)
        self.update()

    def Save(self):

        self.nametext = self.name.text()
        self.text = self.note.toPlainText()
        self.teg = self.tegs.text()
        self.teg1 = self.tegs1.text()
        self.teg2 = self.tegs2.text()
        self.teg3 = self.tegs3.text()
        self.teg4 = self.tegs4.text()
        self.teg5 = self.tegs5.text()
        
        self.conn=sqlite3.connect("files.db")
        self.cursor=self.conn.cursor()

        time = datetime.datetime.now()
        print(time)

        sql = self.cursor.execute(""" INSERT INTO worktable (Name, Text, Time, Tegs, Tegs1, Tegs2, Tegs3, Tegs4, Tegs5)
                 VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}') """.format(self.nametext, self.text, time, self.teg, self.teg1, self.teg2, self.teg3, self.teg4, self.teg5))
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