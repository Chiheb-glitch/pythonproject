import sqlite3
import time
import mysql.connector
import Adafruit_ADS1x15


mydb=mysql.connector.Connect(host="192.168.1.6",user="chiheb123",passwd="123456789",database="exemple")
mycursor = mydb.cursor()


adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1

mycursor.execute("DELETE FROM `exemple`.`sensor` WHERE id > 0")

while 1:
 values = [0]*4
 for i in range(4):
    
      values[i] = adc.read_adc(i, gain=GAIN)

 sql=("INSERT INTO `sensor` (`val`) VALUES ({})".format(*values))

  

 mycursor.execute(sql)
 print("values({})".format(*values))
 time.sleep(1)
 mydb.commit()
 
