from controller import *


def main() -> None:
    """
    This function creates a QApplication and a Controller instance. It sets the
controller to be the main window
    of the application, and shows the window.
    """
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
