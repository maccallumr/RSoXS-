##MacCallum Robertson 6/14/2016

import sys
import scipy
import gdal
import matplotlib.pyplot as plt
import Image
from PySide import QtCore, QtGui
from PySide.QtGui import *
from PySide.QtCore import QTimer, SIGNAL, SLOT
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3
from mpl_toolkits.mplot3d import Axes3D
from numpy import trapz

import glob
import os
from sys import argv
from astropy.io import fits as pyfits
from astropy.table import Table, Column

fits_im=[]
fits_im = os.listdir("./")
fits_im.sort()


app =QApplication.instance()

if not app:
    app = QApplication(sys.argv)
    
w = QWidget()

#Window#
w.resize(250,300)
w.setWindowTitle('FImView')

button1= QPushButton('Load Fits Images',w)
button1.setToolTip('Load fits images from file named "fits"')
button1.resize(button1.sizeHint())
button1.move(30,50)

button2= QPushButton('Make Header File',w)
button2.setToolTip('Makes a file containing information from the file header')
button2.resize(button2.sizeHint())
button2.move(30,90)



options=QComboBox(w)
options.resize(150,20)
options.move(30,160)
options.show()

textbox1 = QLineEdit(w)
textbox1.move(240, 35)
textbox1.resize(50, 20)
textbox1.setText('                                                        ')
textbox1.hide()

textbox_store = QLineEdit(w)
textbox_store.move(240, 35)
textbox_store.resize(50, 20)
textbox_store.setText('                                                        ')
textbox_store.hide()

label1 = QLabel(w)
label1.setText('Fits Image Viewer')
label1.move(30, 20)
label1.show()

button3= QPushButton('Prev',w)
button3.setToolTip('Makes a file containing information from the file header')
button3.resize(button3.sizeHint())
button3.move(30,250)
button3.hide()

button4= QPushButton('Next',w)
button4.setToolTip('Makes a file containing information from the file header')
button4.resize(button4.sizeHint())
button4.move(130,250)
button4.hide()

label3 = QLabel(w)
label3.setText('Select Image File')
label3.move(30, 130)
label3.hide()

label2 = QLabel(w)
label2.setText('                                       ')
label2.move(30, 210)
label2.hide()

label1 = QLabel(w)
label1.setText('File Path:')
label1.move(30, 190)
label1.hide()

def on_click_button1():
    
    label3.show()
    button3.show()
    button4.show()

    count=0
    for i in range(0,len(fits_im)):
        if fits_im[i].endswith('.fits'):
            options.addItem(str(i)+":"+str(fits_im[i]))
            options.show()
        else:
            count=count+1
 
def on_click_button2(): 
    name=textbox1.text()
    
    picname=name+'.dat'
    
    dir = "./"
    indexed_image=dir+name+'.fits'
    
    #fitsNames=[]
    #for fitsName in glob.glob(dir+'*.fits'):
    #        fitsNames.append(fitsName)
    fits_header(picname,indexed_image)      
    
def on_click_button3(): 
    if textbox_store.text()=='':
        index=0
    else:
        index=textbox_store.text()
        
    index=int(index)
   
    
    for g in range(index-1,-1,-1):
        if fits_im[g].endswith('.fits'):
            new_index=g
            break
       
    index=int(new_index)
  


    loaded_im=pyfits.open(fits_im[index])
    plt.imshow(loaded_im[2].data) 
    plt.colorbar()
    plt.title('RSoXS Scattering')
    pic=fits_im[index][0:-5]
    plt.savefig(pic+'.png')
    plt.close()
    
    textbox_store.setText(str(index))
    label1.show()
    
    
    label2.setText(fits_im[index])
    label2.show()
    
    textbox1.setText(pic)
    
    w.resize(1100,600)
    image=QImage(pic+'.png')
    pixmap=QPixmap.fromImage(image)
    pixmap=pixmap.scaled(700,700,QtCore.Qt.KeepAspectRatio)
    imagelabel=QLabel(w)
    imagelabel.setPixmap(pixmap)
    imagelabel.move(300,30)
    ##imagelabel.resize(100,100)
    imagelabel.setScaledContents(True)
    imagelabel.show()

    

def on_click_button4(): 
    
    if textbox_store.text()=='':
        index=0
    else:
        index=textbox_store.text()
    index=int(index)
    
    
    for g in range(index+1,300):
        if fits_im[g].endswith('.fits'):
            new_index=g
            break
        
    index=int(new_index)
    print index
 
    loaded_im=pyfits.open(fits_im[index])
    plt.imshow(loaded_im[2].data) 
    plt.colorbar()
    plt.title('RSoXS Scattering')
    pic=fits_im[index][0:-5]
    plt.savefig(pic+'.png')
    plt.close()
    
    
    textbox_store.setText(str(index))
    label1.show()
    
    
    label2.setText(fits_im[index])
    label2.show()
    
    textbox1.setText(pic)
    
    w.resize(1100,600)
    image=QImage(pic+'.png')
    pixmap=QPixmap.fromImage(image)
    pixmap=pixmap.scaled(700,700,QtCore.Qt.KeepAspectRatio)
    imagelabel=QLabel(w)
    imagelabel.setPixmap(pixmap)
    imagelabel.move(300,30)
    ##imagelabel.resize(100,100)
    imagelabel.setScaledContents(True)
    imagelabel.show()      

    
def on_activated(text):
    text_str=str(text)
    
    
    if text_str[3]==':':
        index=int(text_str[:3])
    elif text_str[2]==':':
        index=int(text_str[:2])
    else:
        index=int(text_str[0])
    #if len(text_str)>1:
    #    index=int(text_str[:3])
    #else:
    #    index=int(text_str[0])
    textbox_store.setText(str(index))
    
    loaded_im=pyfits.open(fits_im[index])
    plt.imshow(loaded_im[2].data) 
    plt.colorbar()
    plt.title('RSoXS Scattering')
    pic=fits_im[index][0:-5]
    plt.savefig(pic+'.png')
    plt.close()
    
  
    label1.show()

    label2.setText(fits_im[index])
    label2.show()
    
    textbox1.setText(pic)
    
    w.resize(1100,600)
    image=QImage(pic+'.png')
    pixmap=QPixmap.fromImage(image)
    pixmap=pixmap.scaled(700,700,QtCore.Qt.KeepAspectRatio)
    imagelabel=QLabel(w)
    imagelabel.setPixmap(pixmap)
    imagelabel.move(300,30)
    #imagelabel.resize(100,100)
    imagelabel.setScaledContents(True)
    imagelabel.show()
    
    
 
options.activated[str].connect(on_activated)

button1.clicked.connect(on_click_button1) 
button2.clicked.connect(on_click_button2)  
button3.clicked.connect(on_click_button3) 
button4.clicked.connect(on_click_button4) 

def fits_header(picname,indexed_image):
    

    keys0 = ['SIMPLE', 'BITPIX', 'NAXIS','EXTEND', 'COMMENT','EXPOSURE', 'TEMP', 'RINGCRNT','DATE', 'Piezo Vertical','Sample X', 'Sample Y', 'Sample Z','Sample Theta', 'Sample Y Scaled','CCD Theta', 'Beam Stop', 'Pollux CCD X','Pollux CCD Y', 'CCD Temperature Setpoint','T-2T', 'Beamline Energy', 'Beamline Energy Goal','Exit Slit Left', 'Exit Slit Right','Horizontal Exit Slit Size', 'Horizontal Exit Slit Position', 'Vertical Exit Slit Size','Vertical Exit Slit Position', 'EPU Gap','EPU Z', 'Mono Energy', 'EPU Polarization','M103 Yaw', 'M103 Bend Up','M103 Bend Down', 'M101 Feedback', 'M101 Horizontal Deflection','M101 Vertical Deflection', 'Vertical Slit Position','Vertical Slit Size', 'Horizontal Slit Position', 'Mono 101 Vessel','Horizontal Slit Size', 'filterTi-Au','M121 Translation', 'Higher Order Suppressor', 'AO 0','AO 1', 'In Vacuum Slit Bottom','In Vacuum Slit Top', 'In Vacuum Slit Left', 'In Vacuum Slit Right','OSP Adjustment', 'CCD Shutter Inhibit','Temperature Controller', 'Upstream JJ Vert Aperture', 'Upstream JJ Vert Aperture','Upstream JJ Horz Trans', 'In-Chamber JJ Vert Aperture','In-Chamber JJ Vert Trans', 'In-Chamber JJ Horz Aperture', 'In-Chamber JJ Horz Trans','Middle JJ Vert Trans', 'CCD Temperature','Beam Current', 'TEY signal', 'IZERO','Photodiode', 'AI 0','AI 3 Izero', 'AI 5', 'AI 6 BeamStop','AI 7', 'COUNTER']
    keys1 = ['BITPIX','NAXIS','NAXIS1','NAXIS2','PCOUNT','GCOUNT','TFIELDS','EXTNAME','TTYPE1','TFORM1']
    keys2 = ['BITPIX','NAXIS','NAXIS1','NAXIS2','PCOUNT','GCOUNT','BZERO','BSCALE','EXTNAME']
    for i in range(0,3):
        values=[]
        hdu = i
        
            
        if i==0:
            
            header = pyfits.getheader(indexed_image, hdu)
            values.append([header.get(key) for key in keys0])
            newval=values[0]
        
            fil=open(picname,'a')
            for i in range(0, len(newval)):
                fil.write(keys0[i]+":"+str(newval[i]))
                fil.write("\n")
            fil.close()
        if i==1:
            
            header = pyfits.getheader(indexed_image, hdu)
            values.append([header.get(key) for key in keys1])    
            newval=values[0]
        
            fil=open(picname,'a')
            for i in range(0, len(newval)):
                fil.write('BINTABLE-' + keys1[i]+":"+str(newval[i]))
                fil.write("\n")
            fil.close()
        if i==2:
            
            header = pyfits.getheader(indexed_image, hdu)
            values.append([header.get(key) for key in keys2])   
            newval=values[0]
        
            fil=open(picname,'a')
            for i in range(0, len(newval)):
                fil.write('IMAGE-' + keys2[i]+":"+str(newval[i]))
                fil.write("\n")
            fil.close()
        
  
       
w.show()
sys.exit(app.exec_())
