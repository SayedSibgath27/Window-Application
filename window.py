#Front end tool in python-pyqt, flask, tkinter.
#import pandas
#from pandas import*
import pandas as pd 
from tkinter import*
from tkinter.filedialog import askopenfilename
def uploadfile():
    #Open the dialoge box
    path=askopenfilename(initialdir="",
                         filetypes=(("txtfile","*.txt"),("allfile","*.*")),
                         title="choose a file")
    print(path)
    #data=pd.read_excel(path)
    #print(data)
    #file=open(path,"r")
    #content=file.read()
    #print(content)
    #data=pd.read_csv(path)
    #print(data)
    data=pd.read_csv("https://data.covid19india.org/csv/latest/states.csv")
    print(data)
    
    
#Window is created in 3 step 
#Spet 1 import the package 
#Spet 2 creat a window 
#Step 3 display the window 
window=Tk()#Tk function creat a window 
#customize the window 
window.geometry('1250x1000')
#Creat a lable 
heading=Label(window,text='Application for file analysis',font=100)
heading.place(x=650,y=30)
upload_Label=Label(window,text='Click below to upload your file', font=50,fg='Grey')
upload_Label.place(x=650,y=80)
upload_BTW=Button(window,text='Upload file', font=40,fg='Dark blue',command=uploadfile)
upload_BTW.place(x=700,y=120)
window.mainloop()# it is the last line of the programme 