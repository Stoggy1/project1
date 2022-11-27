from PyQt5.QtWidgets import *
from view import *
from main import *

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
            exponent = int(self.lineEdit.text())
            cats = int(self.lineEdit_2.text())
            aliens = int(self.lineEdit_3.text())
            catEars = cat_ears(cats)
            alien = alien_ears(aliens)
            self.label_5.setText(f'        SUMMARY   \n'
                                 f'     Exponent product:           {exponent}\n'
                                 f'     Cat ears in total:          {catEars}\n'
                                 f'     Alien ears in total:        {alien}')
        except:
            self.label_5.setText('exponent, cat ears, and alien ears \nneed to be numeric \ne. g. 10, 1, 5, '
                                 'cannot have decimal place')

    def delete(self):
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.lineedit_4.setText('')
        self.label_5.setText('')