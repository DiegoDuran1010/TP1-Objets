# Single line comment 

'''
Ce ceci est un commentaire multi ligne

'''

from cgitb import grey, text
from time import timezone
from tkinter import *
from tkinter import font
from tkinter.font import BOLD
from setuptools import Command
import RPi.GPIO as GPIO
import time
import math
from ADCDevice import *
trigPin = 16
echoPin = 18
MAX_DISTANCE = 220          # define the maximum measuring distance, unit: cm
timeOut = MAX_DISTANCE*60   # calculate timeout according to the maximum measuring distance 
motorPins = (12, 16, 18, 22)    # define pins connected to four phase ABCD of stepper motor
CCWStep = (0x01,0x02,0x04,0x08) # define power supply order for rotating anticlockwise 
CWStep = (0x08,0x04,0x02,0x01)  # define power supply order for rotating clockwise
adc = ADCDevice() # Define an ADCDevice class object


def setupThermo():
    global adc
    if(adc.detectI2C(0x48)): # Detect the pcf8591.
        adc = PCF8591()
    elif(adc.detectI2C(0x4b)): # Detect the ads7830
        adc = ADS7830()
    else:
        print("No correct I2C address found, \n"
        "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
        "Program Exit. \n");
        exit(-1)
        
def loop():
    while True:
        value = adc.analogRead(0)        # read ADC value A0 pin
        voltage = value / 255.0 * 3.3        # calculate voltage
        Rt = 10 * voltage / (3.3 - voltage)    # calculate resistance value of thermistor
        tempK = 1/(1/(273.15 + 25) + math.log(Rt/10)/3950.0) # calculate temperature (Kelvin)
        tempC = tempK -273.15        # calculate temperature (Celsius)
        #print ('ADC Value : %d, Voltage : %.2f, Temperature : %.2f'%(value,voltage,tempC))
        print(tempC)
        time.sleep(0.01)

def destroy():
    adc.close()
    GPIO.cleanup()
    


def pulseIn(pin,level,timeOut): # obtain pulse time of a pin under timeOut
    t0 = time.time()
    while(GPIO.input(pin) != level):
        if((time.time() - t0) > timeOut*0.000001):
            return 0;
    t0 = time.time()
    while(GPIO.input(pin) == level):
        if((time.time() - t0) > timeOut*0.000001):
            return 0;
    pulseTime = (time.time() - t0)*1000000
    return pulseTime
    
def getSonar():     # get the measurement results of ultrasonic module,with unit: cm
    GPIO.output(trigPin,GPIO.HIGH)      # make trigPin output 10us HIGH level 
    time.sleep(0.00001)     # 10us
    GPIO.output(trigPin,GPIO.LOW) # make trigPin output LOW level 
    pingTime = pulseIn(echoPin,GPIO.HIGH,timeOut)   # read plus time of echoPin
    distance = pingTime * 340.0 / 2.0 / 10000.0     # calculate distance with sound speed 340m/s 
    return distance
    
def setupSonar():
    GPIO.setmode(GPIO.BOARD)      # use PHYSICAL GPIO Numbering
    GPIO.setup(trigPin, GPIO.OUT)   # set trigPin to OUTPUT mode
    GPIO.setup(echoPin, GPIO.IN)    # set echoPin to INPUT mode

def loop():
    while(True):
        distance = getSonar() # get distance
        print ("The distance is : %.2f cm"%(distance))
        time.sleep(1)

def setupMotor():    
    GPIO.setmode(GPIO.BOARD)       # use PHYSICAL GPIO Numbering
    for pin in motorPins:
        GPIO.setup(pin,GPIO.OUT)
        
# as for four phase stepping motor, four steps is a cycle. the function is used to drive the stepping motor clockwise or anticlockwise to take four steps    
def moveOnePeriod(direction,ms):    
    for j in range(0,4,1):      # cycle for power supply order
        for i in range(0,4,1):  # assign to each pin
            if (direction == 1):# power supply order clockwise
                GPIO.output(motorPins[i],((CCWStep[j] == 1<<i) and GPIO.HIGH or GPIO.LOW))
            else :              # power supply order anticlockwise
                GPIO.output(motorPins[i],((CWStep[j] == 1<<i) and GPIO.HIGH or GPIO.LOW))
        if(ms<3):       # the delay can not be less than 3ms, otherwise it will exceed speed limit of the motor
            ms = 3
        time.sleep(ms*0.001)    
        
# continuous rotation function, the parameter steps specifies the rotation cycles, every four steps is a cycle
def moveSteps(direction, ms, steps):
    for i in range(steps):
        moveOnePeriod(direction, ms)
        
# function used to stop motor
def motorStop():
    for i in range(0,4,1):
        GPIO.output(motorPins[i],GPIO.LOW)
            
def loop():
    while True:
        moveSteps(1,3,512)  # rotating 360 deg clockwise, a total of 2048 steps in a circle, 512 cycles
        time.sleep(0.5)
        moveSteps(0,3,512)  # rotating 360 deg anticlockwise
        time.sleep(0.5)

def destroy():
    GPIO.cleanup()             # Release resource

def main():
    # Window est la variable qui va set la window pour l'interface
    window =Tk() 
    window.title('TP1 ')
    window.geometry("600x600+10+20")
   
   # Variable lbl est la variable qui s'occupe d'afficher le titre de l'application
    lbl = Label(window, text = "Contrôle d'une porte d'aération d'une serre", fg='black', font=("Adobe arabic",12,BOLD))
    lbl.place(x= 150,y= 50)

    lblTemp = Label(window, text="", Command = loop, fg='black',font=("Adobe arabic",BOLD,12))
    lblTemp.place(x=155,y = 50)



    #Variable lbl2 est la variable qui s'occupe d'afficher la température de l'ouverture de la porte
    lbl2 = Label(window, text="Température d'ouverture de la porte : ", fg='black',font=("Adobe arabic",10,BOLD))
    lbl2.place(x = 10, y = 100)
    #Variable lbl3 est la variable qui s'occupe d'afficher la distance de la porte du recepteur 
    lbl3 = Label(window, text="Distance d'ouverture de la porte: ", fg='black',font=("Adobe arabic",10,BOLD))
    lbl3.place(x=10, y=125)
    #Variable lblControle est la variable qui s'occupe d'afficher le contôle voulu
    lblControle = Label(window, text="Contrôle:",fg='black',font=("Adobe arabic",10,BOLD,UNDERLINE))
    lblControle.place(x=10,y=150)
    #Variable btnAutomatique est le button qui va afficher automatique et qui va ouvrir la porte de façon automatique
    btnAutomatique = Button(window, text="Automatique",fg='black')
    btnAutomatique.place(x=80, y=150)
    #Variable btnManuelle est le button qui va afficher manuelle et qui va ouvrir la porte de façon manuelle
    btnManuelle = Button(window, text="Manuelle",fg='black')
    btnManuelle.place(x=80, y=180)
    #Variable txtfld est l'espace où l'utilisateur va rentrer le pourcentage dont il veut ouvrir la porte
    txtfld = Entry(window,text="", bd=2, width=5)
    txtfld.place(x=180, y=180)
    #Variable lblPourcentage affiche le signe de %
    lblPourcentage = Label(window,text="%", fg="black", font=("Adobe arabic",15))
    lblPourcentage.place(x=250,y=185)
    #Variable btnOuvrir est le button qui va permettre d'ouvrir la porte 
    btnOuvrir = Button(window, text="Ouvrir la porte!",fg='black')
    btnOuvrir.place(x=80, y=220)
    #Variable btnFermer est le button qui va permettre de fermer la porte
    btnFermer = Button(window, text="Fermer la porte!",fg='black')
    btnFermer.place(x=210, y=220)
    #Variable lblMoteur affiche le statut du moteur
    lblMoteur = Label(window,text="Statut du Moteur :", fg='black', font=("Adobe arabic",10,BOLD,UNDERLINE))
    lblMoteur.place(x=10,y=250)
    #Variable lblDirection affiche la direction que la porte est en train de bouger
    lblDirection = Label(window, text="Direction : ", fg='black',font=("Adobe arabic", 10 ,  BOLD))
    lblDirection.place(x=10,y=270)
    #Variable lbldeDirection affiche la direction gauche ou droite
    lbldeDirection = Label(window, text="Gauche ou Droite", fg='black', font=("Adobe arabic",10))
    lbldeDirection.place(x=80,y=271)
    #Variable lblVitesse affiche la vitesse à laquelle la porte va bouger
    lblVitesse = Label(window, text="Vitesse : ", fg='black', font=("Adobe Arabic",10, BOLD))
    lblVitesse.place(x=250, y=270)
    #Variable btnAfficher est un button qui va afficher les logs 
    btnAfficher = Button(window, text="Afficher les logs", fg='black')
    btnAfficher.place(x=200,y=300)
    #window.mainloop garde la fênetre ouverte 
    window.mainloop()





if __name__ == "__main__":
    setupThermo()
    setupSonar()
    setupMotor()

    main()


