"""my_controller_supervisor controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, LED, DistanceSensor
from controller import Supervisor,Emitter,Node,Field,Keyboard
import math
import sys



class Driver (Supervisor) :
  x = 0.1
  z = 0.3
  
  translationValues = [[0.75,0.32,-2],[0.75,0.32,-1.5],[0.75,0.32,-1.0],[0.75,0.32,-0.5],[0.75,0.32,0],
                      [0.75,0.32,0.5],[0.75,0.32,1.0],[0.75,0.32,1.5],[0.75,0.32,2]]
                      
  secondTrans =  [[0.75,0.32,-2],[1.0,0.32,-2],[1.5,0.32,-2],[2,0.32,-2],[2.5,0.32,-2],[3,0.32,-2]]
  def wait(self): 
      n = 0
      while (n < 200):
        n = n + 1
        if self.step(self.timeStep) == -1: break
  def initialization(self):
    self.timeStep = int(self.getBasicTimeStep())
    robot = self.getFromDef('PLAYER')
    if robot is None:
      #robot might be None if the controller is about to quit
      sys.exit(1);


    print robot.getField('translation').getSFVec3f()
    #robot.getField('rotation').setSFRotation([0.785094, 0.437966, 0.437965, 4.47276])
    #45 graus anti horario
    robot.getField('rotation').setSFRotation([-0.862981, 0.357257, 0.357256, 1.71763])
    self.wait()
    self.wait()
    #for value in self.translationValues:
     # robot.getField('translation').setSFVec3f(value)
      #self.wait()
    
    #45 graus horario
    #robot.getField('rotation').setSFRotation([-0.862981, -0.357257, -0.357256, 1.71763])
    
    # for value in self.secondTrans:
    #   robot.getField('translation').setSFVec3f(value)
    #   self.wait()
    
    while(1):
      ori = robot.getOrientation()
      angle = 180 - abs( math.degrees(math.atan2(ori[1],ori[7])))
      print robot.getField('translation').getSFVec3f()
      print angle
      if self.step(self.timeStep) == -1: break
   
    #orientation = robot.getOrientation()
    #print orientation
    #orientation[1] = 0
    #orientation[7] = 0
    
    #print robot.getField('rotation').setSFRotation([-0.862981, 0.357257, 0.357256, 1.71763])
    #while(1):
     # ori = robot.getOrientation()
      #angle = 180 - abs( math.degrees(math.atan2(ori[1],ori[7])))
      #print angle
      #if self.step(self.timeStep) == -1: break
controller = Driver()
controller.initialization()