import sys
import importlib.util
import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import QtCore,QtGui,uic,QtWidgets
from MainMenu import Ui_MainMenu
from EFieldSetup import Ui_UniformElectricSetup
from AnimationPlayerWindow import Ui_PlayerWindow,Ui_PlayerWindow2D
from UsefulValuesEUniform import Ui_EUniformUsefulValuesWindow
from BFieldSetup import Ui_BFieldSetup
from CustomErrorDialog import Ui_ErrorNotification
from SBPP import *
from DipoleSetup import Ui_DipoleSetupWindow
from DriftSetup import Ui_DriftSetupWindow
from NullSetup import Ui_NullSetupWindow
from MirrorSetup import Ui_MirrorSetup
from UserFieldSetup import Ui_UserFieldSetup
from ElectromagnetSetup import Ui_ElectromagnetSetup
from GradientDriftCartesianSetup import Ui_CartesianDriftSetup
from RadialGradientSetup import Ui_RadialGradientSetup
import pandas as pd
import io
import os

class EUniformValues(QtWidgets.QDialog):
    def __init__(self):
        super(EUniformValues,self).__init__()
        self.ui = Ui_EUniformUsefulValuesWindow()
        self.ui.setupUi(self)
class CustomError(QtWidgets.QDialog):
    def __init__(self,message):
        super(CustomError,self).__init__()
        self.ui = Ui_ErrorNotification()
        self.ui.setupUi(self)
        self.ui.label.setText("{}".format(message))
        self.ui.pushButton.clicked.connect(self.accept)
class AnimationPlayerWindow(QtWidgets.QDialog):
    def __init__(self,qs,dqs,ts=None):
        super(AnimationPlayerWindow,self).__init__()
        self.ui = Ui_PlayerWindow()
        #self.ui.setupUi(self)
        self.ui.__init__()
        self.ui.set_data(qs,dqs,ts)
        
class MainMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainMenu,self).__init__()
        self.ui=Ui_MainMenu()
        self.ui.setupUi(self)
        self.ui.DebugPush.clicked.connect(self.on_Debug_Push)
        self.ui.SetupLauncher.clicked.connect(self.on_Launch_Push)
    def throw_error(self,message):
        self.ErrorWindow = CustomError(message)
        self.ErrorWindow.show()
    def on_Debug_Push(self):
        print("Clicked Debug")
        #print(self.ui.SimSelectionMenu.currentItem())
        #print(self.ui.SimSelectionMenu.children())
        print((self.ui.SimSelectionMenu.selectedItems()[0]).text(0))
        #self.open_NullSetup()
        #self.open_UniformESetup()
        self.open_UserFieldSetup()
        return 0
    def on_Launch_Push(self):
        try:
            SelectedSimulation = (self.ui.SimSelectionMenu.selectedItems()[0]).text(0)
        except:
            error_message = "You need to select a simulation."
            self.throw_error(error_message)
        try:
            if SelectedSimulation == "Uniform Fields" or SelectedSimulation == "Non-Uniform Fields":
                error_message = "You need to select a specific simulation; use the drop-down menu."
                self.throw_error(error_message)
            else:
                if SelectedSimulation == "Pure Electric":
                    self.open_UniformESetup()
                elif SelectedSimulation == "Pure Magnetic":
                    print("Called")
                    self.open_UniformBSetup()
                elif SelectedSimulation == 'Drift Motion':
                    self.open_DriftSetup()
                elif SelectedSimulation == 'Magnetic Null':
                    self.open_NullSetup()
                elif SelectedSimulation == 'Magnetic Dipole':
                    self.open_DipoleSetup()
                elif SelectedSimulation == 'Magnetic Mirror':
                    self.open_MagneticMirrorSetup()
                elif SelectedSimulation == 'Electromagnet':
                    self.open_ElectromagnetSetup()
                elif SelectedSimulation == 'User-defined field':
                    self.open_UserFieldSetup()
                elif SelectedSimulation == 'Radial gradient drift':
                    self.open_RadialGradientSetup()
                elif SelectedSimulation == 'Linear gradient drift':
                    self.open_CartesianGradientSetup()
        except:
            error_message = "Something went wrong"
            self.throw_error(error_message)
    def open_NullSetup(self):
        self.NullSetup = NullSetupWindow()
        self.NullSetup.show()
    def open_DriftSetup(self):
        self.DriftSetup = DriftSetupWindow()
        self.DriftSetup.show()
    def open_DipoleSetup(self):
        self.DipoleSetup = DipoleSetupWindow()
        self.DipoleSetup.show()
    def open_UniformESetup(self):
        self.UniformESetup = EFieldSetupWindow()
        self.UniformESetup.show()
    def open_UniformBSetup(self):
        print("Called")
        self.UniformBSetup = BFieldSetupWindow()
        self.UniformBSetup.show()
    def open_MagneticMirrorSetup(self):
        self.MagneticMirrorSetup = MirrorSetupWindow()
        self.MagneticMirrorSetup.show()
    def open_UserFieldSetup(self):
        self.UserFieldSetup = UserFieldSetupWindow()
        self.UserFieldSetup.show()
    def open_ElectromagnetSetup(self):
        self.ElectromagnetSetup = ElectromagnetSetupWindow()
        self.ElectromagnetSetup.show()
    def open_RadialGradientSetup(self):
        self.RadialGradientSetup = RadialGradientSetupWindow()
        self.RadialGradientSetup.show()
    def open_CartesianGradientSetup(self):
        self.CartesianGradientSetup = CartesianGradientSetupWindow()
        self.CartesianGradientSetup.show()
class CartesianGradientSetupWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(CartesianGradientSetupWindow,self).__init__()
        self.ui = Ui_CartesianDriftSetup()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.ui.SetAllButton.clicked.connect(self.set_all)
        self.ui.TwoDButton.clicked.connect(self.enable_2D_options)
        self.ui.ThreeDButton.clicked.connect(self.disable_2D_options)
        self.ui.CoordinatevtButton.clicked.connect(self.enable_vt_options)
        self.ui.PhaseButton.clicked.connect(self.enable_vt_options)
        self.ui.VelocityvtButton.clicked.connect(self.enable_vt_options)
        self.ui.CoordinateButton.clicked.connect(self.enable_cvc_options)
        self.ui.ComputeButton.clicked.connect(self.ComputeTrajectories)
        self.ui.AnimateButton.clicked.connect(self.LaunchPlayer)
    def enable_cvc_options(self):
        self.ui.XYCheckBox.setEnabled(True)
        self.ui.XZCheckBox.setEnabled(True)
        self.ui.YZCheckBox.setEnabled(True)
        self.disable_vt_options()
    def disable_cvc_options(self):
        self.ui.XYCheckBox.setEnabled(False)
        self.ui.XZCheckBox.setEnabled(False)
        self.ui.YZCheckBox.setEnabled(False)
        self.ui.XYCheckBox.setChecked(False)
        self.ui.XZCheckBox.setChecked(False)
        self.ui.YZCheckBox.setChecked(False)
    def enable_vt_options(self):
        self.ui.CheckBoxX.setEnabled(True)
        self.ui.CheckBoxY.setEnabled(True)
        self.ui.CheckBoxZ.setEnabled(True)
        self.disable_cvc_options()
    def disable_vt_options(self):
        self.ui.CheckBoxX.setEnabled(False)
        self.ui.CheckBoxY.setEnabled(False)
        self.ui.CheckBoxZ.setEnabled(False)
        self.ui.CheckBoxX.setChecked(False)
        self.ui.CheckBoxY.setChecked(False)
        self.ui.CheckBoxZ.setChecked(False)
    def disable_2D_options(self):
        self.ui.TwoDOptionGroup.setExclusive(False)
        self.ui.CoordinateButton.setEnabled(False)
        self.ui.CoordinateButton.setChecked(False)
        self.ui.CoordinatevtButton.setEnabled(False)
        self.ui.CoordinatevtButton.setChecked(False)
        self.ui.PhaseButton.setEnabled(False)
        self.ui.PhaseButton.setChecked(False)
        self.ui.VelocityvtButton.setChecked(False)
        self.ui.VelocityvtButton.setEnabled(False)
        self.disable_cvc_options()
        self.disable_vt_options()
        self.ui.TwoDOptionGroup.setExclusive(True)
    def enable_2D_options(self):
        self.ui.CoordinateButton.setEnabled(True)
        self.ui.CoordinatevtButton.setEnabled(True)
        self.ui.PhaseButton.setEnabled(True)
        self.ui.VelocityvtButton.setEnabled(True)
    def throw_error(self,message):
        self.ErrorWindow = CustomError(message)
        self.ErrorWindow.show()
    def ComputeTrajectories(self):
        self.set_all()
        try:
            time1 = time.time()
            self.qs,self.dqs,self.ts = SBPP.Integrator_Synched_nonRel(self.q0s,self.dq0s,E_func_zero,B_func_linear_grad,
        self.masses,self.charges,self.dt,self.tf,self.fparams,output_Freq = 1)
            time2 = time.time()
            self.write_to_user("Completed computation; it took {:e} seconds".format(time2-time1))
            self.qs = np.array(self.qs)
            self.dqs = np.array(self.dqs)
        except:
            self.throw_error("Computation failed; check input quantities!")
        

    def LaunchPlayer(self):
        self.set_frequency()
        if self.ui.ThreeDButton.isChecked():
            self.PlayerWindow = Ui_PlayerWindow(figsize=self.figsize)
            self.PlayerWindow.set_data(self.qs,self.dqs,frequency = self.frequency,ts = self.ts)
            self.PlayerWindow.set_options(plot_traj = self.ui.FullTrajectoryButton.isChecked())
            self.PlayerWindow.show()
        elif self.ui.CoordinatevtButton.isChecked():
            if self.ui.CheckBoxX.isChecked():
                self.PlayerWindowXvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvt.set_data(self.qs[:,:,0],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvt.set_options(axis_labels=('t[s]','x[m]'))
                self.PlayerWindowXvt.show()
            if self.ui.CheckBoxY.isChecked():
                self.PlayerWindowYvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowYvt.set_data(self.qs[:,:,1],self.ts,ts=self.ts,frequency=self.frequency)
                self.PlayerWindowYvt.set_options(axis_labels=('t[s]','y[m]'))
                self.PlayerWindowYvt.show()
            if self.ui.CheckBoxZ.isChecked():
                self.PlayerWindowZvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowZvt.set_data(self.qs[:,:,2],self.ts,ts=self.ts,frequency=self.frequency)
                self.PlayerWindowZvt.set_options(axis_labels=('t[s]','z[m]'))
                self.PlayerWindowZvt.show()
        elif self.ui.PhaseButton.isChecked():
            if self.ui.CheckBoxX.isChecked():
                self.PlayerWindowXvVx = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvVx.set_data(self.qs[:,:,0],self.dqs[:,:,0],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvVx.set_options(axis_labels=('x[m]','v$_x$[m/s]'))
                self.PlayerWindowXvVx.show()
            if self.ui.CheckBoxY.isChecked():
                self.PlayerWindowXvVy = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvVy.set_data(self.qs[:,:,1],self.dqs[:,:,1],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvVy.set_options(axis_labels=('y[m]','v$_y$[m/s]'))
                self.PlayerWindowXvVy.show()
            if self.ui.CheckBoxZ.isChecked():
                self.PlayerWindowXvVz = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvVz.set_data(self.qs[:,:,2],self.dqs[:,:,2],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvVz.set_options(axis_labels=('y[m]','v$_y$[m/s]'))
                self.PlayerWindowXvVz.show()
        elif self.ui.VelocityvtButton.isChecked():
            if self.ui.CheckBoxX.isChecked():
                self.PlayerWindowVxvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowVxvt.set_data(self.dqs[:,:,0],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowVxvt.set_options(axis_labels=('t[s]','v$_x$[m/s]'))
                self.PlayerWindowVxvt.show()
            if self.ui.CheckBoxY.isChecked():
                self.PlayerWindowVyvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowVyvt.set_data(self.dqs[:,:,1],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowVyvt.set_options(axis_labels=('t[s]','v$_y$[m/s]'))
                self.PlayerWindowVyvt.show()
            if self.ui.CheckBoxZ.isChecked():
                self.PlayerWindowVzvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowVzvt.set_data(self.dqs[:,:,2],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowVzvt.set_options(axis_labels=('t[s]','v$_z$[m/s]'))
                self.PlayerWindowVzvt.show()
        elif self.ui.CoordinateButton.isChecked():
            if self.ui.XYCheckBox.isChecked():
                self.PlayerWindowXvY = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvY.set_data(self.qs[:,:,0],self.qs[:,:,1],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvY.set_options(axis_labels=('x[m]','y[m]'))
                self.PlayerWindowXvY.show()
            if self.ui.XZCheckBox.isChecked():
                self.PlayerWindowXvZ = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvZ.set_data(self.qs[:,:,0],self.qs[:,:,2],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvZ.set_options(axis_labels=('x[m]','z[m]'))
                self.PlayerWindowXvZ.show()
            if self.ui.YZCheckBox.isChecked():
                self.PlayerWindowYvZ = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowYvZ.set_data(self.qs[:,:,1],self.qs[:,:,2],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowYvZ.set_options(axis_labels=('y[m]','z[y]'))
                self.PlayerWindowYvZ.show()
    def write_to_user(self,message):
        self.ui.UserInfoLabel.setText(message)
    def set_all(self):
        try:
            self.set_charges()
            self.set_masses()
            self.set_initial_positions()
            self.set_initial_velocities()
            self.set_dt()
            self.set_field_strengths()
            self.set_tf()
            self.set_frequency()
            self.set_figoptions()
            self.write_to_user("Set all values; ready to compute.")
        except:
            self.throw_error("Error in the format; please fix it and try again!")
    def set_figoptions(self):
        user_input = self.ui.FigureSizeBox.text()
        user_input = np.fromstring(user_input, sep = ' ')
        self.figsize = (user_input[0],user_input[1])
    def set_frequency(self):
        self.frequency = self.ui.FrequencyBox.value()
    def set_charges(self):
        user_input = self.ui.ChargesEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep=' ')
            self.charges = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(user_input)
    def set_masses(self):
        user_input = self.ui.MassesEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep = ' ')
            self.masses = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
    def set_initial_positions(self):
        user_input = self.ui.PositionEntry.toPlainText()
        try:
            user_input = np.array(np.matrix(user_input))
            self.q0s = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(user_input)
    def set_initial_velocities(self):
        user_input = self.ui.VelocityEntry.toPlainText()
        try:
            user_input = np.array(np.matrix(user_input))
            self.dq0s = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(user_input)
    def set_field_strengths(self):
        user_input = self.ui.EFieldEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep=' ')
            self.fparams = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(self.fparams)
    
    def set_dt(self):
        user_input = self.ui.dtEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep = ' ')
            self.dt = user_input[0]
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
    def set_tf(self):
        user_input = self.ui.tfEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep = ' ')
            self.tf = user_input[0]
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        
class RadialGradientSetupWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(RadialGradientSetupWindow,self).__init__()
        self.ui = Ui_RadialGradientSetup()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.ui.SetAllButton.clicked.connect(self.set_all)
        self.ui.TwoDButton.clicked.connect(self.enable_2D_options)
        self.ui.ThreeDButton.clicked.connect(self.disable_2D_options)
        self.ui.CoordinatevtButton.clicked.connect(self.enable_vt_options)
        self.ui.PhaseButton.clicked.connect(self.enable_vt_options)
        self.ui.VelocityvtButton.clicked.connect(self.enable_vt_options)
        self.ui.CoordinateButton.clicked.connect(self.enable_cvc_options)
        self.ui.ComputeButton.clicked.connect(self.ComputeTrajectories)
        self.ui.AnimateButton.clicked.connect(self.LaunchPlayer)
    def enable_cvc_options(self):
        self.ui.XYCheckBox.setEnabled(True)
        self.ui.XZCheckBox.setEnabled(True)
        self.ui.YZCheckBox.setEnabled(True)
        self.disable_vt_options()
    def disable_cvc_options(self):
        self.ui.XYCheckBox.setEnabled(False)
        self.ui.XZCheckBox.setEnabled(False)
        self.ui.YZCheckBox.setEnabled(False)
        self.ui.XYCheckBox.setChecked(False)
        self.ui.XZCheckBox.setChecked(False)
        self.ui.YZCheckBox.setChecked(False)
    def enable_vt_options(self):
        self.ui.CheckBoxX.setEnabled(True)
        self.ui.CheckBoxY.setEnabled(True)
        self.ui.CheckBoxZ.setEnabled(True)
        self.disable_cvc_options()
    def disable_vt_options(self):
        self.ui.CheckBoxX.setEnabled(False)
        self.ui.CheckBoxY.setEnabled(False)
        self.ui.CheckBoxZ.setEnabled(False)
        self.ui.CheckBoxX.setChecked(False)
        self.ui.CheckBoxY.setChecked(False)
        self.ui.CheckBoxZ.setChecked(False)
    def disable_2D_options(self):
        self.ui.TwoDOptionGroup.setExclusive(False)
        self.ui.CoordinateButton.setEnabled(False)
        self.ui.CoordinateButton.setChecked(False)
        self.ui.CoordinatevtButton.setEnabled(False)
        self.ui.CoordinatevtButton.setChecked(False)
        self.ui.PhaseButton.setEnabled(False)
        self.ui.PhaseButton.setChecked(False)
        self.ui.VelocityvtButton.setChecked(False)
        self.ui.VelocityvtButton.setEnabled(False)
        self.disable_cvc_options()
        self.disable_vt_options()
        self.ui.TwoDOptionGroup.setExclusive(True)
    def enable_2D_options(self):
        self.ui.CoordinateButton.setEnabled(True)
        self.ui.CoordinatevtButton.setEnabled(True)
        self.ui.PhaseButton.setEnabled(True)
        self.ui.VelocityvtButton.setEnabled(True)
    def throw_error(self,message):
        self.ErrorWindow = CustomError(message)
        self.ErrorWindow.show()
    def ComputeTrajectories(self):
        self.set_all()
        time1 = time.time()
        self.qs,self.dqs,self.ts = SBPP.Integrator_Synched_nonRel(self.q0s,self.dq0s,E_func_zero,B_func_rad_grad,
        self.masses,self.charges,self.dt,self.tf,self.fparams,output_Freq = 1)
        time2 = time.time()
        self.write_to_user("Completed computation; it took {:e} seconds".format(time2-time1))
        self.qs = np.array(self.qs)
        self.dqs = np.array(self.dqs)
    def LaunchPlayer(self):
        self.set_frequency()
        if self.ui.ThreeDButton.isChecked():
            self.PlayerWindow = Ui_PlayerWindow(figsize=self.figsize)
            self.PlayerWindow.set_data(self.qs,self.dqs,frequency = self.frequency,ts = self.ts)
            self.PlayerWindow.set_options(plot_traj = self.ui.FullTrajectoryButton.isChecked())
            self.PlayerWindow.show()
        elif self.ui.CoordinatevtButton.isChecked():
            if self.ui.CheckBoxX.isChecked():
                self.PlayerWindowXvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvt.set_data(self.qs[:,:,0],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvt.set_options(axis_labels=('t[s]','x[m]'))
                self.PlayerWindowXvt.show()
            if self.ui.CheckBoxY.isChecked():
                self.PlayerWindowYvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowYvt.set_data(self.qs[:,:,1],self.ts,ts=self.ts,frequency=self.frequency)
                self.PlayerWindowYvt.set_options(axis_labels=('t[s]','y[m]'))
                self.PlayerWindowYvt.show()
            if self.ui.CheckBoxZ.isChecked():
                self.PlayerWindowZvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowZvt.set_data(self.qs[:,:,2],self.ts,ts=self.ts,frequency=self.frequency)
                self.PlayerWindowZvt.set_options(axis_labels=('t[s]','z[m]'))
                self.PlayerWindowZvt.show()
        elif self.ui.PhaseButton.isChecked():
            if self.ui.CheckBoxX.isChecked():
                self.PlayerWindowXvVx = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvVx.set_data(self.qs[:,:,0],self.dqs[:,:,0],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvVx.set_options(axis_labels=('x[m]','v$_x$[m/s]'))
                self.PlayerWindowXvVx.show()
            if self.ui.CheckBoxY.isChecked():
                self.PlayerWindowXvVy = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvVy.set_data(self.qs[:,:,1],self.dqs[:,:,1],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvVy.set_options(axis_labels=('y[m]','v$_y$[m/s]'))
                self.PlayerWindowXvVy.show()
            if self.ui.CheckBoxZ.isChecked():
                self.PlayerWindowXvVz = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvVz.set_data(self.qs[:,:,2],self.dqs[:,:,2],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvVz.set_options(axis_labels=('y[m]','v$_y$[m/s]'))
                self.PlayerWindowXvVz.show()
        elif self.ui.VelocityvtButton.isChecked():
            if self.ui.CheckBoxX.isChecked():
                self.PlayerWindowVxvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowVxvt.set_data(self.dqs[:,:,0],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowVxvt.set_options(axis_labels=('t[s]','v$_x$[m/s]'))
                self.PlayerWindowVxvt.show()
            if self.ui.CheckBoxY.isChecked():
                self.PlayerWindowVyvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowVyvt.set_data(self.dqs[:,:,1],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowVyvt.set_options(axis_labels=('t[s]','v$_y$[m/s]'))
                self.PlayerWindowVyvt.show()
            if self.ui.CheckBoxZ.isChecked():
                self.PlayerWindowVzvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowVzvt.set_data(self.dqs[:,:,2],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowVzvt.set_options(axis_labels=('t[s]','v$_z$[m/s]'))
                self.PlayerWindowVzvt.show()
        elif self.ui.CoordinateButton.isChecked():
            if self.ui.XYCheckBox.isChecked():
                self.PlayerWindowXvY = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvY.set_data(self.qs[:,:,0],self.qs[:,:,1],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvY.set_options(axis_labels=('x[m]','y[m]'))
                self.PlayerWindowXvY.show()
            if self.ui.XZCheckBox.isChecked():
                self.PlayerWindowXvZ = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvZ.set_data(self.qs[:,:,0],self.qs[:,:,2],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvZ.set_options(axis_labels=('x[m]','z[m]'))
                self.PlayerWindowXvZ.show()
            if self.ui.YZCheckBox.isChecked():
                self.PlayerWindowYvZ = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowYvZ.set_data(self.qs[:,:,1],self.qs[:,:,2],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowYvZ.set_options(axis_labels=('y[m]','z[y]'))
                self.PlayerWindowYvZ.show()
    def write_to_user(self,message):
        self.ui.UserInfoLabel.setText(message)
    def set_all(self):
        self.set_charges()
        self.set_masses()
        self.set_initial_positions()
        self.set_initial_velocities()
        self.set_dt()
        self.set_field_strengths()
        self.set_tf()
        self.set_frequency()
        self.set_figoptions()
        self.write_to_user("Set all values; ready to compute.")
    def set_figoptions(self):
        user_input = self.ui.FigureSizeBox.text()
        user_input = np.fromstring(user_input, sep = ' ')
        self.figsize = (user_input[0],user_input[1])
    def set_frequency(self):
        self.frequency = self.ui.FrequencyBox.value()
    def set_charges(self):
        user_input = self.ui.ChargesEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep=' ')
            self.charges = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(user_input)
    def set_masses(self):
        user_input = self.ui.MassesEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep = ' ')
            self.masses = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
    def set_initial_positions(self):
        user_input = self.ui.PositionEntry.toPlainText()
        try:
            user_input = np.array(np.matrix(user_input))
            self.q0s = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(user_input)
    def set_initial_velocities(self):
        user_input = self.ui.VelocityEntry.toPlainText()
        try:
            user_input = np.array(np.matrix(user_input))
            self.dq0s = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(user_input)
    def set_field_strengths(self):
        user_input = self.ui.EFieldEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep=' ')
            self.fparams = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(self.fparams)
    
    def set_dt(self):
        user_input = self.ui.dtEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep = ' ')
            self.dt = user_input[0]
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
    def set_tf(self):
        user_input = self.ui.tfEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep = ' ')
            self.tf = user_input[0]
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        
class ElectromagnetSetupWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ElectromagnetSetupWindow,self).__init__()
        self.ui = Ui_ElectromagnetSetup()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.ui.SetAllButton.clicked.connect(self.set_all)
        self.ui.TwoDButton.clicked.connect(self.enable_2D_options)
        self.ui.ThreeDButton.clicked.connect(self.disable_2D_options)
        self.ui.CoordinatevtButton.clicked.connect(self.enable_vt_options)
        self.ui.PhaseButton.clicked.connect(self.enable_vt_options)
        self.ui.VelocityvtButton.clicked.connect(self.enable_vt_options)
        self.ui.CoordinateButton.clicked.connect(self.enable_cvc_options)
        self.ui.ComputeButton.clicked.connect(self.ComputeTrajectories)
        self.ui.AnimateButton.clicked.connect(self.LaunchPlayer)
    def enable_cvc_options(self):
        self.ui.XYCheckBox.setEnabled(True)
        self.ui.XZCheckBox.setEnabled(True)
        self.ui.YZCheckBox.setEnabled(True)
        self.disable_vt_options()
    def disable_cvc_options(self):
        self.ui.XYCheckBox.setEnabled(False)
        self.ui.XZCheckBox.setEnabled(False)
        self.ui.YZCheckBox.setEnabled(False)
        self.ui.XYCheckBox.setChecked(False)
        self.ui.XZCheckBox.setChecked(False)
        self.ui.YZCheckBox.setChecked(False)
    def enable_vt_options(self):
        self.ui.CheckBoxX.setEnabled(True)
        self.ui.CheckBoxY.setEnabled(True)
        self.ui.CheckBoxZ.setEnabled(True)
        self.disable_cvc_options()
    def disable_vt_options(self):
        self.ui.CheckBoxX.setEnabled(False)
        self.ui.CheckBoxY.setEnabled(False)
        self.ui.CheckBoxZ.setEnabled(False)
        self.ui.CheckBoxX.setChecked(False)
        self.ui.CheckBoxY.setChecked(False)
        self.ui.CheckBoxZ.setChecked(False)
    def disable_2D_options(self):
        self.ui.TwoDOptionGroup.setExclusive(False)
        self.ui.CoordinateButton.setEnabled(False)
        self.ui.CoordinateButton.setChecked(False)
        self.ui.CoordinatevtButton.setEnabled(False)
        self.ui.CoordinatevtButton.setChecked(False)
        self.ui.PhaseButton.setEnabled(False)
        self.ui.PhaseButton.setChecked(False)
        self.ui.VelocityvtButton.setChecked(False)
        self.ui.VelocityvtButton.setEnabled(False)
        self.disable_cvc_options()
        self.disable_vt_options()
        self.ui.TwoDOptionGroup.setExclusive(True)
    def enable_2D_options(self):
        self.ui.CoordinateButton.setEnabled(True)
        self.ui.CoordinatevtButton.setEnabled(True)
        self.ui.PhaseButton.setEnabled(True)
        self.ui.VelocityvtButton.setEnabled(True)
    def throw_error(self,message):
        self.ErrorWindow = CustomError(message)
        self.ErrorWindow.show()
    def ComputeTrajectories(self):
        self.set_all()
        time1 = time.time()
        self.qs,self.dqs,self.ts = SBPP.Integrator_Synched_nonRel(self.q0s,self.dq0s,E_func_zero,B_func_electromagnet,
        self.masses,self.charges,self.dt,self.tf,self.fparams,output_Freq = 1)
        time2 = time.time()
        self.write_to_user("Completed computation; it took {:e} seconds".format(time2-time1))
        self.qs = np.array(self.qs)
        self.dqs = np.array(self.dqs)
    def LaunchPlayer(self):
        self.set_frequency()
        if self.ui.ThreeDButton.isChecked():
            self.PlayerWindow = Ui_PlayerWindow(figsize=self.figsize)
            self.PlayerWindow.set_data(self.qs,self.dqs,frequency = self.frequency,ts = self.ts)
            self.PlayerWindow.set_options(plot_traj = self.ui.FullTrajectoryButton.isChecked())
            self.PlayerWindow.show()
        elif self.ui.CoordinatevtButton.isChecked():
            if self.ui.CheckBoxX.isChecked():
                self.PlayerWindowXvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvt.set_data(self.qs[:,:,0],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvt.set_options(axis_labels=('t[s]','x[m]'))
                self.PlayerWindowXvt.show()
            if self.ui.CheckBoxY.isChecked():
                self.PlayerWindowYvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowYvt.set_data(self.qs[:,:,1],self.ts,ts=self.ts,frequency=self.frequency)
                self.PlayerWindowYvt.set_options(axis_labels=('t[s]','y[m]'))
                self.PlayerWindowYvt.show()
            if self.ui.CheckBoxZ.isChecked():
                self.PlayerWindowZvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowZvt.set_data(self.qs[:,:,2],self.ts,ts=self.ts,frequency=self.frequency)
                self.PlayerWindowZvt.set_options(axis_labels=('t[s]','z[m]'))
                self.PlayerWindowZvt.show()
        elif self.ui.PhaseButton.isChecked():
            if self.ui.CheckBoxX.isChecked():
                self.PlayerWindowXvVx = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvVx.set_data(self.qs[:,:,0],self.dqs[:,:,0],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvVx.set_options(axis_labels=('x[m]','v$_x$[m/s]'))
                self.PlayerWindowXvVx.show()
            if self.ui.CheckBoxY.isChecked():
                self.PlayerWindowXvVy = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvVy.set_data(self.qs[:,:,1],self.dqs[:,:,1],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvVy.set_options(axis_labels=('y[m]','v$_y$[m/s]'))
                self.PlayerWindowXvVy.show()
            if self.ui.CheckBoxZ.isChecked():
                self.PlayerWindowXvVz = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvVz.set_data(self.qs[:,:,2],self.dqs[:,:,2],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvVz.set_options(axis_labels=('y[m]','v$_y$[m/s]'))
                self.PlayerWindowXvVz.show()
        elif self.ui.VelocityvtButton.isChecked():
            if self.ui.CheckBoxX.isChecked():
                self.PlayerWindowVxvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowVxvt.set_data(self.dqs[:,:,0],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowVxvt.set_options(axis_labels=('t[s]','v$_x$[m/s]'))
                self.PlayerWindowVxvt.show()
            if self.ui.CheckBoxY.isChecked():
                self.PlayerWindowVyvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowVyvt.set_data(self.dqs[:,:,1],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowVyvt.set_options(axis_labels=('t[s]','v$_y$[m/s]'))
                self.PlayerWindowVyvt.show()
            if self.ui.CheckBoxZ.isChecked():
                self.PlayerWindowVzvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowVzvt.set_data(self.dqs[:,:,2],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowVzvt.set_options(axis_labels=('t[s]','v$_z$[m/s]'))
                self.PlayerWindowVzvt.show()
        elif self.ui.CoordinateButton.isChecked():
            if self.ui.XYCheckBox.isChecked():
                self.PlayerWindowXvY = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvY.set_data(self.qs[:,:,0],self.qs[:,:,1],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvY.set_options(axis_labels=('x[m]','y[m]'))
                self.PlayerWindowXvY.show()
            if self.ui.XZCheckBox.isChecked():
                self.PlayerWindowXvZ = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvZ.set_data(self.qs[:,:,0],self.qs[:,:,2],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvZ.set_options(axis_labels=('x[m]','z[m]'))
                self.PlayerWindowXvZ.show()
            if self.ui.YZCheckBox.isChecked():
                self.PlayerWindowYvZ = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowYvZ.set_data(self.qs[:,:,1],self.qs[:,:,2],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowYvZ.set_options(axis_labels=('y[m]','z[y]'))
                self.PlayerWindowYvZ.show()
    def write_to_user(self,message):
        self.ui.UserInfoLabel.setText(message)
    def set_all(self):
        self.set_charges()
        self.set_masses()
        self.set_initial_positions()
        self.set_initial_velocities()
        self.set_dt()
        self.set_field_strengths()
        self.set_tf()
        self.set_frequency()
        self.set_figoptions()
        self.write_to_user("Set all values; ready to compute.")
    def set_figoptions(self):
        user_input = self.ui.FigureSizeBox.text()
        user_input = np.fromstring(user_input, sep = ' ')
        self.figsize = (user_input[0],user_input[1])
    def set_frequency(self):
        self.frequency = self.ui.FrequencyBox.value()
    def set_charges(self):
        user_input = self.ui.ChargesEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep=' ')
            self.charges = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(user_input)
    def set_masses(self):
        user_input = self.ui.MassesEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep = ' ')
            self.masses = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
    def set_initial_positions(self):
        user_input = self.ui.PositionEntry.toPlainText()
        try:
            user_input = np.array(np.matrix(user_input))
            self.q0s = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(user_input)
    def set_initial_velocities(self):
        user_input = self.ui.VelocityEntry.toPlainText()
        try:
            user_input = np.array(np.matrix(user_input))
            self.dq0s = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(user_input)
    def set_field_strengths(self):
        user_input = self.ui.EFieldEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep=' ')
            self.fparams = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(self.fparams)
    
    def set_dt(self):
        user_input = self.ui.dtEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep = ' ')
            self.dt = user_input[0]
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
    def set_tf(self):
        user_input = self.ui.tfEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep = ' ')
            self.tf = user_input[0]
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
class UserFieldSetupWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UserFieldSetupWindow,self).__init__()
        self.ui = Ui_UserFieldSetup()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.EField = E_func_zero
        self.BField = B_func_zero
        self.fparams = ()
        self.ui.BrowseButton.clicked.connect(self.browseFiles)
        self.ui.SetAllButton.clicked.connect(self.set_all)
        self.ui.TwoDButton.clicked.connect(self.enable_2D_options)
        self.ui.ThreeDButton.clicked.connect(self.disable_2D_options)
        self.ui.CoordinatevtButton.clicked.connect(self.enable_vt_options)
        self.ui.PhaseButton.clicked.connect(self.enable_vt_options)
        self.ui.VelocityvtButton.clicked.connect(self.enable_vt_options)
        self.ui.CoordinateButton.clicked.connect(self.enable_cvc_options)
        self.ui.ComputeButton.clicked.connect(self.ComputeTrajectories)
        self.ui.AnimateButton.clicked.connect(self.LaunchPlayer)
    def set_function(self):
        current_dir = os.getcwd()
        finished = False
        i = -1
        #try:
        while not finished:
            if self.filename[i] == '/':
                finished = True
                directory = self.filename[:i+1]
                fname = self.filename[i+1:-3]
                print(directory,fname)
                #spec = importlib.util.spec_from_file_location(fname,self.filename)
                #module = importlib.util.module_from_spec(spec)
                #spec.loader.exec_module(module)
                #print(dir(module))
                current_dir = os.getcwd()
                os.chdir(directory)
                import SBTVUserFields
                os.chdir(current_dir)
                self.EField = SBTVUserFields.E_func_user
                self.BField = SBTVUserFields.B_func_user
                print('Field value:',self.EField(np.array([0.0,0.0,0.0]),0.0,(0.0,0.0)))
            i-=1
        #except:
            #self.throw_error("No field file selected")
            #self.throw_error(sys.exc_info()[0])
    def throw_error(self,message):
        self.ErrorWindow = CustomError(message)
        self.ErrorWindow.show()        
    def browseFiles(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "QFileDialog.getOpenFileName()",
            "",
            "All Files (*);; Python Files(*.py)",
            )
        if filename:
            self.filename = filename
            self.ui.FileLineEdit.setText(filename)
            print(filename)
    def enable_cvc_options(self):
        self.ui.XYCheckBox.setEnabled(True)
        self.ui.XZCheckBox.setEnabled(True)
        self.ui.YZCheckBox.setEnabled(True)
        self.disable_vt_options()
    def disable_cvc_options(self):
        self.ui.XYCheckBox.setEnabled(False)
        self.ui.XZCheckBox.setEnabled(False)
        self.ui.YZCheckBox.setEnabled(False)
        self.ui.XYCheckBox.setChecked(False)
        self.ui.XZCheckBox.setChecked(False)
        self.ui.YZCheckBox.setChecked(False)
    def enable_vt_options(self):
        self.ui.CheckBoxX.setEnabled(True)
        self.ui.CheckBoxY.setEnabled(True)
        self.ui.CheckBoxZ.setEnabled(True)
        self.disable_cvc_options()
    def disable_vt_options(self):
        self.ui.CheckBoxX.setEnabled(False)
        self.ui.CheckBoxY.setEnabled(False)
        self.ui.CheckBoxZ.setEnabled(False)
        self.ui.CheckBoxX.setChecked(False)
        self.ui.CheckBoxY.setChecked(False)
        self.ui.CheckBoxZ.setChecked(False)
    def disable_2D_options(self):
        self.ui.TwoDOptionGroup.setExclusive(False)
        self.ui.CoordinateButton.setEnabled(False)
        self.ui.CoordinateButton.setChecked(False)
        self.ui.CoordinatevtButton.setEnabled(False)
        self.ui.CoordinatevtButton.setChecked(False)
        self.ui.PhaseButton.setEnabled(False)
        self.ui.PhaseButton.setChecked(False)
        self.ui.VelocityvtButton.setChecked(False)
        self.ui.VelocityvtButton.setEnabled(False)
        self.disable_cvc_options()
        self.disable_vt_options()
        self.ui.TwoDOptionGroup.setExclusive(True)
    def enable_2D_options(self):
        self.ui.CoordinateButton.setEnabled(True)
        self.ui.CoordinatevtButton.setEnabled(True)
        self.ui.PhaseButton.setEnabled(True)
        self.ui.VelocityvtButton.setEnabled(True)
    def throw_error(self,message):
        self.ErrorWindow = CustomError(message)
        self.ErrorWindow.show()
    def ComputeTrajectories(self):
        self.set_all()
        time1 = time.time()
        self.qs,self.dqs,self.ts = SBPP.Integrator_Synched_nonRel(self.q0s,self.dq0s,self.EField,self.BField,
        self.masses,self.charges,self.dt,self.tf,self.fparams,output_Freq = 1)
        time2 = time.time()
        self.write_to_user("Completed computation; it took {:e} seconds".format(time2-time1))
        self.qs = np.array(self.qs)
        self.dqs = np.array(self.dqs)
    def LaunchPlayer(self):
        self.set_frequency()
        if self.ui.ThreeDButton.isChecked():
            self.PlayerWindow = Ui_PlayerWindow(figsize=self.figsize)
            self.PlayerWindow.set_data(self.qs,self.dqs,frequency = self.frequency,ts = self.ts)
            self.PlayerWindow.set_options(plot_traj = self.ui.FullTrajectoryButton.isChecked())
            self.PlayerWindow.show()
        elif self.ui.CoordinatevtButton.isChecked():
            if self.ui.CheckBoxX.isChecked():
                self.PlayerWindowXvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvt.set_data(self.qs[:,:,0],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvt.set_options(axis_labels=('t[s]','x[m]'))
                self.PlayerWindowXvt.show()
            if self.ui.CheckBoxY.isChecked():
                self.PlayerWindowYvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowYvt.set_data(self.qs[:,:,1],self.ts,ts=self.ts,frequency=self.frequency)
                self.PlayerWindowYvt.set_options(axis_labels=('t[s]','y[m]'))
                self.PlayerWindowYvt.show()
            if self.ui.CheckBoxZ.isChecked():
                self.PlayerWindowZvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowZvt.set_data(self.qs[:,:,2],self.ts,ts=self.ts,frequency=self.frequency)
                self.PlayerWindowZvt.set_options(axis_labels=('t[s]','z[m]'))
                self.PlayerWindowZvt.show()
        elif self.ui.PhaseButton.isChecked():
            if self.ui.CheckBoxX.isChecked():
                self.PlayerWindowXvVx = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvVx.set_data(self.qs[:,:,0],self.dqs[:,:,0],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvVx.set_options(axis_labels=('x[m]','v$_x$[m/s]'))
                self.PlayerWindowXvVx.show()
            if self.ui.CheckBoxY.isChecked():
                self.PlayerWindowXvVy = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvVy.set_data(self.qs[:,:,1],self.dqs[:,:,1],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvVy.set_options(axis_labels=('y[m]','v$_y$[m/s]'))
                self.PlayerWindowXvVy.show()
            if self.ui.CheckBoxZ.isChecked():
                self.PlayerWindowXvVz = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvVz.set_data(self.qs[:,:,2],self.dqs[:,:,2],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvVz.set_options(axis_labels=('y[m]','v$_y$[m/s]'))
                self.PlayerWindowXvVz.show()
        elif self.ui.VelocityvtButton.isChecked():
            if self.ui.CheckBoxX.isChecked():
                self.PlayerWindowVxvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowVxvt.set_data(self.dqs[:,:,0],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowVxvt.set_options(axis_labels=('t[s]','v$_x$[m/s]'))
                self.PlayerWindowVxvt.show()
            if self.ui.CheckBoxY.isChecked():
                self.PlayerWindowVyvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowVyvt.set_data(self.dqs[:,:,1],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowVyvt.set_options(axis_labels=('t[s]','v$_y$[m/s]'))
                self.PlayerWindowVyvt.show()
            if self.ui.CheckBoxZ.isChecked():
                self.PlayerWindowVzvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowVzvt.set_data(self.dqs[:,:,2],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowVzvt.set_options(axis_labels=('t[s]','v$_z$[m/s]'))
                self.PlayerWindowVzvt.show()
        elif self.ui.CoordinateButton.isChecked():
            if self.ui.XYCheckBox.isChecked():
                self.PlayerWindowXvY = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvY.set_data(self.qs[:,:,0],self.qs[:,:,1],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvY.set_options(axis_labels=('x[m]','y[m]'))
                self.PlayerWindowXvY.show()
            if self.ui.XZCheckBox.isChecked():
                self.PlayerWindowXvZ = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvZ.set_data(self.qs[:,:,0],self.qs[:,:,2],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvZ.set_options(axis_labels=('x[m]','z[m]'))
                self.PlayerWindowXvZ.show()
            if self.ui.YZCheckBox.isChecked():
                self.PlayerWindowYvZ = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowYvZ.set_data(self.qs[:,:,1],self.qs[:,:,2],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowYvZ.set_options(axis_labels=('y[m]','z[y]'))
                self.PlayerWindowYvZ.show()
    def write_to_user(self,message):
        self.ui.UserInfoLabel.setText(message)
    def set_all(self):
        self.set_function()
        self.set_charges()
        self.set_masses()
        self.set_initial_positions()
        self.set_initial_velocities()
        self.set_dt()
        self.set_field_strengths()
        self.set_tf()
        self.set_frequency()
        self.set_figoptions()
        self.write_to_user("Set all values; ready to compute.")
    def set_figoptions(self):
        user_input = self.ui.FigureSizeBox.text()
        user_input = np.fromstring(user_input, sep = ' ')
        self.figsize = (user_input[0],user_input[1])
    def set_frequency(self):
        self.frequency = self.ui.FrequencyBox.value()    
    def set_charges(self):
        user_input = self.ui.ChargesEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep=' ')
            self.charges = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(user_input)
    def set_masses(self):
        user_input = self.ui.MassesEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep = ' ')
            self.masses = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
    def set_initial_positions(self):
        user_input = self.ui.PositionEntry.toPlainText()
        try:
            user_input = np.array(np.matrix(user_input))
            self.q0s = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(user_input)
    def set_initial_velocities(self):
        user_input = self.ui.VelocityEntry.toPlainText()
        try:
            user_input = np.array(np.matrix(user_input))
            self.dq0s = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(user_input)
    def set_field_strengths(self):
        user_input = self.ui.EFieldEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep=' ')
            self.fparams = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(self.fparams)
    
    def set_dt(self):
        user_input = self.ui.dtEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep = ' ')
            self.dt = user_input[0]
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
    def set_tf(self):
        user_input = self.ui.tfEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep = ' ')
            self.tf = user_input[0]
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
class MirrorSetupWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MirrorSetupWindow,self).__init__()
        self.ui = Ui_MirrorSetup()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.ui.SetAllButton.clicked.connect(self.set_all)
        self.ui.TwoDButton.clicked.connect(self.enable_2D_options)
        self.ui.ThreeDButton.clicked.connect(self.disable_2D_options)
        self.ui.CoordinatevtButton.clicked.connect(self.enable_vt_options)
        self.ui.PhaseButton.clicked.connect(self.enable_vt_options)
        self.ui.VelocityvtButton.clicked.connect(self.enable_vt_options)
        self.ui.CoordinateButton.clicked.connect(self.enable_cvc_options)
        self.ui.ComputeButton.clicked.connect(self.ComputeTrajectories)
        self.ui.AnimateButton.clicked.connect(self.LaunchPlayer)
    def enable_cvc_options(self):
        self.ui.XYCheckBox.setEnabled(True)
        self.ui.XZCheckBox.setEnabled(True)
        self.ui.YZCheckBox.setEnabled(True)
        self.disable_vt_options()
    def disable_cvc_options(self):
        self.ui.XYCheckBox.setEnabled(False)
        self.ui.XZCheckBox.setEnabled(False)
        self.ui.YZCheckBox.setEnabled(False)
        self.ui.XYCheckBox.setChecked(False)
        self.ui.XZCheckBox.setChecked(False)
        self.ui.YZCheckBox.setChecked(False)
    def enable_vt_options(self):
        self.ui.CheckBoxX.setEnabled(True)
        self.ui.CheckBoxY.setEnabled(True)
        self.ui.CheckBoxZ.setEnabled(True)
        self.disable_cvc_options()
    def disable_vt_options(self):
        self.ui.CheckBoxX.setEnabled(False)
        self.ui.CheckBoxY.setEnabled(False)
        self.ui.CheckBoxZ.setEnabled(False)
        self.ui.CheckBoxX.setChecked(False)
        self.ui.CheckBoxY.setChecked(False)
        self.ui.CheckBoxZ.setChecked(False)
    def disable_2D_options(self):
        self.ui.TwoDOptionGroup.setExclusive(False)
        self.ui.CoordinateButton.setEnabled(False)
        self.ui.CoordinateButton.setChecked(False)
        self.ui.CoordinatevtButton.setEnabled(False)
        self.ui.CoordinatevtButton.setChecked(False)
        self.ui.PhaseButton.setEnabled(False)
        self.ui.PhaseButton.setChecked(False)
        self.ui.VelocityvtButton.setChecked(False)
        self.ui.VelocityvtButton.setEnabled(False)
        self.disable_cvc_options()
        self.disable_vt_options()
        self.ui.TwoDOptionGroup.setExclusive(True)
    def enable_2D_options(self):
        self.ui.CoordinateButton.setEnabled(True)
        self.ui.CoordinatevtButton.setEnabled(True)
        self.ui.PhaseButton.setEnabled(True)
        self.ui.VelocityvtButton.setEnabled(True)
    def throw_error(self,message):
        self.ErrorWindow = CustomError(message)
        self.ErrorWindow.show()
    def ComputeTrajectories(self):
        self.set_all()
        time1 = time.time()
        self.qs,self.dqs,self.ts = SBPP.Integrator_Synched_nonRel(self.q0s,self.dq0s,E_func_zero,B_func_Magnetic_Mirror,
        self.masses,self.charges,self.dt,self.tf,self.fparams,output_Freq = 1)
        time2 = time.time()
        self.write_to_user("Completed computation; it took {:e} seconds".format(time2-time1))
        self.qs = np.array(self.qs)
        self.dqs = np.array(self.dqs)
    def LaunchPlayer(self):
        self.set_frequency()
        if self.ui.ThreeDButton.isChecked():
            self.PlayerWindow = Ui_PlayerWindow(figsize=self.figsize)
            self.PlayerWindow.set_data(self.qs,self.dqs,frequency = self.frequency,ts = self.ts)
            self.PlayerWindow.set_options(plot_traj = self.ui.FullTrajectoryButton.isChecked())
            self.PlayerWindow.show()
        elif self.ui.CoordinatevtButton.isChecked():
            if self.ui.CheckBoxX.isChecked():
                self.PlayerWindowXvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvt.set_data(self.qs[:,:,0],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvt.set_options(axis_labels=('t[s]','x[m]'))
                self.PlayerWindowXvt.show()
            if self.ui.CheckBoxY.isChecked():
                self.PlayerWindowYvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowYvt.set_data(self.qs[:,:,1],self.ts,ts=self.ts,frequency=self.frequency)
                self.PlayerWindowYvt.set_options(axis_labels=('t[s]','y[m]'))
                self.PlayerWindowYvt.show()
            if self.ui.CheckBoxZ.isChecked():
                self.PlayerWindowZvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowZvt.set_data(self.qs[:,:,2],self.ts,ts=self.ts,frequency=self.frequency)
                self.PlayerWindowZvt.set_options(axis_labels=('t[s]','z[m]'))
                self.PlayerWindowZvt.show()
        elif self.ui.PhaseButton.isChecked():
            if self.ui.CheckBoxX.isChecked():
                self.PlayerWindowXvVx = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvVx.set_data(self.qs[:,:,0],self.dqs[:,:,0],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvVx.set_options(axis_labels=('x[m]','v$_x$[m/s]'))
                self.PlayerWindowXvVx.show()
            if self.ui.CheckBoxY.isChecked():
                self.PlayerWindowXvVy = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvVy.set_data(self.qs[:,:,1],self.dqs[:,:,1],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvVy.set_options(axis_labels=('y[m]','v$_y$[m/s]'))
                self.PlayerWindowXvVy.show()
            if self.ui.CheckBoxZ.isChecked():
                self.PlayerWindowXvVz = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvVz.set_data(self.qs[:,:,2],self.dqs[:,:,2],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvVz.set_options(axis_labels=('y[m]','v$_y$[m/s]'))
                self.PlayerWindowXvVz.show()
        elif self.ui.VelocityvtButton.isChecked():
            if self.ui.CheckBoxX.isChecked():
                self.PlayerWindowVxvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowVxvt.set_data(self.dqs[:,:,0],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowVxvt.set_options(axis_labels=('t[s]','v$_x$[m/s]'))
                self.PlayerWindowVxvt.show()
            if self.ui.CheckBoxY.isChecked():
                self.PlayerWindowVyvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowVyvt.set_data(self.dqs[:,:,1],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowVyvt.set_options(axis_labels=('t[s]','v$_y$[m/s]'))
                self.PlayerWindowVyvt.show()
            if self.ui.CheckBoxZ.isChecked():
                self.PlayerWindowVzvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowVzvt.set_data(self.dqs[:,:,2],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowVzvt.set_options(axis_labels=('t[s]','v$_z$[m/s]'))
                self.PlayerWindowVzvt.show()
        elif self.ui.CoordinateButton.isChecked():
            if self.ui.XYCheckBox.isChecked():
                self.PlayerWindowXvY = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvY.set_data(self.qs[:,:,0],self.qs[:,:,1],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvY.set_options(axis_labels=('x[m]','y[m]'))
                self.PlayerWindowXvY.show()
            if self.ui.XZCheckBox.isChecked():
                self.PlayerWindowXvZ = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvZ.set_data(self.qs[:,:,0],self.qs[:,:,2],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvZ.set_options(axis_labels=('x[m]','z[m]'))
                self.PlayerWindowXvZ.show()
            if self.ui.YZCheckBox.isChecked():
                self.PlayerWindowYvZ = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowYvZ.set_data(self.qs[:,:,1],self.qs[:,:,2],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowYvZ.set_options(axis_labels=('y[m]','z[y]'))
                self.PlayerWindowYvZ.show()
    def write_to_user(self,message):
        self.ui.UserInfoLabel.setText(message)
    def set_all(self):
        self.set_charges()
        self.set_masses()
        self.set_initial_positions()
        self.set_initial_velocities()
        self.set_dt()
        self.set_field_strengths()
        self.set_tf()
        self.set_frequency()
        self.set_figoptions()
        self.write_to_user("Set all values; ready to compute.")
    def set_figoptions(self):
        user_input = self.ui.FigureSizeBox.text()
        user_input = np.fromstring(user_input, sep = ' ')
        self.figsize = (user_input[0],user_input[1])
    def set_frequency(self):
        self.frequency = self.ui.FrequencyBox.value()    
    def set_charges(self):
        user_input = self.ui.ChargesEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep=' ')
            self.charges = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(user_input)
    def set_masses(self):
        user_input = self.ui.MassesEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep = ' ')
            self.masses = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
    def set_initial_positions(self):
        user_input = self.ui.PositionEntry.toPlainText()
        try:
            user_input = np.array(np.matrix(user_input))
            self.q0s = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(user_input)
    def set_initial_velocities(self):
        user_input = self.ui.VelocityEntry.toPlainText()
        try:
            user_input = np.array(np.matrix(user_input))
            self.dq0s = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(user_input)
    def set_field_strengths(self):
        user_input = self.ui.EFieldEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep=' ')
            self.fparams = (0,user_input[0],user_input[1])
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(self.fparams)
    
    def set_dt(self):
        user_input = self.ui.dtEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep = ' ')
            self.dt = user_input[0]
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
    def set_tf(self):
        user_input = self.ui.tfEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep = ' ')
            self.tf = user_input[0]
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
class DipoleSetupWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(DipoleSetupWindow,self).__init__()
        self.ui = Ui_DipoleSetupWindow()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.ui.SetAllButton.clicked.connect(self.set_all)
        self.ui.TwoDButton.clicked.connect(self.enable_2D_options)
        self.ui.ThreeDButton.clicked.connect(self.disable_2D_options)
        self.ui.CoordinatevtButton.clicked.connect(self.enable_vt_options)
        self.ui.PhaseButton.clicked.connect(self.enable_vt_options)
        self.ui.VelocityvtButton.clicked.connect(self.enable_vt_options)
        self.ui.CoordinateButton.clicked.connect(self.enable_cvc_options)
        self.ui.ComputeButton.clicked.connect(self.ComputeTrajectories)
        self.ui.AnimateButton.clicked.connect(self.LaunchPlayer)
    def enable_cvc_options(self):
        self.ui.XYCheckBox.setEnabled(True)
        self.ui.XZCheckBox.setEnabled(True)
        self.ui.YZCheckBox.setEnabled(True)
        self.disable_vt_options()
    def disable_cvc_options(self):
        self.ui.XYCheckBox.setEnabled(False)
        self.ui.XZCheckBox.setEnabled(False)
        self.ui.YZCheckBox.setEnabled(False)
        self.ui.XYCheckBox.setChecked(False)
        self.ui.XZCheckBox.setChecked(False)
        self.ui.YZCheckBox.setChecked(False)
    def enable_vt_options(self):
        self.ui.CheckBoxX.setEnabled(True)
        self.ui.CheckBoxY.setEnabled(True)
        self.ui.CheckBoxZ.setEnabled(True)
        self.disable_cvc_options()
    def disable_vt_options(self):
        self.ui.CheckBoxX.setEnabled(False)
        self.ui.CheckBoxY.setEnabled(False)
        self.ui.CheckBoxZ.setEnabled(False)
        self.ui.CheckBoxX.setChecked(False)
        self.ui.CheckBoxY.setChecked(False)
        self.ui.CheckBoxZ.setChecked(False)
    def disable_2D_options(self):
        self.ui.TwoDOptionGroup.setExclusive(False)
        self.ui.CoordinateButton.setEnabled(False)
        self.ui.CoordinateButton.setChecked(False)
        self.ui.CoordinatevtButton.setEnabled(False)
        self.ui.CoordinatevtButton.setChecked(False)
        self.ui.PhaseButton.setEnabled(False)
        self.ui.PhaseButton.setChecked(False)
        self.ui.VelocityvtButton.setChecked(False)
        self.ui.VelocityvtButton.setEnabled(False)
        self.disable_cvc_options()
        self.disable_vt_options()
        self.ui.TwoDOptionGroup.setExclusive(True)
    def enable_2D_options(self):
        self.ui.CoordinateButton.setEnabled(True)
        self.ui.CoordinatevtButton.setEnabled(True)
        self.ui.PhaseButton.setEnabled(True)
        self.ui.VelocityvtButton.setEnabled(True)
    def throw_error(self,message):
        self.ErrorWindow = CustomError(message)
        self.ErrorWindow.show()
    def ComputeTrajectories(self):
        self.set_all()
        time1 = time.time()
        self.qs,self.dqs,self.ts = SBPP.Integrator_Synched_nonRel(self.q0s,self.dq0s,E_func_zero,B_func_Dipolar,
        self.masses,self.charges,self.dt,self.tf,self.fparams,output_Freq = 1)
        time2 = time.time()
        self.write_to_user("Completed computation; it took {:e} seconds".format(time2-time1))
        self.qs = np.array(self.qs)
        self.dqs = np.array(self.dqs)
    def LaunchPlayer(self):
        self.set_frequency()
        if self.ui.ThreeDButton.isChecked():
            self.PlayerWindow = Ui_PlayerWindow(figsize=self.figsize)
            self.PlayerWindow.set_data(self.qs,self.dqs,frequency = self.frequency,ts = self.ts)
            self.PlayerWindow.set_options(plot_traj = self.ui.FullTrajectoryButton.isChecked(),interval = 
            self.ui.IntervalBox.value())
            self.PlayerWindow.show()
        elif self.ui.CoordinatevtButton.isChecked():
            if self.ui.CheckBoxX.isChecked():
                self.PlayerWindowXvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvt.set_data(self.qs[:,:,0],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvt.set_options(axis_labels=('t[s]','x[m]'))
                self.PlayerWindowXvt.show()
            if self.ui.CheckBoxY.isChecked():
                self.PlayerWindowYvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowYvt.set_data(self.qs[:,:,1],self.ts,ts=self.ts,frequency=self.frequency)
                self.PlayerWindowYvt.set_options(axis_labels=('t[s]','y[m]'))
                self.PlayerWindowYvt.show()
            if self.ui.CheckBoxZ.isChecked():
                self.PlayerWindowZvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowZvt.set_data(self.qs[:,:,2],self.ts,ts=self.ts,frequency=self.frequency)
                self.PlayerWindowZvt.set_options(axis_labels=('t[s]','z[m]'))
                self.PlayerWindowZvt.show()
        elif self.ui.PhaseButton.isChecked():
            if self.ui.CheckBoxX.isChecked():
                self.PlayerWindowXvVx = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvVx.set_data(self.qs[:,:,0],self.dqs[:,:,0],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvVx.set_options(axis_labels=('x[m]','v$_x$[m/s]'))
                self.PlayerWindowXvVx.show()
            if self.ui.CheckBoxY.isChecked():
                self.PlayerWindowXvVy = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvVy.set_data(self.qs[:,:,1],self.dqs[:,:,1],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvVy.set_options(axis_labels=('y[m]','v$_y$[m/s]'))
                self.PlayerWindowXvVy.show()
            if self.ui.CheckBoxZ.isChecked():
                self.PlayerWindowXvVz = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvVz.set_data(self.qs[:,:,2],self.dqs[:,:,2],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvVz.set_options(axis_labels=('y[m]','v$_y$[m/s]'))
                self.PlayerWindowXvVz.show()
        elif self.ui.VelocityvtButton.isChecked():
            if self.ui.CheckBoxX.isChecked():
                self.PlayerWindowVxvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowVxvt.set_data(self.dqs[:,:,0],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowVxvt.set_options(axis_labels=('t[s]','v$_x$[m/s]'))
                self.PlayerWindowVxvt.show()
            if self.ui.CheckBoxY.isChecked():
                self.PlayerWindowVyvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowVyvt.set_data(self.dqs[:,:,1],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowVyvt.set_options(axis_labels=('t[s]','v$_y$[m/s]'))
                self.PlayerWindowVyvt.show()
            if self.ui.CheckBoxZ.isChecked():
                self.PlayerWindowVzvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowVzvt.set_data(self.dqs[:,:,2],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowVzvt.set_options(axis_labels=('t[s]','v$_z$[m/s]'))
                self.PlayerWindowVzvt.show()
        elif self.ui.CoordinateButton.isChecked():
            if self.ui.XYCheckBox.isChecked():
                self.PlayerWindowXvY = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvY.set_data(self.qs[:,:,0],self.qs[:,:,1],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvY.set_options(axis_labels=('x[m]','y[m]'))
                self.PlayerWindowXvY.show()
            if self.ui.XZCheckBox.isChecked():
                self.PlayerWindowXvZ = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvZ.set_data(self.qs[:,:,0],self.qs[:,:,2],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvZ.set_options(axis_labels=('x[m]','z[m]'))
                self.PlayerWindowXvZ.show()
            if self.ui.YZCheckBox.isChecked():
                self.PlayerWindowYvZ = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowYvZ.set_data(self.qs[:,:,1],self.qs[:,:,2],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowYvZ.set_options(axis_labels=('y[m]','z[y]'))
                self.PlayerWindowYvZ.show()
    def write_to_user(self,message):
        self.ui.UserInfoLabel.setText(message)
    def set_all(self):
        try:
            self.set_charges()
            self.set_masses()
            self.set_initial_positions()
            self.set_initial_velocities()
            self.set_dt()
            self.set_field_strengths()
            self.set_tf()
            self.set_frequency()
            self.set_figoptions()
            self.write_to_user("Set all values; ready to compute.")
        except:
            self.throw_error("Format error; check all boxes and try again!")
            self.write_to_user("Failed")
    def set_figoptions(self):
        user_input = self.ui.FigureSizeBox.text()
        user_input = np.fromstring(user_input, sep = ' ')
        self.figsize = (user_input[0],user_input[1])
    def set_frequency(self):
        self.frequency = self.ui.FrequencyBox.value()
    def set_charges(self):
        user_input = self.ui.ChargesEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep=' ')
            self.charges = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(user_input)
    def set_masses(self):
        user_input = self.ui.MassesEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep = ' ')
            self.masses = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
    def set_initial_positions(self):
        user_input = self.ui.PositionEntry.toPlainText()
        try:
            user_input = np.array(np.matrix(user_input))
            self.q0s = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(user_input)
    def set_initial_velocities(self):
        user_input = self.ui.VelocityEntry.toPlainText()
        try:
            user_input = np.array(np.matrix(user_input))
            self.dq0s = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(user_input)
    def set_field_strengths(self):
        user_inputEField = self.ui.EFieldEntry.toPlainText()
        try:
            user_inputEField = np.fromstring(user_inputEField,sep=' ')
            self.fparams = (0,0,0,user_inputEField[0])
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(self.fparams)
    
    def set_dt(self):
        user_input = self.ui.dtEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep = ' ')
            self.dt = user_input[0]
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
    def set_tf(self):
        user_input = self.ui.tfEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep = ' ')
            self.tf = user_input[0]
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)    
    
class NullSetupWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(NullSetupWindow,self).__init__()
        self.ui = Ui_NullSetupWindow()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.ui.SetAllButton.clicked.connect(self.set_all)
        self.ui.TwoDButton.clicked.connect(self.enable_2D_options)
        self.ui.ThreeDButton.clicked.connect(self.disable_2D_options)
        self.ui.CoordinatevtButton.clicked.connect(self.enable_vt_options)
        self.ui.PhaseButton.clicked.connect(self.enable_vt_options)
        self.ui.VelocityvtButton.clicked.connect(self.enable_vt_options)
        self.ui.CoordinateButton.clicked.connect(self.enable_cvc_options)
        self.ui.ComputeButton.clicked.connect(self.ComputeTrajectories)
        self.ui.AnimateButton.clicked.connect(self.LaunchPlayer)
    def enable_cvc_options(self):
        self.ui.XYCheckBox.setEnabled(True)
        self.ui.XZCheckBox.setEnabled(True)
        self.ui.YZCheckBox.setEnabled(True)
        self.disable_vt_options()
    def disable_cvc_options(self):
        self.ui.XYCheckBox.setEnabled(False)
        self.ui.XZCheckBox.setEnabled(False)
        self.ui.YZCheckBox.setEnabled(False)
        self.ui.XYCheckBox.setChecked(False)
        self.ui.XZCheckBox.setChecked(False)
        self.ui.YZCheckBox.setChecked(False)
    def enable_vt_options(self):
        self.ui.CheckBoxX.setEnabled(True)
        self.ui.CheckBoxY.setEnabled(True)
        self.ui.CheckBoxZ.setEnabled(True)
        self.disable_cvc_options()
    def disable_vt_options(self):
        self.ui.CheckBoxX.setEnabled(False)
        self.ui.CheckBoxY.setEnabled(False)
        self.ui.CheckBoxZ.setEnabled(False)
        self.ui.CheckBoxX.setChecked(False)
        self.ui.CheckBoxY.setChecked(False)
        self.ui.CheckBoxZ.setChecked(False)
    def disable_2D_options(self):
        self.ui.TwoDOptionGroup.setExclusive(False)
        self.ui.CoordinateButton.setEnabled(False)
        self.ui.CoordinateButton.setChecked(False)
        self.ui.CoordinatevtButton.setEnabled(False)
        self.ui.CoordinatevtButton.setChecked(False)
        self.ui.PhaseButton.setEnabled(False)
        self.ui.PhaseButton.setChecked(False)
        self.ui.VelocityvtButton.setChecked(False)
        self.ui.VelocityvtButton.setEnabled(False)
        self.disable_cvc_options()
        self.disable_vt_options()
        self.ui.TwoDOptionGroup.setExclusive(True)
    def enable_2D_options(self):
        self.ui.CoordinateButton.setEnabled(True)
        self.ui.CoordinatevtButton.setEnabled(True)
        self.ui.PhaseButton.setEnabled(True)
        self.ui.VelocityvtButton.setEnabled(True)
    def throw_error(self,message):
        self.ErrorWindow = CustomError(message)
        self.ErrorWindow.show()
    def ComputeTrajectories(self):
        self.set_all()
        time1 = time.time()
        self.masses = self.masses[0]*np.ones(shape = self.particleNumber)
        self.charges = self.charges[0]*np.ones(shape = self.particleNumber)
        self.q0s,self.dq0s = generate_magnetic_null_conditions(self.particleNumber,self.vrad)
        self.qs,self.dqs,self.ts = SBPP.Integrator_Synched_nonRel(self.q0s,self.dq0s,E_func_zero,B_func_Null,
        self.masses,self.charges,self.dt,self.tf,self.fparams,output_Freq = 1)
        time2 = time.time()
        self.write_to_user("Completed computation; it took {:e} seconds".format(time2-time1))
        self.qs = np.array(self.qs)
        self.dqs = np.array(self.dqs)
    def LaunchPlayer(self):
        self.set_frequency()
        if self.ui.ThreeDButton.isChecked():
            self.PlayerWindow = Ui_PlayerWindow(figsize=self.figsize)
            self.PlayerWindow.set_data(self.qs,self.dqs,frequency = self.frequency,ts = self.ts)
            self.PlayerWindow.set_options(plot_traj = self.ui.FullTrajectoryButton.isChecked(),interval = 
            self.ui.IntervalBox.value())
            self.PlayerWindow.show()
        elif self.ui.CoordinatevtButton.isChecked():
            if self.ui.CheckBoxX.isChecked():
                self.PlayerWindowXvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvt.set_data(self.qs[:,:,0],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvt.set_options(axis_labels=('t[s]','x[m]'))
                self.PlayerWindowXvt.show()
            if self.ui.CheckBoxY.isChecked():
                self.PlayerWindowYvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowYvt.set_data(self.qs[:,:,1],self.ts,ts=self.ts,frequency=self.frequency)
                self.PlayerWindowYvt.set_options(axis_labels=('t[s]','y[m]'))
                self.PlayerWindowYvt.show()
            if self.ui.CheckBoxZ.isChecked():
                self.PlayerWindowZvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowZvt.set_data(self.qs[:,:,2],self.ts,ts=self.ts,frequency=self.frequency)
                self.PlayerWindowZvt.set_options(axis_labels=('t[s]','z[m]'))
                self.PlayerWindowZvt.show()
        elif self.ui.PhaseButton.isChecked():
            if self.ui.CheckBoxX.isChecked():
                self.PlayerWindowXvVx = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvVx.set_data(self.qs[:,:,0],self.dqs[:,:,0],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvVx.set_options(axis_labels=('x[m]','v$_x$[m/s]'))
                self.PlayerWindowXvVx.show()
            if self.ui.CheckBoxY.isChecked():
                self.PlayerWindowXvVy = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvVy.set_data(self.qs[:,:,1],self.dqs[:,:,1],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvVy.set_options(axis_labels=('y[m]','v$_y$[m/s]'))
                self.PlayerWindowXvVy.show()
            if self.ui.CheckBoxZ.isChecked():
                self.PlayerWindowXvVz = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvVz.set_data(self.qs[:,:,2],self.dqs[:,:,2],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvVz.set_options(axis_labels=('y[m]','v$_y$[m/s]'))
                self.PlayerWindowXvVz.show()
        elif self.ui.VelocityvtButton.isChecked():
            if self.ui.CheckBoxX.isChecked():
                self.PlayerWindowVxvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowVxvt.set_data(self.dqs[:,:,0],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowVxvt.set_options(axis_labels=('t[s]','v$_x$[m/s]'))
                self.PlayerWindowVxvt.show()
            if self.ui.CheckBoxY.isChecked():
                self.PlayerWindowVyvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowVyvt.set_data(self.dqs[:,:,1],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowVyvt.set_options(axis_labels=('t[s]','v$_y$[m/s]'))
                self.PlayerWindowVyvt.show()
            if self.ui.CheckBoxZ.isChecked():
                self.PlayerWindowVzvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowVzvt.set_data(self.dqs[:,:,2],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowVzvt.set_options(axis_labels=('t[s]','v$_z$[m/s]'))
                self.PlayerWindowVzvt.show()
        elif self.ui.CoordinateButton.isChecked():
            if self.ui.XYCheckBox.isChecked():
                self.PlayerWindowXvY = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvY.set_data(self.qs[:,:,0],self.qs[:,:,1],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvY.set_options(axis_labels=('x[m]','y[m]'),
                plot_traj = self.ui.FullTrajectoryButton.isChecked())
                self.PlayerWindowXvY.show()
            if self.ui.XZCheckBox.isChecked():
                self.PlayerWindowXvZ = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvZ.set_data(self.qs[:,:,0],self.qs[:,:,2],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvZ.set_options(axis_labels=('x[m]','z[m]'))
                self.PlayerWindowXvZ.show()
            if self.ui.YZCheckBox.isChecked():
                self.PlayerWindowYvZ = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowYvZ.set_data(self.qs[:,:,1],self.qs[:,:,2],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowYvZ.set_options(axis_labels=('y[m]','z[y]'))
                self.PlayerWindowYvZ.show()
    def write_to_user(self,message):
        self.ui.UserInfoLabel.setText(message)
    def set_all(self):
        try:
            self.set_charges()
            self.set_masses()
            self.set_initial_positions()
            self.set_initial_velocities()
            self.set_dt()
            self.set_field_strengths()
            self.set_tf()
            self.set_frequency()
            self.set_figoptions()
            self.set_particleNumber()
            self.write_to_user("Set all values; ready to compute.")
        except:
            self.throw_error("Format error; check all boxes and try again!")
            self.write_to_user("Failed; correct errors and try again.")
    def set_figoptions(self):
        user_input = self.ui.FigureSizeBox.text()
        user_input = np.fromstring(user_input, sep = ' ')
        self.figsize = (user_input[0],user_input[1])
    def set_frequency(self):
        self.frequency = self.ui.FrequencyBox.value()
    def set_charges(self):
        user_input = self.ui.ChargesEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep=' ')
            self.charges = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(user_input)
    def set_masses(self):
        user_input = self.ui.MassesEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep = ' ')
            self.masses = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
    def set_particleNumber(self):
        user_input = self.ui.ParticleNumberEntry.toPlainText()
        print(user_input)
        try:
            user_input = np.fromstring(user_input,sep=' ')
            self.particleNumber = user_input[0]
            self.particleNumber = int(self.particleNumber)
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
    def set_initial_positions(self):
        user_input = self.ui.PositionEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep=' ')
            rad_circ = user_input[0]
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(user_input)
    def set_initial_velocities(self):
        user_input = self.ui.VelocityEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep=' ')
            self.vrad = user_input[0]
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(user_input)
    def set_field_strengths(self):
        user_input = self.ui.BFieldEntry.toPlainText()
        print(user_input)
        try:
            user_input = np.fromstring(user_input,sep=' ')
            self.fparams = (0,user_input[0],user_input[1],0)
            print(self.fparams)
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        
    
    def set_dt(self):
        user_input = self.ui.dtEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep = ' ')
            self.dt = user_input[0]
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
    def set_tf(self):
        user_input = self.ui.tfEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep = ' ')
            self.tf = user_input[0]
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
class DriftSetupWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(DriftSetupWindow,self).__init__()
        self.ui = Ui_DriftSetupWindow()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.ui.SetAllButton.clicked.connect(self.set_all)
        self.ui.TwoDButton.clicked.connect(self.enable_2D_options)
        self.ui.ThreeDButton.clicked.connect(self.disable_2D_options)
        self.ui.CoordinatevtButton.clicked.connect(self.enable_vt_options)
        self.ui.PhaseButton.clicked.connect(self.enable_vt_options)
        self.ui.VelocityvtButton.clicked.connect(self.enable_vt_options)
        self.ui.CoordinateButton.clicked.connect(self.enable_cvc_options)
        self.ui.ComputeButton.clicked.connect(self.ComputeTrajectories)
        self.ui.AnimateButton.clicked.connect(self.LaunchPlayer)
    def enable_cvc_options(self):
        self.ui.XYCheckBox.setEnabled(True)
        self.ui.XZCheckBox.setEnabled(True)
        self.ui.YZCheckBox.setEnabled(True)
        self.disable_vt_options()
    def disable_cvc_options(self):
        self.ui.XYCheckBox.setEnabled(False)
        self.ui.XZCheckBox.setEnabled(False)
        self.ui.YZCheckBox.setEnabled(False)
        self.ui.XYCheckBox.setChecked(False)
        self.ui.XZCheckBox.setChecked(False)
        self.ui.YZCheckBox.setChecked(False)
    def enable_vt_options(self):
        self.ui.CheckBoxX.setEnabled(True)
        self.ui.CheckBoxY.setEnabled(True)
        self.ui.CheckBoxZ.setEnabled(True)
        self.disable_cvc_options()
    def disable_vt_options(self):
        self.ui.CheckBoxX.setEnabled(False)
        self.ui.CheckBoxY.setEnabled(False)
        self.ui.CheckBoxZ.setEnabled(False)
        self.ui.CheckBoxX.setChecked(False)
        self.ui.CheckBoxY.setChecked(False)
        self.ui.CheckBoxZ.setChecked(False)
    def disable_2D_options(self):
        self.ui.TwoDOptionGroup.setExclusive(False)
        self.ui.CoordinateButton.setEnabled(False)
        self.ui.CoordinateButton.setChecked(False)
        self.ui.CoordinatevtButton.setEnabled(False)
        self.ui.CoordinatevtButton.setChecked(False)
        self.ui.PhaseButton.setEnabled(False)
        self.ui.PhaseButton.setChecked(False)
        self.ui.VelocityvtButton.setChecked(False)
        self.ui.VelocityvtButton.setEnabled(False)
        self.disable_cvc_options()
        self.disable_vt_options()
        self.ui.TwoDOptionGroup.setExclusive(True)
    def enable_2D_options(self):
        self.ui.CoordinateButton.setEnabled(True)
        self.ui.CoordinatevtButton.setEnabled(True)
        self.ui.PhaseButton.setEnabled(True)
        self.ui.VelocityvtButton.setEnabled(True)
    def throw_error(self,message):
        self.ErrorWindow = CustomError(message)
        self.ErrorWindow.show()
    def ComputeTrajectories(self):
        self.set_all()
        time1 = time.time()
        self.qs,self.dqs,self.ts = SBPP.Integrator_Synched_nonRel(self.q0s,self.dq0s,E_func_uniform_arbitrary,B_func_uniform_arbitrary,
        self.masses,self.charges,self.dt,self.tf,self.fparams,output_Freq = 1)
        time2 = time.time()
        self.write_to_user("Completed computation; it took {:e} seconds".format(time2-time1))
        self.qs = np.array(self.qs)
        self.dqs = np.array(self.dqs)
    def LaunchPlayer(self):
        self.set_frequency()
        if self.ui.ThreeDButton.isChecked():
            self.PlayerWindow = Ui_PlayerWindow(figsize=self.figsize)
            self.PlayerWindow.set_data(self.qs,self.dqs,frequency = self.frequency,ts = self.ts)
            self.PlayerWindow.set_options(plot_traj = self.ui.FullTrajectoryButton.isChecked())
            self.PlayerWindow.show()
        elif self.ui.CoordinatevtButton.isChecked():
            if self.ui.CheckBoxX.isChecked():
                self.PlayerWindowXvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvt.set_data(self.qs[:,:,0],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvt.set_options(axis_labels=('t[s]','x[m]'))
                self.PlayerWindowXvt.show()
            if self.ui.CheckBoxY.isChecked():
                self.PlayerWindowYvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowYvt.set_data(self.qs[:,:,1],self.ts,ts=self.ts,frequency=self.frequency)
                self.PlayerWindowYvt.set_options(axis_labels=('t[s]','y[m]'))
                self.PlayerWindowYvt.show()
            if self.ui.CheckBoxZ.isChecked():
                self.PlayerWindowZvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowZvt.set_data(self.qs[:,:,2],self.ts,ts=self.ts,frequency=self.frequency)
                self.PlayerWindowZvt.set_options(axis_labels=('t[s]','z[m]'))
                self.PlayerWindowZvt.show()
        elif self.ui.PhaseButton.isChecked():
            if self.ui.CheckBoxX.isChecked():
                self.PlayerWindowXvVx = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvVx.set_data(self.qs[:,:,0],self.dqs[:,:,0],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvVx.set_options(axis_labels=('x[m]','v$_x$[m/s]'))
                self.PlayerWindowXvVx.show()
            if self.ui.CheckBoxY.isChecked():
                self.PlayerWindowXvVy = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvVy.set_data(self.qs[:,:,1],self.dqs[:,:,1],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvVy.set_options(axis_labels=('y[m]','v$_y$[m/s]'))
                self.PlayerWindowXvVy.show()
            if self.ui.CheckBoxZ.isChecked():
                self.PlayerWindowXvVz = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvVz.set_data(self.qs[:,:,2],self.dqs[:,:,2],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvVz.set_options(axis_labels=('y[m]','v$_y$[m/s]'))
                self.PlayerWindowXvVz.show()
        elif self.ui.VelocityvtButton.isChecked():
            if self.ui.CheckBoxX.isChecked():
                self.PlayerWindowVxvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowVxvt.set_data(self.dqs[:,:,0],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowVxvt.set_options(axis_labels=('t[s]','v$_x$[m/s]'))
                self.PlayerWindowVxvt.show()
            if self.ui.CheckBoxY.isChecked():
                self.PlayerWindowVyvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowVyvt.set_data(self.dqs[:,:,1],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowVyvt.set_options(axis_labels=('t[s]','v$_y$[m/s]'))
                self.PlayerWindowVyvt.show()
            if self.ui.CheckBoxZ.isChecked():
                self.PlayerWindowVzvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowVzvt.set_data(self.dqs[:,:,2],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowVzvt.set_options(axis_labels=('t[s]','v$_z$[m/s]'))
                self.PlayerWindowVzvt.show()
        elif self.ui.CoordinateButton.isChecked():
            if self.ui.XYCheckBox.isChecked():
                self.PlayerWindowXvY = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvY.set_data(self.qs[:,:,0],self.qs[:,:,1],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvY.set_options(axis_labels=('x[m]','y[m]'))
                self.PlayerWindowXvY.show()
            if self.ui.XZCheckBox.isChecked():
                self.PlayerWindowXvZ = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvZ.set_data(self.qs[:,:,0],self.qs[:,:,2],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvZ.set_options(axis_labels=('x[m]','z[m]'))
                self.PlayerWindowXvZ.show()
            if self.ui.YZCheckBox.isChecked():
                self.PlayerWindowYvZ = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowYvZ.set_data(self.qs[:,:,1],self.qs[:,:,2],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowYvZ.set_options(axis_labels=('y[m]','z[y]'))
                self.PlayerWindowYvZ.show()
    def write_to_user(self,message):
        self.ui.UserInfoLabel.setText(message)
    def set_all(self):
        try:
            self.set_charges()
            self.set_masses()
            self.set_initial_positions()
            self.set_initial_velocities()
            self.set_dt()
            self.set_field_strengths()
            self.set_tf()
            self.set_frequency()
            self.set_figoptions()
            self.write_to_user("Set all values; ready to compute.")
        except:
            self.throw_error("Format error; check all boxes and try again")
            self.write_to_user("Failed; correct errors and try again")
    def set_figoptions(self):
        user_input = self.ui.FigureSizeBox.text()
        user_input = np.fromstring(user_input, sep = ' ')
        self.figsize = (user_input[0],user_input[1])
    def set_frequency(self):
        self.frequency = self.ui.FrequencyBox.value()
    def set_charges(self):
        user_input = self.ui.ChargesEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep=' ')
            self.charges = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(user_input)
    def set_masses(self):
        user_input = self.ui.MassesEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep = ' ')
            self.masses = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
    def set_initial_positions(self):
        user_input = self.ui.PositionEntry.toPlainText()
        try:
            user_input = np.array(np.matrix(user_input))
            self.q0s = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(user_input)
    def set_initial_velocities(self):
        user_input = self.ui.VelocityEntry.toPlainText()
        try:
            user_input = np.array(np.matrix(user_input))
            self.dq0s = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(user_input)
    def set_field_strengths(self):
        user_inputEField = self.ui.EFieldEntry.toPlainText()
        user_inputBField = self.ui.BFieldEntry.toPlainText()
        try:
            user_inputEField = np.fromstring(user_inputEField,sep=' ')
            user_inputBField = np.fromstring(user_inputBField,sep=' ')
            self.fparams = (user_inputEField[0],user_inputEField[1],user_inputEField[2],
            user_inputBField[0],user_inputBField[1],user_inputBField[2])
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(self.fparams)
    
    def set_dt(self):
        user_input = self.ui.dtEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep = ' ')
            self.dt = user_input[0]
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
    def set_tf(self):
        user_input = self.ui.tfEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep = ' ')
            self.tf = user_input[0]
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
class BFieldSetupWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(BFieldSetupWindow,self).__init__()
        self.ui = Ui_BFieldSetup()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.ui.SetAllButton.clicked.connect(self.set_all)
        self.ui.TwoDButton.clicked.connect(self.enable_2D_options)
        self.ui.ThreeDButton.clicked.connect(self.disable_2D_options)
        self.ui.CoordinatevtButton.clicked.connect(self.enable_vt_options)
        self.ui.PhaseButton.clicked.connect(self.enable_vt_options)
        self.ui.VelocityvtButton.clicked.connect(self.enable_vt_options)
        self.ui.CoordinateButton.clicked.connect(self.enable_cvc_options)
        self.ui.ComputeButton.clicked.connect(self.ComputeTrajectories)
        self.ui.AnimateButton.clicked.connect(self.LaunchPlayer)
    def enable_cvc_options(self):
        self.ui.XYCheckBox.setEnabled(True)
        self.ui.XZCheckBox.setEnabled(True)
        self.ui.YZCheckBox.setEnabled(True)
        self.disable_vt_options()
    def disable_cvc_options(self):
        self.ui.XYCheckBox.setEnabled(False)
        self.ui.XZCheckBox.setEnabled(False)
        self.ui.YZCheckBox.setEnabled(False)
        self.ui.XYCheckBox.setChecked(False)
        self.ui.XZCheckBox.setChecked(False)
        self.ui.YZCheckBox.setChecked(False)
    def enable_vt_options(self):
        self.ui.CheckBoxX.setEnabled(True)
        self.ui.CheckBoxY.setEnabled(True)
        self.ui.CheckBoxZ.setEnabled(True)
        self.disable_cvc_options()
    def disable_vt_options(self):
        self.ui.CheckBoxX.setEnabled(False)
        self.ui.CheckBoxY.setEnabled(False)
        self.ui.CheckBoxZ.setEnabled(False)
        self.ui.CheckBoxX.setChecked(False)
        self.ui.CheckBoxY.setChecked(False)
        self.ui.CheckBoxZ.setChecked(False)
    def disable_2D_options(self):
        self.ui.TwoDOptionGroup.setExclusive(False)
        self.ui.CoordinateButton.setEnabled(False)
        self.ui.CoordinateButton.setChecked(False)
        self.ui.CoordinatevtButton.setEnabled(False)
        self.ui.CoordinatevtButton.setChecked(False)
        self.ui.PhaseButton.setEnabled(False)
        self.ui.PhaseButton.setChecked(False)
        self.ui.VelocityvtButton.setChecked(False)
        self.ui.VelocityvtButton.setEnabled(False)
        self.disable_cvc_options()
        self.disable_vt_options()
        self.ui.TwoDOptionGroup.setExclusive(True)
    def enable_2D_options(self):
        self.ui.CoordinateButton.setEnabled(True)
        self.ui.CoordinatevtButton.setEnabled(True)
        self.ui.PhaseButton.setEnabled(True)
        self.ui.VelocityvtButton.setEnabled(True)
    def throw_error(self,message):
        self.ErrorWindow = CustomError(message)
        self.ErrorWindow.show()    
    def ComputeTrajectories(self):
        self.set_all()
        #print(B_func_uniform_arbitrary(np.array([0.0,0.0,0.0]),0,self.fparams))
        time1 = time.time()
        self.qs,self.dqs,self.ts = SBPP.Integrator_Synched_nonRel(self.q0s,self.dq0s,E_func_uniform_arbitrary,B_func_uniform_arbitrary,
        self.masses,self.charges,self.dt,self.tf,self.fparams,output_Freq = 1)
        time2 = time.time()
        self.write_to_user("Completed computation; it took {:e} seconds".format(time2-time1))
        self.qs = np.array(self.qs)
        self.dqs = np.array(self.dqs)
    def LaunchPlayer(self):
        self.set_frequency()
        if self.ui.ThreeDButton.isChecked():
            self.PlayerWindow = Ui_PlayerWindow(figsize=self.figsize)
            self.PlayerWindow.set_data(self.qs,self.dqs,frequency = self.frequency,ts = self.ts)
            self.PlayerWindow.set_options(plot_traj = self.ui.FullTrajectoryButton.isChecked())
            self.PlayerWindow.show()
        elif self.ui.CoordinatevtButton.isChecked():
            if self.ui.CheckBoxX.isChecked():
                self.PlayerWindowXvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvt.set_data(self.qs[:,:,0],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvt.set_options(axis_labels=('t[s]','x[m]'))
                self.PlayerWindowXvt.show()
            if self.ui.CheckBoxY.isChecked():
                self.PlayerWindowYvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowYvt.set_data(self.qs[:,:,1],self.ts,ts=self.ts,frequency=self.frequency)
                self.PlayerWindowYvt.set_options(axis_labels=('t[s]','y[m]'))
                self.PlayerWindowYvt.show()
            if self.ui.CheckBoxZ.isChecked():
                self.PlayerWindowZvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowZvt.set_data(self.qs[:,:,2],self.ts,ts=self.ts,frequency=self.frequency)
                self.PlayerWindowZvt.set_options(axis_labels=('t[s]','z[m]'))
                self.PlayerWindowZvt.show()
        elif self.ui.PhaseButton.isChecked():
            if self.ui.CheckBoxX.isChecked():
                self.PlayerWindowXvVx = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvVx.set_data(self.qs[:,:,0],self.dqs[:,:,0],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvVx.set_options(axis_labels=('x[m]','v$_x$[m/s]'))
                self.PlayerWindowXvVx.show()
            if self.ui.CheckBoxY.isChecked():
                self.PlayerWindowXvVy = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvVy.set_data(self.qs[:,:,1],self.dqs[:,:,1],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvVy.set_options(axis_labels=('y[m]','v$_y$[m/s]'))
                self.PlayerWindowXvVy.show()
            if self.ui.CheckBoxZ.isChecked():
                self.PlayerWindowXvVz = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvVz.set_data(self.qs[:,:,2],self.dqs[:,:,2],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvVz.set_options(axis_labels=('y[m]','v$_y$[m/s]'))
                self.PlayerWindowXvVz.show()
        elif self.ui.VelocityvtButton.isChecked():
            if self.ui.CheckBoxX.isChecked():
                self.PlayerWindowVxvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowVxvt.set_data(self.dqs[:,:,0],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowVxvt.set_options(axis_labels=('t[s]','v$_x$[m/s]'))
                self.PlayerWindowVxvt.show()
            if self.ui.CheckBoxY.isChecked():
                self.PlayerWindowVyvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowVyvt.set_data(self.dqs[:,:,1],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowVyvt.set_options(axis_labels=('t[s]','v$_y$[m/s]'))
                self.PlayerWindowVyvt.show()
            if self.ui.CheckBoxZ.isChecked():
                self.PlayerWindowVzvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowVzvt.set_data(self.dqs[:,:,2],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowVzvt.set_options(axis_labels=('t[s]','v$_z$[m/s]'))
                self.PlayerWindowVzvt.show()
        elif self.ui.CoordinateButton.isChecked():
            if self.ui.XYCheckBox.isChecked():
                self.PlayerWindowXvY = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvY.set_data(self.qs[:,:,0],self.qs[:,:,1],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvY.set_options(axis_labels=('x[m]','y[m]'))
                self.PlayerWindowXvY.show()
            if self.ui.XZCheckBox.isChecked():
                self.PlayerWindowXvZ = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvZ.set_data(self.qs[:,:,0],self.qs[:,:,2],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvZ.set_options(axis_labels=('x[m]','z[m]'))
                self.PlayerWindowXvZ.show()
            if self.ui.YZCheckBox.isChecked():
                self.PlayerWindowYvZ = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowYvZ.set_data(self.qs[:,:,1],self.qs[:,:,2],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowYvZ.set_options(axis_labels=('y[m]','z[y]'))
                self.PlayerWindowYvZ.show()
    def write_to_user(self,message):
        self.ui.UserInfoLabel.setText(message)
    def set_all(self):
        try:
            self.set_charges()
            self.set_masses()
            self.set_initial_positions()
            self.set_initial_velocities()
            self.set_dt()
            self.set_field_strengths()
            self.set_tf()
            self.set_frequency()
            self.set_figoptions()
            self.write_to_user("Set all values; ready to compute.")
        except:
            self.throw_error("Make sure you have set all options correctly")
            self.write_to_user("Error; check format and data")
    def set_figoptions(self):
        user_input = self.ui.FigureSizeBox.text()
        user_input = np.fromstring(user_input, sep = ' ')
        self.figsize = (user_input[0],user_input[1])
    def set_frequency(self):
        self.frequency = self.ui.FrequencyBox.value()
    def set_charges(self):
        user_input = self.ui.ChargesEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep=' ')
            self.charges = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(user_input)
    def set_masses(self):
        user_input = self.ui.MassesEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep = ' ')
            self.masses = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
    def set_initial_positions(self):
        user_input = self.ui.PositionEntry.toPlainText()
        try:
            user_input = np.array(np.matrix(user_input))
            self.q0s = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(user_input)
    def set_initial_velocities(self):
        user_input = self.ui.VelocityEntry.toPlainText()
        try:
            user_input = np.array(np.matrix(user_input))
            self.dq0s = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(user_input)
    def set_field_strengths(self):
        user_input = self.ui.EFieldEntry.toPlainText()
        print(user_input)

        try:
            user_input = np.fromstring(user_input,sep=' ')
            self.fparams = (0,0,0,user_input[0],user_input[1],user_input[2])
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        #print(self.fparams)
    
    def set_dt(self):
        user_input = self.ui.dtEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep = ' ')
            self.dt = user_input[0]
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
    def set_tf(self):
        user_input = self.ui.tfEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep = ' ')
            self.tf = user_input[0]
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)

class EFieldSetupWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(EFieldSetupWindow,self).__init__()
        self.ui = Ui_UniformElectricSetup()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        ### Triggers for the buttons
        #self.ui.SetChargesButton.clicked.connect(self.set_charges)
        #self.ui.SetMassesButton.clicked.connect(self.set_masses)
        #self.ui.SetPositionsButton.clicked.connect(self.set_initial_positions)
        #self.ui.SetVelocitiesButton.clicked.connect(self.set_initial_velocities)
        #self.ui.SetFieldButton.clicked.connect(self.set_field_strengths)
        #self.ui.SetdtButton.clicked.connect(self.set_dt)
        #self.ui.SettfButton.clicked.connect(self.set_tf)
        self.ui.actionCommon_Values.triggered.connect(self.UsefulValues)
        #self.ui.DebugButton.clicked.connect(self.print_debug)
        self.ui.SetAllButton.clicked.connect(self.set_all)
        self.ui.TwoDButton.clicked.connect(self.enable_2D_options)
        self.ui.ThreeDButton.clicked.connect(self.disable_2D_options)
        self.ui.CoordinatevtButton.clicked.connect(self.enable_vt_options)
        self.ui.PhaseButton.clicked.connect(self.enable_vt_options)
        self.ui.VelocityvtButton.clicked.connect(self.enable_vt_options)
        self.ui.CoordinateButton.clicked.connect(self.enable_cvc_options)
        self.ui.ComputeButton.clicked.connect(self.ComputeTrajectories)
        self.ui.AnimateButton.clicked.connect(self.LaunchPlayer)
    def enable_cvc_options(self):
        self.ui.XYCheckBox.setEnabled(True)
        self.ui.XZCheckBox.setEnabled(True)
        self.ui.YZCheckBox.setEnabled(True)
        self.disable_vt_options()
    def disable_cvc_options(self):
        self.ui.XYCheckBox.setEnabled(False)
        self.ui.XZCheckBox.setEnabled(False)
        self.ui.YZCheckBox.setEnabled(False)
        self.ui.XYCheckBox.setChecked(False)
        self.ui.XZCheckBox.setChecked(False)
        self.ui.YZCheckBox.setChecked(False)
    def enable_vt_options(self):
        self.ui.CheckBoxX.setEnabled(True)
        self.ui.CheckBoxY.setEnabled(True)
        self.ui.CheckBoxZ.setEnabled(True)
        self.disable_cvc_options()
    def disable_vt_options(self):
        self.ui.CheckBoxX.setEnabled(False)
        self.ui.CheckBoxY.setEnabled(False)
        self.ui.CheckBoxZ.setEnabled(False)
        self.ui.CheckBoxX.setChecked(False)
        self.ui.CheckBoxY.setChecked(False)
        self.ui.CheckBoxZ.setChecked(False)
    def disable_2D_options(self):
        self.ui.TwoDOptionGroup.setExclusive(False)
        self.ui.CoordinateButton.setEnabled(False)
        self.ui.CoordinateButton.setChecked(False)
        self.ui.CoordinatevtButton.setEnabled(False)
        self.ui.CoordinatevtButton.setChecked(False)
        self.ui.PhaseButton.setEnabled(False)
        self.ui.PhaseButton.setChecked(False)
        self.ui.VelocityvtButton.setChecked(False)
        self.ui.VelocityvtButton.setEnabled(False)
        self.disable_cvc_options()
        self.disable_vt_options()
        self.ui.TwoDOptionGroup.setExclusive(True)
    def enable_2D_options(self):
        self.ui.CoordinateButton.setEnabled(True)
        self.ui.CoordinatevtButton.setEnabled(True)
        self.ui.PhaseButton.setEnabled(True)
        self.ui.VelocityvtButton.setEnabled(True)
    def throw_error(self,message):
        self.ErrorWindow = CustomError(message)
        self.ErrorWindow.show()    
    def ComputeTrajectories(self):
        self.set_all()
        
        try:
            time1 = time.time()
            self.qs,self.dqs,self.ts = SBPP.Integrator_Synched_nonRel(self.q0s,self.dq0s,E_func_uniform_arbitrary,B_func_zero,
        self.masses,self.charges,self.dt,self.tf,self.fparams,output_Freq = 1)
            time2 = time.time()
            self.write_to_user("Completed computation; it took {:e} seconds".format(time2-time1))
            self.qs = np.array(self.qs)
            self.dqs = np.array(self.dqs)
            self.ui.AnimateButton.setEnabled(True)
        except:
            self.throw_error("Something went wrong! Check all inputs and try again!")
            self.write_to_user("Computation failed!")
    def LaunchPlayer(self):
        self.set_frequency()
        if self.ui.ThreeDButton.isChecked():
            self.PlayerWindow = Ui_PlayerWindow(figsize=self.figsize)
            self.PlayerWindow.set_data(self.qs,self.dqs,frequency = self.frequency,ts = self.ts)
            self.PlayerWindow.set_options(plot_traj = self.ui.FullTrajectoryButton.isChecked())
            self.PlayerWindow.show()
        elif self.ui.CoordinatevtButton.isChecked():
            if self.ui.CheckBoxX.isChecked():
                self.PlayerWindowXvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvt.set_data(self.qs[:,:,0],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvt.set_options(axis_labels=('t[s]','x[m]'))
                self.PlayerWindowXvt.show()
            if self.ui.CheckBoxY.isChecked():
                self.PlayerWindowYvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowYvt.set_data(self.qs[:,:,1],self.ts,ts=self.ts,frequency=self.frequency)
                self.PlayerWindowYvt.set_options(axis_labels=('t[s]','y[m]'))
                self.PlayerWindowYvt.show()
            if self.ui.CheckBoxZ.isChecked():
                self.PlayerWindowZvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowZvt.set_data(self.qs[:,:,2],self.ts,ts=self.ts,frequency=self.frequency)
                self.PlayerWindowZvt.set_options(axis_labels=('t[s]','z[m]'))
                self.PlayerWindowZvt.show()
        elif self.ui.PhaseButton.isChecked():
            if self.ui.CheckBoxX.isChecked():
                self.PlayerWindowXvVx = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvVx.set_data(self.qs[:,:,0],self.dqs[:,:,0],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvVx.set_options(axis_labels=('x[m]','v$_x$[m/s]'))
                self.PlayerWindowXvVx.show()
            if self.ui.CheckBoxY.isChecked():
                self.PlayerWindowXvVy = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvVy.set_data(self.qs[:,:,1],self.dqs[:,:,1],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvVy.set_options(axis_labels=('y[m]','v$_y$[m/s]'))
                self.PlayerWindowXvVy.show()
            if self.ui.CheckBoxZ.isChecked():
                self.PlayerWindowXvVz = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvVz.set_data(self.qs[:,:,2],self.dqs[:,:,2],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvVz.set_options(axis_labels=('y[m]','v$_y$[m/s]'))
                self.PlayerWindowXvVz.show()
        elif self.ui.VelocityvtButton.isChecked():
            if self.ui.CheckBoxX.isChecked():
                self.PlayerWindowVxvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowVxvt.set_data(self.dqs[:,:,0],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowVxvt.set_options(axis_labels=('t[s]','v$_x$[m/s]'))
                self.PlayerWindowVxvt.show()
            if self.ui.CheckBoxY.isChecked():
                self.PlayerWindowVyvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowVyvt.set_data(self.dqs[:,:,1],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowVyvt.set_options(axis_labels=('t[s]','v$_y$[m/s]'))
                self.PlayerWindowVyvt.show()
            if self.ui.CheckBoxZ.isChecked():
                self.PlayerWindowVzvt = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowVzvt.set_data(self.dqs[:,:,2],self.ts,ts = self.ts,frequency = self.frequency)
                self.PlayerWindowVzvt.set_options(axis_labels=('t[s]','v$_z$[m/s]'))
                self.PlayerWindowVzvt.show()
        elif self.ui.CoordinateButton.isChecked():
            if self.ui.XYCheckBox.isChecked():
                self.PlayerWindowXvY = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvY.set_data(self.qs[:,:,0],self.qs[:,:,1],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvY.set_options(axis_labels=('x[m]','y[m]'))
                self.PlayerWindowXvY.show()
            if self.ui.XZCheckBox.isChecked():
                self.PlayerWindowXvZ = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowXvZ.set_data(self.qs[:,:,0],self.qs[:,:,2],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowXvZ.set_options(axis_labels=('x[m]','z[m]'))
                self.PlayerWindowXvZ.show()
            if self.ui.YZCheckBox.isChecked():
                self.PlayerWindowYvZ = Ui_PlayerWindow2D(figsize=self.figsize)
                self.PlayerWindowYvZ.set_data(self.qs[:,:,1],self.qs[:,:,2],ts = self.ts,frequency = self.frequency)
                self.PlayerWindowYvZ.set_options(axis_labels=('y[m]','z[y]'))
                self.PlayerWindowYvZ.show()
    def write_to_user(self,message):
        self.ui.UserInfoLabel.setText(message)
    def set_all(self):
        try:
            self.set_charges()
            self.set_masses()
            self.set_initial_positions()
            self.set_initial_velocities()
            self.set_dt()
            self.set_field_strengths()
            self.set_tf()
            self.set_frequency()
            self.set_figoptions()
            self.write_to_user("Set all values; ready to compute.")
        except:
            self.throw_error("Format error; check all boxes and try again")
            self.write_to_user("Failed; correct errors")
    def set_figoptions(self):
        user_input = self.ui.FigureSizeBox.text()
        user_input = np.fromstring(user_input, sep = ' ')
        self.figsize = (user_input[0],user_input[1])
    def set_frequency(self):
        self.frequency = self.ui.FrequencyBox.value()
    def set_charges(self):
        user_input = self.ui.ChargesEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep=' ')
            self.charges = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(user_input)
    def set_masses(self):
        user_input = self.ui.MassesEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep = ' ')
            self.masses = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
    def set_initial_positions(self):
        user_input = self.ui.PositionEntry.toPlainText()
        try:
            user_input = np.array(np.matrix(user_input))
            self.q0s = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(user_input)
    def set_initial_velocities(self):
        user_input = self.ui.VelocityEntry.toPlainText()
        try:
            user_input = np.array(np.matrix(user_input))
            self.dq0s = user_input
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        print(user_input)
    def set_field_strengths(self):
        user_input = self.ui.EFieldEntry.toPlainText()
        print(user_input)

        try:
            user_input = np.fromstring(user_input,sep=' ')
            self.fparams = (user_input[0],user_input[1],user_input[2])
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
        #print(self.fparams)
    def UsefulValues(self):
        self.usefulValWindow = EUniformValues()
        self.usefulValWindow.show()
    def print_debug(self):
        #print(self.tf,self.dt,self.fparams,self.dq0s,self.q0s)
        message = "Cats"
        self.throw_error(message)
        print(self.dt)
        #print("Debug")
    def set_dt(self):
        user_input = self.ui.dtEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep = ' ')
            self.dt = user_input[0]
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
    def set_tf(self):
        user_input = self.ui.tfEntry.toPlainText()
        try:
            user_input = np.fromstring(user_input,sep = ' ')
            self.tf = user_input[0]
        except:
            error_text = "Incorrect format used"
            self.throw_error(error_text)
def main():
    app = QtWidgets.QApplication(sys.argv)
    StartMenu = MainMenu()
    #EFieldSetupMenu = EFieldSetupWindow()
    #StartMenu.ui.DebugPush.clicked.connect(EFieldSetupMenu.show())
    StartMenu.show()
    sys.exit(app.exec_())
if __name__=='__main__':
    main()
    