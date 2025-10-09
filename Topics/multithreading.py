from threading import *
from time import sleep

class Hello(Thread):
 def run(self):
  for i in range(5):
   print("Hello")
   sleep(1)

class Hii(Thread): 
 def run(self):
  for i in range(5):
   print("Hii")
   sleep(1)

t1 = Hello()
t2 = Hii()
# # here works main thread by default, and it runs whole methods
# t1.run()
# t2.run()

# here threads are work and it prints simultaniously
t1.start()
sleep(0.2)
t2.start()
t1.join()
t2.join()
print("byeee!")












