from PyQt5.QtWidgets import *
from view import *
from functions import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.submit())
        self.pushButton_2.clicked.connect(lambda: self.delete())

    def submit(self):
        try:
            value_x = float(self.lineEdit_4.text())
            exponent_y = float(self.lineEdit.text())
            cats = int(self.lineEdit_2.text())
            aliens = int(self.lineEdit_3.text())
            catEars = cat_ears(cats)
            alien = alien_ears(aliens)
            exponent = power(value_x, exponent_y)
            self.label_5.setText(f'                                 SUMMARY   \n'
                                 f'                       Exponent product:       {exponent:.2f}\n'
                                 f'                       Cat ears in total:          {catEars}\n'
                                 f'                       Alien ears in total:        {alien}')
        except ValueError:
            self.label_5.setText('exponent, cat ears, and alien ears \nneed to be numeric \ne. g. 10, 1, 5, '
                                 'cannot have decimal place')

        except RuntimeError:
            self.label_5.setText('Cat ears and Alien ears must be positive integers.')

    def delete(self):
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.label_5.setText('')
