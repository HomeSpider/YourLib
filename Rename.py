class ReName(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(400, 100)
        self.move(350, 150)
        self.setWindowTitle('Renaming...')
        self.setWindowIcon(QIcon('notebook.jpg'))

        self.vbox = QVBoxLayout(self)

        self.label = QLabel("Enter New Name, Please", self)
        self.label.resize(100, 40)
        self.vbox.addWidget(self.label)

        self.note = QTextEdit(self)
        self.note.resize(300, 40)
        self.vbox.addWidget(self.note)

        self.hbox = QHBoxLayout(self)

        self.button = QPushButton("Cancel", self)
        self.button.clicked.connect(self.close)
        self.hbox.addWidget(self.button)

        self.button = QPushButton("Save", self)
        self.button.clicked.connect(self.save)
        self.hbox.addWidget(self.button)

        self.vbox.addLayout(self.hbox)

        self.setLayout(self.vbox)

        self.pal = self.palette()
        self.pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QColor("#C0C0C0"))
        self.setPalette(self.pal)

    def save(self):
        self.text = self.note.toPlainText()
        Sharing(self.text)
        #self.c = Connect()
        #self.c.rename.connect(NFile(1))
        #self.c.rename.emit()
        me = NFile(1)
        self.close()
        
class Connect(QObject):
    rename = pyqtSignal()

class Sharing():
    def __init__(self, name):
        self.name = name
        with open ("name.txt", "w") as file:
            file.write(self.name)
    def get(self):
        with open ("name.txt", "r") as file:
            self.name = file.read()
        return self.name