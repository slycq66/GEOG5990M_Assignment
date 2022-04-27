  ---------------------------------------------------------------
  ***************************************************************
  *                      Sheep and Grass                        *
  ***************************************************************
  *                                                             *
  *       My GitHub Homepage: https://github.com/slycq66/       *
  * GNU GENERAL PUBLIC LICENSE 3+  HTTP://WWW.GNU.ORG/licenses/ *
  *                                                             *
  ***************************************************************
  *                      Version   1.1                          *
  ***************************************************************
  ---------------------------------------------------------------
  
 INSTALLING: 

 Download agentframework.py and mymodel.py. They should be put in the same file.

 To run: Reconmand to run mymodel.py by Spyder.
 
 Note that if you are running this in Spyder, you may also need to tell that specifically to    use a different backend. Make sure you're using an IPython prompt (prompt looks like "[1]")    rather than a standard Python prompt (prompt looks like ">>>"), then go to the Tools menu,    the Preferences menuitem, and pick IPython console from the list on the left, the Graphics    tab; and adjust the Backend drop down list to Automatic, then save your files and restart     Spyder. 
 
 If you don't have Spyderk, you can download it here:
 https://www.spyder-ide.org/
 
  ---------------------------------------------------------------
 
 USE: 
 
 The model is an ABM(agent based model).It can be used to model a very simple ecosystem. The  model automatically creates sheep that move randomly around the environment, storing certain  substances in the environment (such as grass) and sharing them with other sheep.

 The model can do:

 ·Builds agents in a space;
 ·Gets them to interact with each other;
 ·Reads in environmental data;
 ·Gets agents to interact with the environment;
 ·Randomizes the order of agent actions;
 ·Displays the model as an animation;
 ·Is contained within a GUI;
 ·Is initialised with data from the web.
 
  ---------------------------------------------------------------
 
 IDEAS FOR FURTHER DEVELOPMENT
 
 ·Getting the sheep to move in a more realistic way, such as toward more food;
 ·Create a new agent: wolves and allow them to hunt sheep; 
 ·To regenerate the environment at a certain rate;
 ·Let sheep or wolves replicate after certain conditions have been met, such as accumulating   more than 2,000 units of forage or eating four sheep;
 ·Give the agent age attribute, die naturally after a certain number of iteration, and allow     the energy to re-enter the environment.

 Tried but failed: Build a GUI that lets users customize initial variables. The code can be found in agentframework.py.
   
 ---------------------------------------------------------------