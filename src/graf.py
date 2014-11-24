import serial # import Serial Library
import numpy  # Import numpy
import matplotlib.pyplot as plt #import matplotlib library
from drawnow import *
import random

voltg= []
pressure=[]
arduinoData = serial.Serial('/dev/ttyACM0', 9600) #Creating our serial object named arduinoData
plt.ion() #Tell matplotlib you want interactive mode to plot live data
cnt=0

def is_valid(data):
    try:
        float(data)
        aux = data.split('.')
        if len(aux[1]) is 2:
            return True
        else:
            return False
    except:
        return False
def makeFig(): #Create a function that makes our desired plot
    plt.ylim(0,50)                                 #Set y min and max values
    test = "Lectura Actual: "+str(voltg[-1]) + " [V]"
       plt.title(test)
    plt.grid(True)                                  #Turn the grid on
    plt.ylabel('Tension [V]')                            #Set ylabels
    plt.plot(voltg, 'ro-', label='Tension')       #plot the temperature
    plt.legend(loc='upper left')                    #plot the legend
    
    

while True: # While loop that loops forever
    try:
        while (arduinoData.inWaiting()==0): #Wait here until there is data
            pass #do nothing
        arduinoString = arduinoData.readline().replace('\r\n','') #read the line of text from the serial port
        if is_valid(arduinoString):
            pass
        else:
            continue
        temp = float(arduinoString) 
        voltg.append(temp)                     #Build our voltg array by appending temp readings
        drawnow(makeFig)                       #Call drawnow to update our live graph
        plt.pause(.000001)                     #Pause Briefly. Important to keep drawnow from crashing
        cnt=cnt+1
        if(cnt>50):                            #If you have 50 or more points, delete the first one from the array
            voltg.pop(0)                       #This allows us to just see the last 50 data points
    except KeyboardInterrupt:
        break