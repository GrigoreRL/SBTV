# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Grigore\UIs\MirrorSetup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MirrorSetup(object):
    def setupUi(self, MirrorSetup):
        MirrorSetup.setObjectName("MirrorSetup")
        MirrorSetup.resize(1291, 805)
        self.centralwidget = QtWidgets.QWidget(MirrorSetup)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.ChargeLabel = QtWidgets.QLabel(self.centralwidget)
        self.ChargeLabel.setObjectName("ChargeLabel")
        self.gridLayout.addWidget(self.ChargeLabel, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_6.addWidget(self.label_11, 0, 0, 1, 1)
        self.FrequencyBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.FrequencyBox.setMinimum(1)
        self.FrequencyBox.setMaximum(250)
        self.FrequencyBox.setObjectName("FrequencyBox")
        self.gridLayout_6.addWidget(self.FrequencyBox, 0, 1, 1, 1)
        self.DisplayParticlesBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.DisplayParticlesBox.setEnabled(False)
        self.DisplayParticlesBox.setMinimum(1)
        self.DisplayParticlesBox.setMaximum(10000)
        self.DisplayParticlesBox.setObjectName("DisplayParticlesBox")
        self.gridLayout_6.addWidget(self.DisplayParticlesBox, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setEnabled(False)
        self.label_12.setObjectName("label_12")
        self.gridLayout_6.addWidget(self.label_12, 1, 0, 1, 1)
        self.DisplayParticlesBox.raise_()
        self.label_11.raise_()
        self.FrequencyBox.raise_()
        self.label_12.raise_()
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 2, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_13.addWidget(self.label_9)
        self.gridLayout.addWidget(self.groupBox_4, 0, 2, 2, 1)
        self.ChargesEntry = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ChargesEntry.setObjectName("ChargesEntry")
        self.gridLayout.addWidget(self.ChargesEntry, 1, 0, 1, 1)
        self.MassLabel = QtWidgets.QLabel(self.centralwidget)
        self.MassLabel.setObjectName("MassLabel")
        self.gridLayout.addWidget(self.MassLabel, 2, 0, 1, 1)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_9 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 719, 246))
        self.scrollAreaWidgetContents_9.setObjectName("scrollAreaWidgetContents_9")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_9)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.TwoDButton = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_9)
        self.TwoDButton.setObjectName("TwoDButton")
        self.gridLayout_7.addWidget(self.TwoDButton, 1, 0, 1, 1)
        self.ThreeDButton = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_9)
        self.ThreeDButton.setChecked(True)
        self.ThreeDButton.setObjectName("ThreeDButton")
        self.gridLayout_7.addWidget(self.ThreeDButton, 2, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_9)
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_14 = QtWidgets.QLabel(self.groupBox_7)
        self.label_14.setGeometry(QtCore.QRect(10, 20, 51, 16))
        self.label_14.setObjectName("label_14")
        self.FullTrajectoryButton = QtWidgets.QCheckBox(self.groupBox_7)
        self.FullTrajectoryButton.setGeometry(QtCore.QRect(10, 70, 92, 17))
        self.FullTrajectoryButton.setChecked(True)
        self.FullTrajectoryButton.setObjectName("FullTrajectoryButton")
        self.FigureSizeBox = QtWidgets.QLineEdit(self.groupBox_7)
        self.FigureSizeBox.setGeometry(QtCore.QRect(10, 40, 113, 20))
        self.FigureSizeBox.setObjectName("FigureSizeBox")
        self.GridBox = QtWidgets.QCheckBox(self.groupBox_7)
        self.GridBox.setGeometry(QtCore.QRect(10, 90, 91, 17))
        self.GridBox.setChecked(True)
        self.GridBox.setObjectName("GridBox")
        self.IntervalBox = QtWidgets.QSpinBox(self.groupBox_7)
        self.IntervalBox.setGeometry(QtCore.QRect(10, 110, 42, 22))
        self.IntervalBox.setMinimum(1)
        self.IntervalBox.setMaximum(100)
        self.IntervalBox.setObjectName("IntervalBox")
        self.gridLayout_7.addWidget(self.groupBox_7, 0, 1, 1, 1)
        self.TwoDOptionsBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_9)
        self.TwoDOptionsBox_3.setObjectName("TwoDOptionsBox_3")
        self.CoordinateButton = QtWidgets.QRadioButton(self.TwoDOptionsBox_3)
        self.CoordinateButton.setEnabled(False)
        self.CoordinateButton.setGeometry(QtCore.QRect(60, 20, 111, 17))
        self.CoordinateButton.setObjectName("CoordinateButton")
        self.TwoDOptionGroup = QtWidgets.QButtonGroup(MirrorSetup)
        self.TwoDOptionGroup.setObjectName("TwoDOptionGroup")
        self.TwoDOptionGroup.addButton(self.CoordinateButton)
        self.layoutWidget_4 = QtWidgets.QWidget(self.TwoDOptionsBox_3)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 20, 41, 65))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.XYCheckBox = QtWidgets.QCheckBox(self.layoutWidget_4)
        self.XYCheckBox.setEnabled(False)
        self.XYCheckBox.setObjectName("XYCheckBox")
        self.verticalLayout_3.addWidget(self.XYCheckBox)
        self.XZCheckBox = QtWidgets.QCheckBox(self.layoutWidget_4)
        self.XZCheckBox.setEnabled(False)
        self.XZCheckBox.setObjectName("XZCheckBox")
        self.verticalLayout_3.addWidget(self.XZCheckBox)
        self.YZCheckBox = QtWidgets.QCheckBox(self.layoutWidget_4)
        self.YZCheckBox.setEnabled(False)
        self.YZCheckBox.setObjectName("YZCheckBox")
        self.verticalLayout_3.addWidget(self.YZCheckBox)
        self.layoutWidget_5 = QtWidgets.QWidget(self.TwoDOptionsBox_3)
        self.layoutWidget_5.setGeometry(QtCore.QRect(10, 140, 101, 19))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.CheckBoxX = QtWidgets.QCheckBox(self.layoutWidget_5)
        self.CheckBoxX.setEnabled(False)
        self.CheckBoxX.setObjectName("CheckBoxX")
        self.horizontalLayout_5.addWidget(self.CheckBoxX)
        self.CheckBoxY = QtWidgets.QCheckBox(self.layoutWidget_5)
        self.CheckBoxY.setEnabled(False)
        self.CheckBoxY.setObjectName("CheckBoxY")
        self.horizontalLayout_5.addWidget(self.CheckBoxY)
        self.CheckBoxZ = QtWidgets.QCheckBox(self.layoutWidget_5)
        self.CheckBoxZ.setEnabled(False)
        self.CheckBoxZ.setObjectName("CheckBoxZ")
        self.horizontalLayout_5.addWidget(self.CheckBoxZ)
        self.layoutWidget_6 = QtWidgets.QWidget(self.TwoDOptionsBox_3)
        self.layoutWidget_6.setGeometry(QtCore.QRect(110, 100, 86, 65))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.CoordinatevtButton = QtWidgets.QRadioButton(self.layoutWidget_6)
        self.CoordinatevtButton.setEnabled(False)
        self.CoordinatevtButton.setObjectName("CoordinatevtButton")
        self.TwoDOptionGroup.addButton(self.CoordinatevtButton)
        self.verticalLayout_4.addWidget(self.CoordinatevtButton)
        self.VelocityvtButton = QtWidgets.QRadioButton(self.layoutWidget_6)
        self.VelocityvtButton.setEnabled(False)
        self.VelocityvtButton.setObjectName("VelocityvtButton")
        self.TwoDOptionGroup.addButton(self.VelocityvtButton)
        self.verticalLayout_4.addWidget(self.VelocityvtButton)
        self.PhaseButton = QtWidgets.QRadioButton(self.layoutWidget_6)
        self.PhaseButton.setEnabled(False)
        self.PhaseButton.setObjectName("PhaseButton")
        self.TwoDOptionGroup.addButton(self.PhaseButton)
        self.verticalLayout_4.addWidget(self.PhaseButton)
        self.gridLayout_7.addWidget(self.TwoDOptionsBox_3, 0, 0, 1, 1)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_9)
        self.gridLayout.addWidget(self.scrollArea_3, 2, 1, 5, 2)
        self.MassesEntry = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.MassesEntry.setObjectName("MassesEntry")
        self.gridLayout.addWidget(self.MassesEntry, 3, 0, 1, 1)
        self.PosLabel = QtWidgets.QLabel(self.centralwidget)
        self.PosLabel.setObjectName("PosLabel")
        self.gridLayout.addWidget(self.PosLabel, 4, 0, 1, 1)
        self.PositionEntry = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.PositionEntry.setObjectName("PositionEntry")
        self.gridLayout.addWidget(self.PositionEntry, 5, 0, 1, 1)
        self.VelLabel = QtWidgets.QLabel(self.centralwidget)
        self.VelLabel.setObjectName("VelLabel")
        self.gridLayout.addWidget(self.VelLabel, 6, 0, 1, 1)
        self.VelocityEntry = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.VelocityEntry.setObjectName("VelocityEntry")
        self.gridLayout.addWidget(self.VelocityEntry, 7, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_12.addWidget(self.label_5)
        self.ComputeButton = QtWidgets.QPushButton(self.groupBox_5)
        self.ComputeButton.setObjectName("ComputeButton")
        self.verticalLayout_12.addWidget(self.ComputeButton)
        self.AnimateButton = QtWidgets.QPushButton(self.groupBox_5)
        self.AnimateButton.setObjectName("AnimateButton")
        self.verticalLayout_12.addWidget(self.AnimateButton)
        self.gridLayout.addWidget(self.groupBox_5, 7, 1, 1, 1)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 544, 90))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.UserInfoLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        self.UserInfoLabel.setObjectName("UserInfoLabel")
        self.verticalLayout_11.addWidget(self.UserInfoLabel)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_7)
        self.gridLayout.addWidget(self.scrollArea_2, 7, 2, 1, 1)
        self.EFieldLabel = QtWidgets.QLabel(self.centralwidget)
        self.EFieldLabel.setObjectName("EFieldLabel")
        self.gridLayout.addWidget(self.EFieldLabel, 8, 0, 1, 1)
        self.EFieldEntry = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.EFieldEntry.setObjectName("EFieldEntry")
        self.gridLayout.addWidget(self.EFieldEntry, 9, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 719, 256))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_4.addWidget(self.label_13)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_8)
        self.gridLayout.addWidget(self.scrollArea, 9, 1, 3, 2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tfLabel_3 = QtWidgets.QLabel(self.groupBox_3)
        self.tfLabel_3.setObjectName("tfLabel_3")
        self.gridLayout_5.addWidget(self.tfLabel_3, 1, 1, 1, 1)
        self.TimeStepLabel = QtWidgets.QLabel(self.groupBox_3)
        self.TimeStepLabel.setObjectName("TimeStepLabel")
        self.gridLayout_5.addWidget(self.TimeStepLabel, 1, 0, 1, 1)
        self.dtEntry = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.dtEntry.setObjectName("dtEntry")
        self.gridLayout_5.addWidget(self.dtEntry, 2, 0, 1, 1)
        self.tfEntry = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.tfEntry.setObjectName("tfEntry")
        self.gridLayout_5.addWidget(self.tfEntry, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 10, 0, 1, 1)
        self.SetAllButton = QtWidgets.QPushButton(self.centralwidget)
        self.SetAllButton.setObjectName("SetAllButton")
        self.gridLayout.addWidget(self.SetAllButton, 11, 0, 1, 1)
        MirrorSetup.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MirrorSetup)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1291, 21))
        self.menubar.setObjectName("menubar")
        MirrorSetup.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MirrorSetup)
        self.statusbar.setObjectName("statusbar")
        MirrorSetup.setStatusBar(self.statusbar)

        self.retranslateUi(MirrorSetup)
        QtCore.QMetaObject.connectSlotsByName(MirrorSetup)

    def retranslateUi(self, MirrorSetup):
        _translate = QtCore.QCoreApplication.translate
        MirrorSetup.setWindowTitle(_translate("MirrorSetup", "Magnetic Mirror Setup Window"))
        self.ChargeLabel.setText(_translate("MirrorSetup", "Charge - input a value in C in the format \"Value1 Value2 etc.\""))
        self.groupBox_2.setTitle(_translate("MirrorSetup", "Output options"))
        self.label_11.setText(_translate("MirrorSetup", "<html><head/><body><p align=\"center\">Output Frequency</p><p align=\"center\">Steps</p></body></html>"))
        self.FrequencyBox.setToolTip(_translate("MirrorSetup", "<html><head/><body><p>Input a positive integer!</p></body></html>"))
        self.label_12.setText(_translate("MirrorSetup", "Particles to show"))
        self.groupBox_4.setTitle(_translate("MirrorSetup", "Important"))
        self.label_9.setText(_translate("MirrorSetup", "<html><head/><body><p>Try not to exceed 1e8 time steps.</p><p>All inputs <span style=\" font-weight:600; font-style:italic; text-decoration: underline;\">must</span>  be in scientific notation. Don\'t forget to add .0 to integers, i.e. 1.0.</p></body></html>"))
        self.ChargesEntry.setPlainText(_translate("MirrorSetup", "1.0"))
        self.MassLabel.setText(_translate("MirrorSetup", "Mass - input a value in Kg in the format \"Value1 Value2 etc.\""))
        self.TwoDButton.setToolTip(_translate("MirrorSetup", "<html><head/><body><p>Select whether you want to see 2D or 3D plots</p></body></html>"))
        self.TwoDButton.setText(_translate("MirrorSetup", "2D"))
        self.ThreeDButton.setToolTip(_translate("MirrorSetup", "<html><head/><body><p>Select whether you want to see 2D or 3D plots</p></body></html>"))
        self.ThreeDButton.setText(_translate("MirrorSetup", "3D"))
        self.groupBox_7.setTitle(_translate("MirrorSetup", "Figure Options"))
        self.label_14.setText(_translate("MirrorSetup", "Figure size"))
        self.FullTrajectoryButton.setText(_translate("MirrorSetup", "Full Trajectory"))
        self.FigureSizeBox.setText(_translate("MirrorSetup", "10 7.5"))
        self.GridBox.setText(_translate("MirrorSetup", "Grid on figures"))
        self.TwoDOptionsBox_3.setToolTip(_translate("MirrorSetup", "<html><head/><body><p>Select which coordinate pairs you want displayed. Select at least one option.</p></body></html>"))
        self.TwoDOptionsBox_3.setTitle(_translate("MirrorSetup", "2D Options"))
        self.CoordinateButton.setToolTip(_translate("MirrorSetup", "<html><head/><body><p>Select whether you want to see coordinate space of phase space plots</p></body></html>"))
        self.CoordinateButton.setText(_translate("MirrorSetup", "Coordinate Space"))
        self.XYCheckBox.setToolTip(_translate("MirrorSetup", "<html><head/><body><p>Select which coordinate pairs you want displayed. Select at least one option.</p></body></html>"))
        self.XYCheckBox.setText(_translate("MirrorSetup", "X-Y"))
        self.XZCheckBox.setToolTip(_translate("MirrorSetup", "<html><head/><body><p>Select which coordinate pairs you want displayed. Select at least one option.</p></body></html>"))
        self.XZCheckBox.setText(_translate("MirrorSetup", "X-Z"))
        self.YZCheckBox.setToolTip(_translate("MirrorSetup", "<html><head/><body><p>Select which coordinate pairs you want displayed. Select at least one option.</p></body></html>"))
        self.YZCheckBox.setText(_translate("MirrorSetup", "Y-Z"))
        self.CheckBoxX.setText(_translate("MirrorSetup", "X"))
        self.CheckBoxY.setText(_translate("MirrorSetup", "Y"))
        self.CheckBoxZ.setText(_translate("MirrorSetup", "Z"))
        self.CoordinatevtButton.setText(_translate("MirrorSetup", "Coordinate-t"))
        self.VelocityvtButton.setText(_translate("MirrorSetup", "Velocities-t"))
        self.PhaseButton.setToolTip(_translate("MirrorSetup", "<html><head/><body><p>Select whether you want to see coordinate space of phase space plots</p></body></html>"))
        self.PhaseButton.setText(_translate("MirrorSetup", "Phase Space"))
        self.MassesEntry.setPlainText(_translate("MirrorSetup", "1.0"))
        self.PosLabel.setText(_translate("MirrorSetup", "Initial positions"))
        self.PositionEntry.setToolTip(_translate("MirrorSetup", "<html><head/><body><p>Remember not to add a semi-colon (;) after the last set of co-ordinates!</p></body></html>"))
        self.PositionEntry.setWhatsThis(_translate("MirrorSetup", "<html><head/><body><p>Cat</p></body></html>"))
        self.PositionEntry.setPlainText(_translate("MirrorSetup", "0.95e4 0.0 0.0"))
        self.VelLabel.setText(_translate("MirrorSetup", "Initial velocities"))
        self.VelocityEntry.setToolTip(_translate("MirrorSetup", "<html><head/><body><p>Remember not to add a semi-colon (;) after the last set of co-ordinates!</p></body></html>"))
        self.VelocityEntry.setPlainText(_translate("MirrorSetup", "0.0 5e4 1e4"))
        self.label_5.setText(_translate("MirrorSetup", "<html><head/><body><p align=\"center\">Click to compute/display</p></body></html>"))
        self.ComputeButton.setToolTip(_translate("MirrorSetup", "<html><head/><body><p>Computes the trajectory but <span style=\" font-style:italic; text-decoration: underline;\">does not</span> display it. You need to press the Plot/Animate button to display the plots.</p></body></html>"))
        self.ComputeButton.setText(_translate("MirrorSetup", "Compute Trajectory"))
        self.AnimateButton.setText(_translate("MirrorSetup", "Plot/Animate"))
        self.UserInfoLabel.setText(_translate("MirrorSetup", "<html><head/><body><p>Status window.</p></body></html>"))
        self.EFieldLabel.setText(_translate("MirrorSetup", "<html><head/><body><p>Magnetic field reference strength and mirror scale length</p></body></html>"))
        self.EFieldEntry.setToolTip(_translate("MirrorSetup", "<html><head/><body><p>Remember not to add any semi-colons and to use only one set of values; this is a uniform field!</p></body></html>"))
        self.EFieldEntry.setPlainText(_translate("MirrorSetup", "1e3 1e4"))
        self.label_13.setText(_translate("MirrorSetup", "<html><head/><body><p>Welcome to the magnetic mirror/bottle simulation.</p><p>This simulation is mostly experimental, but is meant to show the trapping effect of a magnetic bottle. </p><p>Try playing around with the velocities and bottle parameters, but remember to keep the particle outisde of the associated loss cone.</p></body></html>"))
        self.tfLabel_3.setText(_translate("MirrorSetup", "Final time"))
        self.TimeStepLabel.setText(_translate("MirrorSetup", "Time-step (s)"))
        self.dtEntry.setPlainText(_translate("MirrorSetup", "1e-6"))
        self.tfEntry.setPlainText(_translate("MirrorSetup", "2.5e-0"))
        self.SetAllButton.setText(_translate("MirrorSetup", "Set All"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MirrorSetup = QtWidgets.QMainWindow()
    ui = Ui_MirrorSetup()
    ui.setupUi(MirrorSetup)
    MirrorSetup.show()
    sys.exit(app.exec_())

