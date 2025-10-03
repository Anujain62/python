
def main():
 try:
  a = int(input("hey, enter a number :"))
  print(a)
  return

 except Exception as e:
  print(e) 
  return

 finally:               #it runs always, if we returns before the exicution of finally so here also runs/exicutes finally block
  print("Hey, I am inside of finally!") 
 

main() 