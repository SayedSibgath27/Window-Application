from tkinter import*
import matplotlib.pyplot as plt
w=Tk()
w.geometry("800x800")
#Plot the graph 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
figure=plt.Figure(figsize=(6,5),dpi=(100))
ax=figure.add_subplot()
bar=FigureCanvasTkAgg(figure,w)
graph=bar.get_tk_widget()
graph.pack(side=LEFT, fill=BOTH)

import pandas as pd
data=pd.read_csv("C:\\Users\\HP Elitebook G6\\Desktop\\Python\\Data Visualation\\states.csv",index_col="State")
#print(data)

#date=data['Date']
#date=list(date)
#print(date)

#state=data['State']
#state=list(state)
#print(state)

#Filter the confirmed cases from karnataka 
confim=data.loc["Kerala"]["Confirmed"]
confim=list(confim)

recover=data.loc["Kerala"]["Recovered"]
recover=list(recover)
#print(recover)

death=data.loc["Kerala"]["Deceased"]
death=list(death)
#print(death)
date=data.loc["Kerala"]["Date"]
date=list(date)
#print(date)


#Plot the graph(Bar graph)
df=pd.DataFrame({'date':date, 'recover':recover, 'confim':confim, 'death':death})
df.plot.bar(x='date', y='recover', color='red', ax=ax,legend=True)
df.plot.bar(x='date', y='confim', color='green', ax=ax,legend=True)
df.plot.bar(x='date', y='death', color='blue', ax=ax,legend=True)



#Print the confirmed cases of Uttar Pradesh on 2021-09-13
#Find out the i dex of givendeath
givendata="2021-04-08"
index=0
c_data=""
for i in date:
   
    if i==givendata:
      #Fetch the confirmed t=cases of that index
      c_data=confim[index]
      #d_data=death[index]
      #r_data=recover[index]
      
    index=index+1
print(c_data)
#print(d_data)
#print(r_data)


w.mainloop()

