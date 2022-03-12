from email.mime import image
from tkinter import *
from tkinter import ttk
import tkinter.font as font
from tkinter import filedialog
from turtle import color
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
pencere = Tk()
pencere.resizable(False,False)
pencere.title('1190505036_Kadir_Sahin')
pencere.geometry("300x250")
FontOzellik = font.Font(family='Ariel', size=11, weight='bold')
def DosyaSecmeKomut():
    dugme5.destroy()
    filename = filedialog.askopenfilename(initialdir= "/", title="Select File")
    image = cv.imread(filename)
    kernel2 = np.ones((5, 5), np.float32)/25
    img = cv.filter2D(src=image, ddepth=-1, kernel=kernel2)
    AveragingBlur=cv.blur(img,(20,20))
    MedianBlur= cv.medianBlur(img,9) 
    GaussianBlurring= cv.GaussianBlur(img,(11,11),150)
    BilateralFilter = cv.bilateralFilter(img,18,100,100)

    def BilateralFilterKomut():
        #ekstra gosterim
        '''cv.imshow("Orjinal",img,)
        cv.imshow("BilateralFilter",BilateralFilter,)'''
        
        plt.subplot(121),plt.imshow(img),plt.title('Original Resim')
        plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(BilateralFilter),plt.title('Bilateral Filter Resim')
        plt.xticks([]), plt.yticks([])
        plt.show()
    def AveragingBlurKomut():
        #ekstra gosterim
        '''cv.imshow("Orjinal",img,)
        cv.imshow("AveragingBlur",AveragingBlur,)'''

        plt.subplot(121),plt.imshow(img),plt.title('Original Resim')
        plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(AveragingBlur),plt.title('Averaging Blur Resim')
        plt.xticks([]), plt.yticks([])
        plt.show()
    def MedianBlurKomut():
        #ekstra gosterim
        '''cv.imshow("Orjinal",img,)
        cv.imshow("MedianBlur",MedianBlur,)'''

        plt.subplot(121),plt.imshow(img),plt.title('Original Resim')
        plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(MedianBlur),plt.title('Median Blur Resim')
        plt.xticks([]), plt.yticks([])
        plt.show()
    def GaussianBlurringKomut():
        #ekstra gosterim
        '''cv.imshow("Orjinal",img,)
        cv.imshow("GaussianBlurring",GaussianBlurring,)'''

        plt.subplot(121),plt.imshow(img),plt.title('Original Resim')
        plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(GaussianBlurring),plt.title('Gaussian Blurring Resim')
        plt.xticks([]), plt.yticks([])
        plt.show()
    dugme1 = Button(pencere,width=20,height=2,bg="#a868ed",text="Averaging Blur",command=AveragingBlurKomut)
    dugme1['font'] = FontOzellik
    dugme1.pack()
    dugme2 = Button(pencere,width=20,height=2,bg="#a868ed",text="Median Blur",command=MedianBlurKomut)
    dugme2['font'] = FontOzellik
    dugme2.pack()
    dugme3 = Button(pencere,width=20,height=2,bg="#a868ed",text="Gaussian Blurring",command=GaussianBlurringKomut)
    dugme3['font'] = FontOzellik
    dugme3.pack()
    dugme4 = Button(pencere,width=20,height=2,bg="#a868ed",text="Bilateral Filter",command=BilateralFilterKomut)
    dugme4['font'] = FontOzellik
    dugme4.pack()
    cv.waitKey(0)
    cv.destroyAllWindows()
dugme5 = Button(pencere,width=20,height=2,bg="#9c5fde",text="Resim Sec",command=DosyaSecmeKomut)
pencere['background']='#442763'
dugme5['font'] = FontOzellik
dugme5.pack()
pencere.mainloop()