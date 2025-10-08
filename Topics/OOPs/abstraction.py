# hiding the implementation details of a class and only showing the essential features to the user. 



# class Car:
#  def __init__(self):
#   self.acc = False
#   self.brk = False
#   self.clutch = False
#  def start(self):
#   self.clutch = True
#   self.acc = True
#   print("car started....")

# car1 = Car()
# car1.start()



# abc (abstract based classes) class are imported becuase python does not support directly.
from abc import ABC, abstractmethod
class Computer(ABC):      #this class is called abstract class because it contains abstract method.
 @abstractmethod 
 def process(self):       #this called abstract method becuase here writes only declaration but not write definiton.
  pass
  # print("inside computer")

class Laptop(Computer):
  def process(self):
   print("its running")

class Whiteboard(Laptop):
 def write(self):
  print("its writing")

class Programmer:
 def work(self,com):
  print("solving bugs")
  com.process()

# com = Computer()      it gives an error, because abstract method is compelsary to implimenting and then use it.
# com.process()

lap = Laptop()
# lap.process()

whbrd = Whiteboard()

prog = Programmer()
prog.work(lap)
prog.work(whbrd)
















