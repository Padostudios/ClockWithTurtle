from turtle import *
from datetime import datetime
import random

pen = Turtle()
pen.speed(10)
pen.width(5)
randomBgColors = ["orange","red","blue","green","cyan","pink","yellow","purple"]
bg = bgcolor(random.choice(randomBgColors))


#-------------NUMBERS------------------------
#These functions are shape of number to be drawn
def zero():
    pen.seth(180)
    pen.forward(30)
    pen.seth(270)
    pen.forward(150)
    pen.seth(0)
    pen.forward(60)
    pen.seth(90)
    pen.forward(150)
    pen.seth(180)
    pen.forward(30)

def one():
    pen.seth(230)
    pen.forward(60)
    pen.back(60)
    pen.seth(270)
    pen.forward(150)

def two():
    pen.seth(180)
    pen.forward(60)
    pen.back(60)
    pen.seth(270)
    pen.forward(75)
    pen.seth(180)
    pen.forward(60)
    pen.seth(270)
    pen.forward(75)
    pen.seth(0)
    pen.forward(60)


def three():
    pen.seth(180)
    pen.forward(60)
    pen.back(60)
    pen.seth(270)
    pen.forward(75)
    pen.seth(180)
    pen.forward(45)
    pen.back(45)
    pen.seth(270)
    pen.forward(75)
    pen.seth(180)
    pen.forward(60)

def four():
    pen.seth(270)
    pen.forward(150)
    pen.back(150)
    pen.seth(240)
    pen.forward(96.5)
    pen.seth(0)
    pen.forward(85)


def five():
    pen.seth(180)
    pen.forward(60)
    pen.seth(270)
    pen.forward(75)
    pen.seth(0)
    pen.forward(60)
    pen.seth(270)
    pen.forward(75)
    pen.seth(180)
    pen.forward(60)
    
def six():
    pen.seth(180)
    pen.forward(60)
    pen.seth(270)
    pen.forward(150)
    pen.seth(0)
    pen.forward(60)
    pen.seth(90)
    pen.forward(75)
    pen.seth(180)
    pen.forward(60)

def seven():
    pen.seth(180)
    pen.forward(60)
    pen.back(60)
    pen.seth(249)
    pen.forward(79)
    pen.seth(180)
    pen.forward(20)
    pen.back(40)
    pen.seth(180)
    pen.forward(20)
    pen.seth(249)
    pen.forward(82)


def eight():
    pen.seth(180)
    pen.forward(30)
    pen.seth(270)
    pen.forward(150)
    pen.seth(0)
    pen.forward(60)
    pen.seth(90)
    pen.forward(150)
    pen.seth(180)
    pen.forward(30)
    pen.seth(180)
    pen.forward(30)
    pen.seth(270)
    pen.forward(75)
    pen.seth(0)
    pen.forward(60)
   
def nine():
    pen.seth(180)
    pen.forward(60)
    pen.seth(270)
    pen.forward(60)
    pen.seth(0)
    pen.forward(60)
    pen.seth(90)
    pen.forward(60)
    pen.back(150)
    pen.seth(180)
    pen.forward(60)

#-----------------------------------------------------------------------

#Positions------------------------------
#These functions are positions of number to be drawn
def firstPos():
    pen.penup()
    pen.setpos(-420,20)
    pen.pendown()
    
    

def secondPos():
    pen.penup()
    pen.setpos(-330,20)
    pen.pendown()
    


def thirdPos():
    pen.penup()
    pen.setpos(-160,20)
    pen.pendown()
    

def fourthPos():
    pen.penup()
    pen.setpos(-80,20)
    pen.pendown()
   


def fifthPos():
    pen.penup()
    pen.setpos(60,20)
    pen.pendown()
    


def sixthPos():
    pen.penup()
    pen.setpos(160,20)
    pen.pendown()
    
#--------------------------------------------------------
#This function draws the values ​​from moment list.
def whatisI(i):
    if i==0:
        zero()
    elif i ==1:
        one()
    elif i==2:
        two()
    elif i==3:
        three()
    elif i==4:
        four()
    elif i==5:
        five()
    elif i==6:
        six()
    elif i==7:
        seven()
    elif i==8:
        eight()
    elif i==9:
        nine()
#--------------------------------------------------------------

#Steps--------------------------------------------------------
#This function draws the shape of two points between times

def firstStp():
    pen.penup()
    pen.setpos(-250,10)
    pen.seth(270)
    pen.pendown()
    pen.forward(30)
    pen.penup()
    pen.forward(60)
    pen.pendown()
    pen.forward(30)

def secondStp():
    pen.penup()
    pen.setpos(-30,10)
    pen.seth(270)
    pen.pendown()
    pen.forward(30)
    pen.penup()
    pen.forward(60)
    pen.pendown()
    pen.forward(30)


while True:
    moment = datetime.now()
    moment = datetime.strftime(moment,"%X")
    moment = [int(i) for i in moment if i!=":"]
    firstPos()
    whatisI(moment[0])
    secondPos()
    whatisI(moment[1])
    firstStp()
    thirdPos()
    whatisI(moment[2])
    fourthPos()
    whatisI(moment[3])
    secondStp()
    fifthPos()
    whatisI(moment[4])
    sixthPos()
    whatisI(moment[5])
    pen.reset()
    pen.speed(10)
    pen.width(5)
    bg = bgcolor(random.choice(randomBgColors))
    
    
    

    



done()




#pen.speed(10)
#pen.width(5)