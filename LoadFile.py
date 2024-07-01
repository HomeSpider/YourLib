import sys, os, datetime, time
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, qApp, QApplication,  QHBoxLayout,  QVBoxLayout, QTextEdit, QLabel, QPushButton, QPlainTextEdit, QLineEdit, QFrame
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from PyQt5.QtGui import QIcon, QFont, QColor 
import sqlite3
from NewFile import SaveW
from OFile import OpenFile

class LoadFile(QWidget):
    def __init__(self):
        super().__init__()
        LoadFile = QWidget(self)
        self.resize(250, 100)
        self.move(400, 300)
        self.setWindowTitle('File Opening')
        self.setWindowIcon(QIcon('croco.png'))

        self.pal = self.palette()
        self.pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QColor("#C8E9E9"))
        self.setPalette(self.pal) 

        self.search = QLineEdit(self)
        self.search2 = QLineEdit(self)

        self.lbl = QLabel("Enter name of the file:")
        self.lbl.resize(250, 50)
        self.lbl.setFont(QFont('TimesNewRoman', 16))

        self.lbl2 = QLabel("Enter the file extension:")
        self.lbl2.resize(250, 50)
        self.lbl2.setFont(QFont('TimesNewRoman', 16))

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.lbl)
        vbox.addWidget(self.search)
        vbox.addWidget(self.lbl2)
        vbox.addWidget(self.search2)

        hbox = QHBoxLayout(self)
        button1 = QPushButton("Back", self)
        button1.clicked.connect(self.close)
        hbox.addWidget(button1)
        button2 = QPushButton("Continue", self)
        button2.clicked.connect(self.open)
        hbox.addWidget(button2)
        vbox.addLayout(hbox)
    def open(self):
        self.conn=sqlite3.connect("files.db")
        self.cursor=self.conn.cursor()

        self.name = self.search.text()
        self.exp = self.search2.text()
        time = datetime.datetime.now()
        if self.exp.lower() == "txt":
            with open ("{}.txt".format(self.name), "r") as file:
                self.text = file.read()
            sql = self.cursor.execute("""INSERT INTO worktable (Name, Text, Time, Tegs, Tegs1, Tegs2, Tegs3, Tegs4, Tegs5)
                 VALUES('{}', '{}', '{}', '0', '0', '0', '0', '0', '0') """.format(self.name, self.text, time))
            self.conn.commit()

            self.SaveW = SaveW()
            self.SaveW.resize(250, 100)
            self.SaveW.move(400, 400)
            self.SaveW.show()
            self.notext()
            self.close()
            self.OFile = OpenFile(self.name)
            self.OFile.show()
        else:
            self.NoData = NoData()
            self.NoData.resize(250, 100)
            self.NoData.move(400, 400)
            self.NoData.show()
            self.notext()

    def notext(self):
        self.search.clear()
        self.search2.clear()
        self.update()

class NoData(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(QtCore.Qt.Popup)
        self.resize(180, 50)
        self.move(600, 400)

        self.label = QLabel("No data found.", self)

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