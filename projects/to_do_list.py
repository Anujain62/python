lst = []

def viewDetail():
 print("===List of tasks===")
 count = 1
 for item in lst:
  print(count,item)
  count+=1

def addTask(task):
 lst.append(task)
 print("Task appends successfully!")

def deleteTask(taskNo):
 lst.pop(taskNo)
 print("Delete task successfully!")


while True:
 print("\n=== To Do List ===")
 print("1. View Details\n2. Add task\n3. Delete task\n4. exit")
 option = int(input("Enter your choice : "))
 if(option==1):
  viewDetail()
 elif(option==2):
  task = input("Enter your task : ")  
  addTask(task)
 elif(option==3):
  viewDetail()
  taskNo = int(input("Enter task number : ")) 
  deleteTask(taskNo-1)
 elif(option==4):
  if(len(lst)==0):
   print("Done all tasks!")
   break
  else:
   print("You have remain some tasks!")
   for item in lst:
    print(item)
 else:
  print("Wrong option!") 
