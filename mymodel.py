# -*- coding: utf-8 -*-
"""
Version 1.1

Created on Mon Feb 11 10:24:45 2022

@author: student201581226
"""

#Environment Settings
import matplotlib
matplotlib.use('TkAgg')
import random
import matplotlib.pyplot
import agentframework
import csv
import tkinter
from tkinter import *
import matplotlib.animation 
import operator
import requests
import bs4

#Initialization of variable
num_of_agents = 10 #Number of sheeps
num_of_iterations = 10
neighbourhood = 20
agents = [] #Creat an empty list

#Fetching data from web pages and use it as sheep's coordinates
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
# print(td_ys)
# print(td_xs)

#Randomizes the order of agent actions
random.seed(2) 

#Create variables for animation presentation
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


"""
function read_env(): 

    Read an raster data and put this data into a 2D list.

    filename -- the raster data(a csv or text file) we want to use as environment

"""
def read_env(filename):
    with open(filename, newline='') as f:
        reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
        environment = []
        for row in reader:
            rowlist = []
            for value in row:
                rowlist.append(value)
            environment.append(rowlist)
    #Check if we read it correctly
    #     matplotlib.pyplot.imshow(environment)
    # matplotlib.pyplot.show()
    return environment
environment = read_env('in.txt')


# Make the agents
for i in range(num_of_agents):
    #Instantiate Sheep class and add them to agents list
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Sheep(environment, agents, y, x)) 

carry_on = True
"""
    To test if the agents can work well:  
    a = agentframework.Agent()
    print(a.y, a.x)
    a.move()
    print(a.y, a.x)
    print(agents)
    print(type(agents))
    print(max(agents, key=operator.itemgetter(1))) 
"""


#Define the update function for visualization
def update(frame_number):
    fig.clear()
    global carry_on
    
    for j in range(num_of_iterations): 
            
            for i in range(num_of_agents):
                agents[i].move()
                agents[i].eat()
                agents[i].share_with_neighbours(neighbourhood)
                #print agents[i]
    # get the most easterly point on the graph as red
    # m = max(agents, key=operator.itemgetter(1))
    # matplotlib.pyplot.scatter(m[1],m[0], color='red')
    
    #Draw the scatter diagram of the agent and environment
    for i in range(num_of_agents):
        matplotlib.pyplot.ylim(0, 100)
        matplotlib.pyplot.xlim(0, 100)
        matplotlib.pyplot.imshow(environment)
        matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y,color="white")
        #print(agents[i].x,agents[i].y)


#Define the stop condition of the model
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < num_of_iterations) & (carry_on) :
        yield a	#Returns control and waits next call
        a = a + 1


#Call gen_function andupdate, print scatter and environment on canvas
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()


#Setting GUI Interface
root = tkinter.Tk()
root.wm_title("Student ID: 201581226")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
# c = tkinter.Canvas(root, width=200, height=200)
# c.pack() # Layout
# c.create_rectangle(0, 0, 200, 200, fill="blue")
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
tkinter.mainloop() #Wait for interactions.

"""
The code below is tring to make GUI that users can set variebles:

from tkinter import *

root = tkinter.Tk()

Label(root, text="number of sheep:").grid(row=0, column=0)
Label(root, text="number of iteration:").grid(row=1, column=0)

v1 = StringVar()
v2 = StringVar()
e1 = Entry(root, textvariable=v1)
e2 = Entry(root, textvariable=v2)
e1.grid(row=0, column=1, padx=5, pady=5)
e2.grid(row=1, column=1, padx=5, pady=5)

num_of_agents,num_of_iterations = None,None

def set_by_user():
    global num_of_agents,num_of_iterations
    num_of_agents = e1.get() 
    num_of_iterations = e2.get()

Button(root, text="set", width=10, command=get_variables) \
    .grid(row=2, column=2, sticky=W, padx=10, pady=10)

Button(root, text="quit", width=10, command=root.quit) \
    .grid(row=3, column=2, sticky=E, padx=10, pady=10)

tkinter.mainloop()
"""