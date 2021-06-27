# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Grigore\UIs\ErrorDialogWithCustomText.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ErrorNotification(object):
    def setupUi(self, ErrorNotification):
        ErrorNotification.setObjectName("ErrorNotification")
        ErrorNotification.resize(362, 129)
        ErrorNotification.setMaximumSize(QtCore.QSize(400, 150))
        self.splitter = QtWidgets.QSplitter(ErrorNotification)
        self.splitter.setGeometry(QtCore.QRect(0, 10, 364, 111))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.splitter)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(ErrorNotification)
        QtCore.QMetaObject.connectSlotsByName(ErrorNotification)

    def retranslateUi(self, ErrorNotification):
        _translate = QtCore.QCoreApplication.translate
        ErrorNotification.setWindowTitle(_translate("ErrorNotification", "Error"))
        ErrorNotification.setWhatsThis(_translate("ErrorNotification", "<html><head/><body><p>Help Text</p></body></html>"))
        self.label.setText(_translate("ErrorNotification", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">sdgfsdh</span></p></body></html>"))
        self.pushButton.setText(_translate("ErrorNotification", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ErrorNotification = QtWidgets.QDialog()
    ui = Ui_ErrorNotification()
    ui.setupUi(ErrorNotification)
    ErrorNotification.show()
    sys.exit(app.exec_())

