#Name: Lee Yun Fai
#Matric Number: U1820770G

import math

Heighttxt = open("Height.txt","r") #opening the file

OriginalHeightList = Heighttxt.readlines()
ListLength = len(OriginalHeightList) #to be used as end limit for range function
HeightList = []

for n in range(1,ListLength):
    HeightList += [float(OriginalHeightList[n])] #HeightList is list of heights in float form, enabling calculations

HListLength = len(HeightList) #to be used as end limit for range function

Seg1 = 0 #Assigning values to variable used to calculate number of people in height category
Seg2 = 0
Seg3 = 0
Seg4 = 0
Seg5 = 0
Seg6 = 0
Seg7 = 0
Seg8 = 0
Seg9 = 0
Seg10 = 0

for i in range(0,HListLength): #to sort the list of heights into the number of people in their respective height category
    if 1.10 <= HeightList[i] < 1.21: #manual assignment of limits is preferable for better readability when bar chart is plotted
        Seg1 += 1
    if 1.21 <= HeightList[i] < 1.32:
        Seg2 += 1
    if 1.32 <= HeightList[i] < 1.43:
        Seg3 += 1
    if 1.43 <= HeightList[i] < 1.54:
        Seg4 += 1
    if 1.54 <= HeightList[i] < 1.65:
        Seg5 += 1
    if 1.65 <= HeightList[i] < 1.76:
        Seg6 += 1
    if 1.76 <= HeightList[i] < 1.87:
        Seg7 += 1
    if 1.87 <= HeightList[i] < 1.98:
        Seg8 += 1
    if 1.98 <= HeightList[i] < 2.09:
        Seg9 += 1
    if 2.09 <= HeightList[i] < 2.20:
        Seg10 += 1

Segs = [Seg1, Seg2, Seg3, Seg4, Seg5, Seg6, Seg7, Seg8, Seg9, Seg10] #for plotting of bar chart later
XInterval = ['1.10-1.21','1.21-1.32','1.32-1.43','1.43-1.54','1.54-1.65','1.65-1.76','1.76-1.87','1.87-1.98','1.98-2.09','2.09-2.20'] #label x-axis intervals

Heighttxt.close() #end of consolidation of information



import turtle #start of plotting of bar chart
turtle.setworldcoordinates(-100,-100,1500,1800)
turtle.title('Number Of People against Height Category(m)')
turtle.bgcolor('linen') #filling the background color

def axis(): #plotting of axes of bar chart
    x = turtle.Turtle()
    y = turtle.Turtle()

    x.speed(0) #for fastest plotting of axes
    y.speed(0)
    
    countx = 0
    county = 0
    xinterval = 0
    yinterval = 1

    while countx < 1000:
        x.forward(100)
        x.right(90)
        x.forward(10)

        x.penup() #to adjust interval words to a suitable position
        x.forward(40)
        x.right(90)
        x.forward(40)
        x.write(XInterval[xinterval],font = ('Arial',6,'underline')) #font adjusted for better visibility on barchart
        x.back(40)
        x.left(90)
        x.back(40)
        x.pendown()

        
        x.back(10)
        x.left(90)

        xinterval += 1
        countx += 100

    else:
        x.forward(100)
        x.write('Height Category(m)',font = ('Arial',11,'bold')) #labelling of x-axis

    y.left(90)
    while county < 1500:
        y.forward(100)
        y.left(90)
        y.forward(10)

        y.penup() #to adjust interval words to a suitable position
        y.forward(30)
        y.left(90)
        y.forward(30)
        y.write(str(yinterval),font = ('Arial',7)) #font adjusted for better visibility on barchart
        y.back(30)
        y.right(90)
        y.back(30)
        y.pendown()
        
        
        y.back(10)
        y.right(90)

        yinterval += 1
        county += 100
        

    else:
        y.forward(100)
        y.write('Number Of People',font = ('Arial',11,'bold')) #labelling of y-axis

axis()



def net(): 
    net = turtle.Turtle()
    net.speed(0)
    net.penup()
    net.left(90)
    net.forward(100)
    net.right(90)
    net.pendown()

    netcount = 0
    
    while netcount < 1500: #plotting reference lines
        net.color('grey')
        net.forward(1100)
        net.back(1100)

        net.penup()
        net.left(90)
        net.forward(100)
        net.right(90)
        net.pendown()

        netcount += 100

    else: #adding the title at the top of the bar chart
        net.penup()
        net.left(90)
        net.forward(100)
        net.right(90)
        net.forward(100)
        net.pendown()
        net.color('black')
        net.write('Number Of People against Height Category(m)',font = ('Arial',13,'underline'))

    net.hideturtle()

net()



bar = turtle.Turtle()
bar.speed(10) #for quick plot of bar
def individualbar(a,b): #base code to plot individual bar with customizable color fill
    bar.begin_fill()
    bar.color('black',b)
    bar.pendown()
    bar.setheading(90)
    bar.forward(a*100)
    bar.right(90)
    bar.forward(100)
    bar.right(90)
    bar.forward(a*100)
    bar.end_fill()

def plotbars(): #code to plot collective sets of data into bar chart
    bar.forward(50)
    individualbar(Seg1,'red')
    individualbar(Seg2,'tomato')
    individualbar(Seg3,'orange')
    individualbar(Seg4,'gold')
    individualbar(Seg5,'darkseagreen')
    individualbar(Seg6,'green')
    individualbar(Seg7,'cornflowerblue')
    individualbar(Seg8,'mediumslateblue')
    individualbar(Seg9,'purple')
    individualbar(Seg10,'violet')
    bar.hideturtle()

plotbars()
    
turtle.done()













