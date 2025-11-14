# The Egyptian football team will be in Russia for the World Cup. Of course, they all would like to buy souvenirs for their families. Luckily, they met the king of souvenirs Matryoshka who is famous for his masterpiece Katryoshka. He makes it using different wooden pieces: eyes, mouths and bodies. He can form a nice Katryoshka using one of the following combinations:

# Two eyes and one body.
# Two eyes, one mouth, and one body.
# One eye, one mouth, and one body.
# If the king has n
#  eyes, m
#  mouths and k
#  bodies, what is the largest number of Katryoshkas he can make?
# Input
# Only one line containing three numbers n
# , m
#  and k
#  (0≤n,m,k≤1018
# ) – the number of eyes, mouths and bodies respectively.

# Output
# Print the largest number of Katryoshkas he can make.






eye,mouth,body = map(int,input().split())

katryoshkas = 0

c = min(mouth,eye,body)
eye-=c 
mouth-=c 
body-=c 

b = min(mouth,eye//2,body)
eye-=b*2
mouth-=b
body-=b 

a = min(eye//2,body)
body-=a 

print(a+b+c)
