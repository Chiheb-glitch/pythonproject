


import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sqlite3
import random

import mysql.connector

import time




import pylab


import numpy as np


from scipy.interpolate import interp1d


from scipy.signal import butter, lfilter, filtfilt


# from scipy.interpolate import spline


#get plot and draw axes


fig = plt.figure()


ax1 = fig.add_subplot(1,1,1)


moving_y = []


xaxisthings = []


startTime = time.time()


secondsShown = 5


secondsCalc = 5


plotHz = 20                        


totalWidth = plotHz*secondsShown


Oversample = 5


allY = [0]*plotHz*secondsShown


allX = [0]*plotHz*secondsShown

mydb=mysql.connector.Connect(host="192.168.1.6",user="chiheb123",passwd="123456789",database="exemple")
mycursor = mydb.cursor()
       


#function to set the next y value


def new_y_value(p):
   
   mycursor.execute("SELECT(`sensor`.`id`), `sensor`.`val`FROM `exemple`.`sensor`;")
   t=()
   for i in mycursor:
       t=t+i
   

   print(t[p])
   return t[p]

   

   

              


def animate(i):
   mycursor.execute("SELECT count(`sensor`.`id`)FROM `exemple`.`sensor`;")
   myresult=mycursor.fetchall()
   x=myresult[-1][-1]
   #add a new y value, and remove the first
   

   totaly = 0
   


   totalx = 0


   count = 0
   

   

   for j in range(secondsCalc * plotHz * Oversample):
       if j == x :
       	break

       totaly +=new_y_value(j)
        


       totalx +=time.time()-startTime


       count+=1


       if count == Oversample:


           allY.append(totaly/Oversample)


           allX.append(totalx/Oversample)


           count = 0


           totalx = 0


           totaly = 0

   
   while len(allY) > (secondsShown*plotHz):


       allY.pop(0)


       allX.pop(0)


   


   ax1.clear()


   ax1.plot(allX,allY)


ani = animation.FuncAnimation(fig, animate, interval=1)


plt.show()