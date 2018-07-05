import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, \
    QDesktopWidget, QHBoxLayout, QGridLayout
import main

class ConvertUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # set size
        self.resize(600,400)
        # move to center
        qr = self.frameGeometry()
        qr.moveCenter(QDesktopWidget().availableGeometry().center())
        self.move(qr.topLeft())
        # window title
        self.setWindowTitle('Number converter')


        vbox = QVBoxLayout()

        label = QLabel("Введите число")
        label.move(10,10)

        self.n_field = QLineEdit()
        self.n_field.resize(self.n_field.sizeHint())

        applySize = QPushButton('Узнать название')
        applySize.resize(applySize.sizeHint())
        applySize.clicked.connect(self.getname_clicked)

        self.name = QLabel("")

        hbox = QHBoxLayout()
        hbox.addWidget(label)
        hbox.addWidget(self.n_field)
        hbox.addWidget(applySize)
        hbox.addWidget(self.name)
        vbox.addLayout(hbox);

        label = QLabel("Тип системы счисления")
        label.move(10, 10)

        self.basement_field = QLineEdit()
        self.basement_field.resize(self.basement_field.sizeHint())

        self.converted_number = QLabel("")
        convert = QPushButton('Перевести')
        convert.resize(convert.sizeHint())
        convert.clicked.connect(self.convert_clicked)
        hbox = QHBoxLayout()
        hbox.addWidget(label)
        hbox.addWidget(self.basement_field)
        hbox.addWidget(convert)
        hbox.addWidget(self.converted_number)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.show()

    @main.converted
    def converted(self, basement, number, result):
        self.converted_number.setText(result)
        self.converted_number.resize(self.converted_number.sizeHint())

    def convert_clicked(self):
        number = int(self.n_field.text())
        basement_type = self.basement_field.text()
        basement = main.get_basement(basement_type)
        self.converted(basement=basement, number=number)

    def getname_clicked(self):
        number = self.n_field.text()
        name = main.get_name(number=number)
        if name:
            self.name.setText(name)
        else:
            self.name.setText('Invalid digit')
        self.name.resize(self.n_field.sizeHint())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    convertui = ConvertUI()
    sys.exit(app.exec_())
