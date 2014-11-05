# -*- coding: utf-8 -*-
"""
Created on Wed Nov 05 10:50:37 2014

@author: FPopecarter
"""
#import core modules
import os
import sys
import glob
import numpy as np
import re
import atexit
import shutil

#Import GUI related modules
from PyQt4 import QtCore
from PyQt4 import QtGui
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar
# For creating simple dialogs
from formlayout import fedit

# import the MainWindow widget from the converted .ui files
from GUI.MainUI import Ui_MainWindow

#Imports button related tools
#from includes.Buttons import Button_Definitions

class ModellerMainWindow(QtGui.QMainWindow, Ui_MainWindow):
    """Customization for Qt Designer created window"""
    
    def definitions(self):
        self.s3 = ""
        self.bucket = ""
        self.project_code = ""
        self.overwrite = False
        self.file_list = ""
        self.tempfile = ""
    
    def cleanup(self):
        print 'closing'

    
    def enable_2DRes(self):
        #Enable / Disable relevant survey Parameters
        self.doubleSpinBox_traverselength.setEnabled(True)
        self.doubleSpinBox_samplingint.setEnabled(True)
        
        self.doubleSpinBox_traverseint.setDisabled(True)
        self.doubleSpinBox_fieldinclination.setDisabled(True)
        
        #Enable / Disable instrument parameters
        self.comboBox_array.setEnabled(True)        
        self.doubleSpinBox_a.setEnabled(True)
        self.doubleSpinBox_a1.setEnabled(True)
        self.doubleSpinBox_a2.setEnabled(True)
        
        self.doubleSpinBox_lowersensor.setDisabled(True)
        self.doubleSpinBox_uppersensor.setDisabled(True)
        
        #Enable / Disable Feature Parameters
        self.comboBox_conductivity.setEnabled(True)
        self.doubleSpinBox_depth.setEnabled(True)
        
        self.doubleSpinBox_magsus.setDisabled(True)
        self.doubleSpinBox_length.setDisabled(True)
        self.doubleSpinBox_width.setDisabled(True)
        self.doubleSpinBox_strike.setDisabled(True)
        self.doubleSpinBox_depthextent.setDisabled(True)
        
        #Modifys ComboBox
        self.comboBox_array.clear()
        self.comboBox_array.addItems(('TP Long','TP Broad','W Long','W Broad','SQ Alpha','SQ Beta', 'SQ Gamma', 'TZ Long', 'TZ Broad', 'TZ Theta'))
        
    def enable_3DRes(self):
        #Enable / Disable relevant survey Parameters
        self.doubleSpinBox_traverselength.setEnabled(True)
        self.doubleSpinBox_traverseint.setEnabled(True)
        self.doubleSpinBox_samplingint.setEnabled(True)
        
        self.doubleSpinBox_fieldinclination.setDisabled(True)
        
        #Enable / Disable instrument parameters
        self.comboBox_array.setEnabled(True)
        self.doubleSpinBox_a.setEnabled(True)
        self.doubleSpinBox_a1.setEnabled(True)
        self.doubleSpinBox_a2.setEnabled(True)
        
        self.doubleSpinBox_lowersensor.setDisabled(True)
        self.doubleSpinBox_uppersensor.setDisabled(True)
        
        #Enable / Disable Feature Parameters
        self.comboBox_conductivity.setEnabled(True)
        self.doubleSpinBox_depth.setEnabled(True)
        self.doubleSpinBox_length.setEnabled(True)
        self.doubleSpinBox_width.setEnabled(True)
        self.doubleSpinBox_depthextent.setEnabled(True)
        
        self.doubleSpinBox_magsus.setDisabled(True)
        self.doubleSpinBox_strike.setDisabled(True)
        
        #Modifys ComboBox
        self.comboBox_array.clear()
        self.comboBox_array.addItems(('TP Long','TP Broad','W Long','W Broad','SQ Alpha','SQ Beta', 'SQ Gamma', 'TZ Long', 'TZ Broad', 'TZ Theta'))
        
    def enable_3DMag(self):
        #Enable / Disable relevant survey Parameters
        self.doubleSpinBox_traverselength.setEnabled(True)
        self.doubleSpinBox_traverseint.setEnabled(True)
        self.doubleSpinBox_samplingint.setEnabled(True)
        self.doubleSpinBox_fieldinclination.setEnabled(True)
        
        #Enable / Disable instrument parameters
        self.comboBox_array.setEnabled(True)
        self.doubleSpinBox_lowersensor.setEnabled(True)
        self.doubleSpinBox_uppersensor.setEnabled(True)
        
        self.doubleSpinBox_a.setDisabled(True)
        self.doubleSpinBox_a1.setDisabled(True)
        self.doubleSpinBox_a2.setDisabled(True)
        
        #Enable / Disable Feature Parameters
        self.doubleSpinBox_depth.setEnabled(True)
        self.doubleSpinBox_length.setEnabled(True)
        self.doubleSpinBox_width.setEnabled(True)
        self.doubleSpinBox_depthextent.setEnabled(True)
        self.doubleSpinBox_magsus.setEnabled(True)
        self.doubleSpinBox_strike.setEnabled(True)
        
        self.comboBox_conductivity.setDisabled(True)
        
        #Modifys ComboBox
        self.comboBox_array.clear()
        self.comboBox_array.addItems(('Vertical', 'Total', 'Horizontal X', 'Horizontal Y'))
        
    def enable_2DMag(self):
        #Enable / Disable relevant survey Parameters
        self.doubleSpinBox_traverselength.setEnabled(True)
        self.doubleSpinBox_traverseint.setEnabled(True)
        self.doubleSpinBox_samplingint.setEnabled(True)
        self.doubleSpinBox_fieldinclination.setEnabled(True)
        
        #Enable / Disable instrument parameters
        self.comboBox_array.setEnabled(True)
        self.doubleSpinBox_lowersensor.setEnabled(True)
        self.doubleSpinBox_uppersensor.setEnabled(True)
        
        self.doubleSpinBox_a.setDisabled(True)
        self.doubleSpinBox_a1.setDisabled(True)
        self.doubleSpinBox_a2.setDisabled(True)
        
        #Enable / Disable Feature Parameters
        self.doubleSpinBox_depth.setEnabled(True)
        self.doubleSpinBox_length.setEnabled(True)
        self.doubleSpinBox_width.setEnabled(True)
        self.doubleSpinBox_depthextent.setEnabled(True)
        self.doubleSpinBox_magsus.setEnabled(True)
        self.doubleSpinBox_strike.setEnabled(True)
        
        self.comboBox_conductivity.setDisabled(True)
        
        #Modifys ComboBox
        self.comboBox_array.clear()
        self.comboBox_array.addItems(('Vertical', 'Total', 'Horizontal X', 'Horizontal Y'))
        
    def tar_data_files(self, output_name, files):
        if not os.path.isfile(output_name):
            tar = tarfile.open(output_name, "w:gz")
            for name in files:
                arcname = os.path.basename(name)
                tar.add(name,arcname=arcname)
            tar.close()  
        
    def put_file(self, file_path, cloud_path):
        k = Key(self.bucket)
        string = str(self.project_code) + '/' + cloud_path
        print string
        if self.bucket.get_key(string) == None or self.overwrite:
            k.key = string
            k.set_contents_from_filename(file_path)
            

        
    def Warning_Dialog(self, title, text):
        message = QtGui.QMessageBox.warning(self,str(title),str(text))
        
    def display_points(self, x, y):
        print 'display updating with Northings/Eastings'
#        self.Eastings = GPSMainWindow.data[:,1]
#        self.Northings = GPSMainWindow.data[:,0]
        self.mpl.canvas.ax.clear()
        self.mpl.canvas.ax.axis('equal')
        print 'canvas cleared'
        print len(x), 'points'
        self.mpl.canvas.ax.plot(x,y, 'o', ms=1, color='black')
         # reset the axes limits
        self.mpl.canvas.ax.set_xlim(xmin=np.min(x), xmax=(np.max(x)))
        self.mpl.canvas.ax.set_ylim(ymin=np.min(y), ymax=(np.max(y)))
        self.mpl.canvas.ax.grid(True)
        self.mpl.canvas.draw()
        print 'canvas drawn'
        
    def display_b_points(self):
        print 'display updating with Northings/Eastings'
#        self.Eastings = GPSMainWindow.data[:,1]
#        self.Northings = GPSMainWindow.data[:,0]
        self.mpl.canvas.ax.clear()
        self.mpl.canvas.ax.axis('equal')
        print 'canvas cleared'
        self.mpl.canvas.ax.plot(self.sens1[:,1],self.sens1[:,2], 'o', ms=1, color='red')
        self.mpl.canvas.ax.plot(self.sens2[:,1],self.sens2[:,2], 'o', ms=1, color='blue')
        self.mpl.canvas.ax.plot(self.sens3[:,1],self.sens3[:,2], 'o', ms=1, color='green')
        self.mpl.canvas.ax.plot(self.sens4[:,1],self.sens4[:,2], 'o', ms=1, color='yellow')
         # reset the axes limits
        #self.mpl.canvas.ax.set_xlim(xmin=np.min(self.sens1[:,1]), xmax=(np.max(self.sens1[:,1])))
        #self.mpl.canvas.ax.set_ylim(ymin=np.min(self.sens1[:,2]), ymax=(np.max(self.sens1[:,2])))
        self.mpl.canvas.ax.grid(True)
        self.mpl.canvas.draw()
        print 'canvas drawn'  
        
    def MagRes2D3Dtoggle(self):
        print 'Toggled'
        
        if self.radioButton_mag.isChecked():
            if self.radioButton_2d.isChecked():
                self.enable_2DMag()
            else:
                self.enable_3DMag()
        else:
            if self.radioButton_2d.isChecked():
                self.enable_2DRes()
            else:
                self.enable_3DRes()
                
        print self.radioButton_mag.isChecked(),self.radioButton_res.isChecked()
        
        
    def Button_Definitions(self):
        self.firstrun=True        
        QtCore.QObject.connect(self.radioButton_mag, QtCore.SIGNAL("toggled(bool)"), self.MagRes2D3Dtoggle)
        QtCore.QObject.connect(self.radioButton_2d, QtCore.SIGNAL("toggled(bool)"), self.MagRes2D3Dtoggle)
        # Buttons in Toolbar
        #self.push_put_data.clicked.connect(self.put_cloud_data)
        #self.push_load_field.clicked.connect(self.load_field)
        #self.Push_cor_GNSS.clicked.connect(self.load_cloud_points)
        #self.Push_cor_GNSS.clicked.connect(self.Process_GNSS)
        #self.Push_display_barty_points.clicked.connect(self.calculate_barty_locs)
#        self.Push_Desample.clicked.connect(self.remove_collinears)
#        self.Push_Greyscale.clicked.connect(self.Grid_Data)
#        self.Push_ZMT.clicked.connect(self.ZMT)
#        self.Push_Calibrate.clicked.connect(self.calibrate)      
#        self.Push_Despike.clicked.connect(self.Despike)
        
#        self.Push_Export.clicked.connect(self.import_NMEA)
        
        # Buttons in Menu
#        self.actionOpen_File.triggered.connect(self.data_SourceFile)
#        self.actionDisplay_GreyScale.triggered.connect(self.Grid_Data)
        #QtCore.QObject.connect(self.mplactionQuit, QtCore.SIGNAL('triggered()'), QtGui.qApp, QtCore.SLOT("quit()"))
    
    
    def __init__(self, parent = None):
        # initialization of the superclass
        super(ModellerMainWindow, self).__init__(parent)
        # setup the GUI --> function generated by pyuic4
        self.setupUi(self)
        #Adds a Matplotlib Toolbar to the display, clears the display and adds only the required buttons
        self.navi_toolbar = NavigationToolbar(self.mpl.canvas, self)
        self.navi_toolbar.clear()
        
 # Add the x,y location widget at the right side of the toolbar
 # The stretch factor is 1 which means any resizing of the toolbar
 # will resize this label instead of the buttons.
#        self.navi_toolbar.locLabel = QtGui.QLabel( "", self )
#        self.navi_toolbar.locLabel.setAlignment(QtCore.Qt.AlignLeft)
#        self.navi_toolbar.locLabel.setSizePolicy(
#        QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,
#                           QtGui.QSizePolicy.Expanding))
#        labelAction = self.navi_toolbar.addWidget(self.navi_toolbar.locLabel)
#        labelAction.setVisible(True)
#Adds Buttons
        #a = self.navi_toolbar.addAction(self.navi_toolbar._icon('home.png'), 'Home',
        #                                self.navi_toolbar.home)
        #a.setToolTip('returns axes to original position')
        a = self.navi_toolbar.addAction(self.navi_toolbar._icon('move.png'), 'Pan',
                                        self.navi_toolbar.pan)
        a.setToolTip('Pan axes with left mouse, zoom with right')
        a = self.navi_toolbar.addAction(self.navi_toolbar._icon('zoom_to_rect.png'), 'Zoom',
                                        self.navi_toolbar.zoom)
        a.setToolTip('Zoom to Rectangle')
        a = self.navi_toolbar.addAction(self.navi_toolbar._icon('filesave.png'), 'Save',
                           self.navi_toolbar.save_figure)
        a.setToolTip('Save the figure')

        #Button_layout is a QT desginer Grid Layout.
        self.toolbar_grid.addWidget(self.navi_toolbar)
        self.Button_Definitions()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    
    app.processEvents()
    
    #Creates Window Form     
    form = ModellerMainWindow()
    
    #display form and focus
    form.show()
    #if sys.platform == "darwin":
    form.raise_()
    
    #Something to do with the App & Cleanup?
    app.exec_()
    atexit.register(form.cleanup)