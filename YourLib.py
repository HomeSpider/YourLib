import sys, os, datetime, time
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, qApp, QApplication,  QHBoxLayout,  QVBoxLayout, QTextEdit, QLabel, QPushButton, QPlainTextEdit, QLineEdit, QFrame, QScrollArea, QGridLayout, QComboBox
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QSignalMapper
from PyQt5.QtGui import QIcon, QFont, QColor, QMouseEvent

import sqlite3

from NewFile import NFile, Tables
from LoadFile import LoadFile
from OFile import OpenFile
from DelFile import DelFile

#refresh after deleting + changing files

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.n = 0
        self.initUI()

        self.tables = Tables()

        self.initlists()
        self.window = QWidget(self)
        self.window.setLayout(self.hbox)
        self.setCentralWidget(self.window)

       
        self.resize(1000, 800)
        self.move(200, 0)
        self.setWindowTitle('Your Library')
        self.setWindowIcon(QIcon('notepad.png')) 
        self.pal = self.palette()
        self.pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QColor("#C0C0C0"))
        self.pal.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.Window, QtGui.QColor("#C0C0C1"))
        self.setPalette(self.pal) 
        
        self.show()
        sys.exit(app.exec_())

    
    def initUI(self):

        self.exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setStatusTip('Exit application')
        self.exitAction.triggered.connect(qApp.quit)

        self.statbar=self.statusBar()

        self.menubar = self.menuBar()
        self.fileMenu = self.menubar.addMenu('&Help me!')
        self.fileMenu.addAction(self.exitAction) 

        self.fileMenu = self.menubar.addMenu('&New File')
        self.create1 = QAction('&Add from files', self) 
        self.create1.triggered.connect(self.LFile)
        self.fileMenu.addAction(self.create1) 

        self.create2 = QAction('&Create', self) 
        self.create2.triggered.connect(self.NFile)
        self.fileMenu.addAction(self.create2)

        self.fileMenu = self.menubar.addMenu('&Edit File')
        self.openf = QAction('&Open', self) 
        self.openf.triggered.connect(self.OFile)
        self.fileMenu.addAction(self.openf)

        self.fileMenu = self.menubar.addMenu('&Del File')
        self.delf = QAction('&Delete', self) 
        self.delf.triggered.connect(self.DFile)
        self.fileMenu.addAction(self.delf)

    def LFile(self):
        self.LoadFile = LoadFile()
        self.LoadFile.show()

    def OFile(self):
        self.OFile = OpenFile()
        self.OFile.show()

    def NFile(self):
        self.NFile = NFile(0)
        self.NFile.show()

    def DFile(self):
        self.DFile = DelFile()
        self.DFile.show()

    def leftlist (self):
        self.conn=sqlite3.connect("files.db")
        self.cursor=self.conn.cursor()
        sql=self.cursor.execute("""select * from worktable """)
        self.grid = QGridLayout()
        for i in sql.fetchall():
            self.label = QLabel("<b>{}</b>: {}".format(i[0], i[1]))
            self.label.setFont(QFont('TimesNewRoman', 18))
            self.label.setMaximumSize(450, 800)
            self.label.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')
            self.grid.addWidget(self.label, self.n, 1)
            self.n += 1

        self.hbox = QHBoxLayout(self)
        widget = QWidget()
        widget.setLayout(self.grid)
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(widget)
        self.hbox.addWidget(self.scroll)
        self.update()

    def initlists (self):
        self.leftlist()
        vbox = QVBoxLayout(self)
        self.vbox2 = QVBoxLayout()
        button = QPushButton("Refresh Page", self)
        button.clicked.connect(self.up)
        self.cbox = QComboBox()
        sql=self.cursor.execute("""select Tegs, Tegs1, Tegs2, Tegs3, Tegs4, Tegs5 from worktable """)

        list1 = []

        for i in sql.fetchall():
            for j in i:
                if j != '0' or j == "''":
                    list1.append(j)

        for i in list1:
            while list1.count(i)>1:
                list1.pop(list1.index(i))

        for i in list1:
            self.cbox.addItem(i)

        label = QLabel(" ")
        label.setFont(QFont('TimesNewRoman', 18))
        label.setMinimumSize(450, 10)
        
        button2 = QPushButton("Search", self)
        button2.clicked.connect(self.search)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(button)
        hbox2.addWidget(button2)

        button3 = QPushButton("Clear", self)
        button3.clicked.connect(self.clear)
        button4 = QPushButton("Open", self)
        button4.clicked.connect(self.openclear)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(button3)
        hbox3.addWidget(button4)

        self.vbox2.addLayout(hbox2)
        self.vbox2.addLayout(hbox3)
        self.vbox2.addWidget(label)
        self.vbox2.addWidget(self.cbox)
        self.vbox2.addStretch(0)

        self.vbox3 = QVBoxLayout()
        self.vbox3.addStretch(0)

        self.vbox2.addLayout(self.vbox3)
        self.hbox.addLayout(self.vbox2)

    def up(self):
        self.conn=sqlite3.connect("files.db")
        self.cursor=self.conn.cursor()
        sql=self.cursor.execute("""select * from worktable """)
        listwork = []
        for i in sql.fetchall():
            listwork.append(i)
        n = 0
        for i in listwork:
            if n == self.n:
                self.label = QLabel("<b>{}</b>: {}".format(i[0], i[1]))
                self.label.setFont(QFont('TimesNewRoman', 18))
                self.label.setMaximumSize(450, 800)
                self.label.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')
                self.grid.addWidget(self.label, self.n, 1)
            n+=1
        self.repaint()

    def clear(self):
        while self.vbox3.count():
            child = self.vbox3.takeAt(0)
            if child.widget() is not None:
                    child.widget().deleteLater()
            elif child.layout() is not None:
                    clearLayout(child.layout())
    def openclear(self):
        self.OFile()

    def open(self, event):
        self.OFile(open=self.label2)
        
    def search(self):
        text = self.cbox.currentText()
        sql=self.cursor.execute("""select * from worktable 
                                WHERE Tegs like "{0}" OR Tegs1 like "{0}" OR Tegs2 like "{0}" OR Tegs3 like "{0}" OR Tegs4 like "{0}" OR Tegs5 like "{0}"
                                """.format(text))
        n = 0

        self.grid2 = QGridLayout()
        widget = QWidget()
        widget.setLayout(self.grid2)
        self.scroll2 = QScrollArea()
        self.scroll2.setWidgetResizable(True)
        self.scroll2.setWidget(widget)
        self.vbox3.addWidget(self.scroll2)
        self.mapper = QtCore.QSignalMapper()

        for i in sql.fetchall():
            self.label2 = QLabel("<b>{}</b>: {}".format(i[0], i[1]))
            self.label2.setFont(QFont('TimesNewRoman', 18))
            self.label2.setMaximumSize(450, 800)
            self.label2.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')
            self.label2.mousePressEvent = self.open
            self.grid2.addWidget(self.label2, n, 1)
            n = n+1
            
        self.update()



if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex=Main()

