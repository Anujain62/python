
# python 3.10 introduced the match statement, which is similar to the switch statement found in other programming language.



def http_status(status):
 match status:
  case 200:
   return 'ok'
  case 404:
   return 'not found'
  case 500:
   return 'internal server error' 
  case _:
   return 'unknown status' 

print(http_status(509))











