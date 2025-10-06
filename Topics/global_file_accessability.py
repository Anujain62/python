from pathlib import Path
path = Path()

# we can assess all global files/folders 
# for file in path.glob('*'):
#  print(file)


# we can acceess any specific extention files from the global
# 1)
# for file in path.glob('*.py'):
#  print(file)


# 2)
for file in path.glob('*.txt'):
 print(file)
