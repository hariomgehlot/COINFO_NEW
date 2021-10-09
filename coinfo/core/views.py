from django.shortcuts import render
from django.shortcuts import render
import matplotlib.pyplot as plt
import requests
import pandas as pd


def index(request):
     return render(request,'index.html')

def get_data():
     url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"


     headers = {
     'x-rapidapi-key': "c2d96daf15mshff016f7faac1f93p1d399cjsn0e7e7622dfc7",
     'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
     }

     return requests.request("GET", url, headers=headers)

def statewise(request):
     api_response =get_data()
     json = api_response.json()

     df = pd.DataFrame(json)

     df2= df.T

     df2.columns

     df2 = df2.drop(['active', 'confirmed', 'deaths', 'deltaconfirmed', 'deltadeaths',
       'deltarecovered', 'lastupdatedtime', 'migratedother', 'recovered',
       'state', 'statecode', 'statenotes', 'State Unassigned'], axis=1)

     df2.reset_index(drop=True, inplace=False)
     states = list(df2.columns)
     statecodes=[]
     for state in states:
          statecodes.append(df2[state][2]["statecode"])
     active_X = []
     confirmed_X = []
     death_X=[]
   
     for state in states:
          active_X.append(int(df2[state][2]['active']))
          confirmed_X.append(int(df2[state][2]['confirmed']))
          death_X.append(int(df2[state][2]['deaths']))
     
     aX =  plt.figure(figsize=(15,5))
     plt.xlabel("States",fontdict={"fontsize":"20"})
     plt.ylabel("Active Cases",fontdict={"fontsize":"20"})
     plt.title("Active Cases in States",fontdict={"fontsize":"16","color":"red"})
     plt.xticks(rotation=80,fontsize=16)
     plt.yticks([i for i in range(25000,175001,25000)],[str(k)+"k" for k in [i for i in range(25,176,25)]])
     plt.bar(statecodes,active_X,color=["red","black","blue","yellow"],width=0.5)
     for s in range(len(states)):
          if(active_X[s] >125000):
               plt.text(s,active_X[s]//2,active_X[s],ha='center',rotation=90,bbox=dict(facecolor='yellow',alpha=1))
          else:
               plt.text(s,active_X[s],active_X[s],ha='center',rotation=90,bbox=dict(facecolor='yellow',alpha=1))
     
     plt.savefig("./core/static/core/active.png")


     cX = plt.figure(figsize=(15,5))
     plt.xlabel("States",fontdict={"fontsize":"16"})
     plt.ylabel("Confirmed Cases",fontdict={"fontsize":"20"})
     plt.title("Confirmed Cases in States",fontdict={"fontsize":"20","color":"red"})
     plt.xticks(rotation=80,fontsize=16)
     plt.yticks([i for i in range(500000,6500000,500000)],[str(k)+"k" for k in [i for i in range(500,6500,500)]])
     plt.bar(statecodes,confirmed_X,color=["red","black","blue","yellow"])
     for s in range(len(states)):
          if(confirmed_X[s] > 5000000):
               plt.text(s,confirmed_X[s]//2,confirmed_X[s],ha='center',bbox=dict(facecolor='yellow',alpha=1),rotation=90)
          else:
               plt.text(s,confirmed_X[s]-20,confirmed_X[s],ha='center',bbox=dict(facecolor='yellow',alpha=1),rotation=90)
     plt.savefig("./core/static/core/confirm.png")


     dX = plt.figure(figsize=(15,5))
     plt.xlabel("States",fontdict={"fontsize":"20"})
     plt.ylabel("Death Cases",fontdict={"fontsize":"20"})
     plt.title("Death Cases in States",fontdict={"fontsize":"20","color":"red"})
     plt.xticks(rotation=80,fontsize=16)
     plt.yticks([i for i in range(0,140001,20000)],[str(k)+"k" for k in [i for i in range(0,141,20)]])
     plt.bar(statecodes,death_X,color=["red","black","blue","yellow"])
     for s in range(len(states)):
          if(death_X[s] >120000):
               plt.text(s,death_X[s]//2,death_X[s],ha='center',bbox=dict(facecolor='yellow',alpha=1),rotation=90)
          else:
               plt.text(s,death_X[s],death_X[s],ha='center',bbox=dict(facecolor='yellow',alpha=1),rotation=90)
     plt.savefig("./core/static/core/death.png")


     
     return render(request, "state.html", {'active_page' : 'state.html'})


def tests(request):
     return render(request,"tests.html")

def world(request):
     return render(request,"world.html")


def SWD(request):
     return render(request,"SWD.html")