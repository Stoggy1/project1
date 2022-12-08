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

    def submit(self) -> None:
        """
        This method is called when the 'submit' button is clicked. It gets the
    values from the line edits
        and calls the relevant functions. If a value error is raised, it
    displays an error message. If a
        runtime error is raised, it displays an error message. If a
    runtime warning is raised, it displays
        an error message.
        """

        try:
            value_x = float(self.lineEdit.text())
            exponent_y = float(self.lineEdit_4.text())
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
            self.label_6.setText('both ears must be positive and below 993')

        except RuntimeWarning:
            self.label_7.setText('Exponent is too big for computer to compute.')

    def delete(self) -> None:
        """
            This method is called when the 'delete' button is clicked. It resets the values of all the line edits
            and labels to be empty.
        """
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.label_5.setText('')
        self.label_6.setText('')
        self.label_7.setText('')
