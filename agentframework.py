# -*- coding: utf-8 -*-
"""
Version 1.1

Created on Mon Feb 14 16:36:45 2022

@author: student201581226
"""


import random

"""
Those sheeps will wonder around, eat grass, store grass in their 'pocket', and share
grass with their neighbours.
"""
class Sheep ():
    
    """
    function __init__(): 

        Initialize the attribute of each sheep, conbine with environment and other sheep.
        
        self -- the created class instance itself
    
        environment -- the environment list
        
        agents -- the agents list(include the sheep itself)
        
        store -- the amount of grass stored, the initial value is 0

    """
    def __init__ (self, environment, agents, y, x):
        self._x = x
        self._y = y
        self.store = 0
        self.environment = environment
        self.agents = agents
           
    def getx(self):
        return self._x

    def setx(self,value):
        self._x = value
        
    x = property(getx, setx)
    
    def gety(self):
        return self._y

    def sety(self,value):
        self._y = value   
        
    y = property(gety, sety)  
    
    """
    function move(): 

        Make the sheep move one unit under a specific condition. 
        
        When they go beyond the boundary, the sheeps will reappear at the other side.

    """  
    def move (self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100

        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
            

    """
    function eat(): 

        Make the sheep eat and store grass. 
        
        Normally they will eat and store up to 10 units of grass at a time, 
        but when the number of grass is less than 10, they will only eat the rest.

    """             
    def eat (self): 
        if  self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
        else:
            self.environment[self._y][self._x] = 0
            self.store += self.environment[self._y][self._x]
            

    """
    function distance_between(): 

        Calculate the Euclidean distance between two sheep.

    """   
    def distance_between(self, agent):
        return (((self._x - agent._y)**2) 
              + ((self._y - agent._y)**2))**0.5
    

    """
    function share_with_neighbours(): 

        Divide the stored grass of sheep within neighbourhood, 
        and print the distance and the number of redistributed grass, 
        keeping two decimal places.

    """      
    def share_with_neighbours (self, neighbourhood):
        for agent in self.agents: 
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                print("sharing " + str(round(dist,2)) + " " + str(round(ave,2)))