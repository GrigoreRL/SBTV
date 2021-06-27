# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Grigore\UIs\UsefulValuesEUniform.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EUniformUsefulValuesWindow(object):
    def setupUi(self, EUniformUsefulValuesWindow):
        EUniformUsefulValuesWindow.setObjectName("EUniformUsefulValuesWindow")
        EUniformUsefulValuesWindow.resize(400, 300)
        self.ValuesLabel = QtWidgets.QLabel(EUniformUsefulValuesWindow)
        self.ValuesLabel.setGeometry(QtCore.QRect(10, 20, 371, 261))
        self.ValuesLabel.setObjectName("ValuesLabel")

        self.retranslateUi(EUniformUsefulValuesWindow)
        QtCore.QMetaObject.connectSlotsByName(EUniformUsefulValuesWindow)

    def retranslateUi(self, EUniformUsefulValuesWindow):
        _translate = QtCore.QCoreApplication.translate
        EUniformUsefulValuesWindow.setWindowTitle(_translate("EUniformUsefulValuesWindow", "Dialog"))
        self.ValuesLabel.setText(_translate("EUniformUsefulValuesWindow", "<html><head/><body><p align=\"center\">Electron Charge = -1.602e-19 C</p><p align=\"center\"><br/></p><p align=\"center\">Electron Mass = 9.11e-31 Kg</p><p align=\"center\"><br/></p><p align=\"center\">Proton Charge = 1.602e-19 C</p><p align=\"center\"><br/></p><p align=\"center\">Proton Mass = 1.673e-27 Kg</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EUniformUsefulValuesWindow = QtWidgets.QDialog()
    ui = Ui_EUniformUsefulValuesWindow()
    ui.setupUi(EUniformUsefulValuesWindow)
    EUniformUsefulValuesWindow.show()
    sys.exit(app.exec_())

