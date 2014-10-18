# -*- coding: utf-8 –*-
#------------------------------------------------------------------------------------------
from Tkinter import *
import tkMessageBox
#-----------------------------------------------------------------------------------------
class APP:
    #------------------------------------------------------------------------------------------
    def __init__(self):
        root = Tk()    
        root.title("program")
        root.geometry('600x300+200+100')
            
        #widjet
        label = Label(root, text='한글')
        label.pack(side='left')
        
        self.txt1 = Entry(root)       
        self.txt1.pack()
    
        btn1 = Button(root,text="click",fg="blue",width=20,height=3,command=self.getVal).pack()
    
        root.mainloop();
    #----------------------------------------------------------------------------------------    
    def getVal(self):
        msg = self.txt1.get()
        self.alert(msg)
    #----------------------------------------------------------------------------------------    
    def log(self):
        f = open('D:/log.log','a')
        f.write('abcde111\r\n')
    #------------------------------------------------------------------------------------------
    def alert(self,msg):
        tkMessageBox.showinfo('notice',msg)     

#--------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app = APP()
    
    