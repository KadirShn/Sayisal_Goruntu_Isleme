from contextlib import closing
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
kerneldeger=0
Foto = cv.imread('C:/Users/shnka/Desktop/1190505036KadirSahin/8.jpg',0)
deger = 0
def MetodFonk(value):
    global deger
    deger = value
    kernel= np.ones((kerneldeger,kerneldeger),np.uint8)
    ErosionAsindir = cv.erode(Foto,kernel,iterations=1)
    DilationYayma = cv.dilate(Foto,kernel,iterations=1)
    OpenningAcma = cv.morphologyEx(Foto,cv.MORPH_OPEN,kernel)
    ClosingKapama = cv.morphologyEx(Foto,cv.MORPH_CLOSE,kernel)
    GradientGradyan = cv.morphologyEx(Foto,cv.MORPH_GRADIENT,kernel)
    TopHat = cv.morphologyEx(Foto,cv.MORPH_TOPHAT,kernel)
    BlackHat = cv.morphologyEx(Foto,cv.MORPH_BLACKHAT,kernel)
    if deger ==0:
        res=np.hstack((Foto,Foto))
    elif deger ==1:
        res=np.hstack((Foto,ErosionAsindir))
    elif deger ==2:
        res=np.hstack((Foto,DilationYayma))
    elif deger ==3:
        res=np.hstack((Foto,OpenningAcma))
    elif deger ==4:
        res=np.hstack((Foto,ClosingKapama))
    elif deger ==5:
        res=np.hstack((Foto,GradientGradyan))
    elif deger ==6:
        res=np.hstack((Foto,TopHat))
    elif deger ==7:
        res=np.hstack((Foto,BlackHat)) 
    cv.imshow("pencere",res)      
def KernelFonk(value):
    global kerneldeger
    kerneldeger = value
    MetodFonk(deger)
cv.namedWindow('pencere')
cv.createTrackbar('Kernel', "pencere", 1, 20, lambda a: KernelFonk(a))
cv.createTrackbar('Metod', "pencere", 1, 7, lambda a: MetodFonk(a))  
cv.waitKey(0)
cv.destroyAllWindows()