import pandas as pd
data=pd.read_csv("C:\\Users\\HP Elitebook G6\\Desktop\\Python\\covidproject\\state_wise.csv",index_col="State")
print(data)

#date=data['Date']
#date=list(date)
#print(date)

#state=data['State']
#state=list(state)
#print(state)

#Filter the confirmed cases from karnataka 
confim=(data.loc["Uttar Pradesh"]["Confirmed"])
confim=list(str(confim))
print(confim)

con_data=''
for i in confim:
    con_data=con_data+i
print(con_data)


recover=(data.loc["Uttar Pradesh"]["Recovered"])
recover=list(str(recover))
print(recover)

rec_data=''
for i in confim:
    rec_data=rec_data+i
print(rec_data)

death=(data.loc["Uttar Pradesh"]["Deaths"])
death=list(str(death))
print(death)
#date=data.loc["Uttar Pradesh"]["Date"]
#date=list(date)
#print(date)


death_data=''
for i in confim:
    death_data=death_data+i
print(death_data)


'''#Plot the graph(Bar graph)
df=pd.DataFrame({'date':date,'recover':recover,'confim':confim, 'death':death})
df.plot.bar(x='date', y='recover', color='green')
df.plot.bar(x='date', y='confim', color='red')
df.plot.bar(x='date', y='confim', color='blue')



#Print the confirmed cases of Uttar Pradesh on 2021-09-13
#Find out the i dex of givendeath
givendata="2021-04-08"
index=0
c_data=""
for i in date:
   
    if i==givendata:
      #Fetch the confirmed t=cases of that index
      c_data=confim[index]
      d_data=death[index]
      r_data=recover[index]
      
    index=index+1
print(c_data)
print(d_data)
print(r_data)
'''
