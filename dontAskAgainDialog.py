from PyQt5.QtCore import Qt, QSettings
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QHBoxLayout, QWidget, QLabel, QSpacerItem, QSizePolicy, \
    QCheckBox, QFrame


class DontAskAgainDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.__initVal()
        self.__initUi()

    def __initVal(self):
        self.__settings_ini = QSettings('settings.ini', QSettings.IniFormat)

        if not self.__settings_ini.contains('dont_ask_again'):
            self.__settings_ini.setValue('dont_ask_again', False)

        self.__dont_ask_again = self.__settings_ini.value('dont_ask_again', type=bool)

    def __initUi(self):
        self.setWindowTitle('Wait!')
        self.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint)
        self.__messageLbl = QLabel()
        self.__messageLbl.setText('Do you want to close this app?')
        self.__messageLbl.setContentsMargins(5, 5, 5, 5)

        dontAskAgainChkBox = QCheckBox('Don\'t ask again')
        dontAskAgainChkBox.stateChanged.connect(self.__dontAskAgainChkBoxChanged)
        dontAskAgainChkBox.setChecked(self.__dont_ask_again)

        okBtn = QPushButton('OK')
        closeBtn = QPushButton('Close')

        okBtn.clicked.connect(self.accept)
        closeBtn.clicked.connect(self.close)

        lay = QHBoxLayout()
        lay.addWidget(dontAskAgainChkBox)
        lay.addSpacerItem(QSpacerItem(10, 10, QSizePolicy.MinimumExpanding))
        lay.addWidget(okBtn)
        lay.addWidget(closeBtn)
        lay.setContentsMargins(0, 0, 0, 0)

        bottomWidget = QWidget()
        bottomWidget.setLayout(lay)

        lay = QVBoxLayout()

        lay.addWidget(self.__messageLbl)
        lay.addWidget(bottomWidget)

        self.setLayout(lay)

    def __dontAskAgainChkBoxChanged(self, state):
        self.__settings_ini.setValue('dont_ask_again', state == 2)

    def isAskAgainEnabled(self):
        return self.__settings_ini.value('dont_ask_again', type=bool)

    def setMessage(self, message):
        self.__messageLbl.setText(message)