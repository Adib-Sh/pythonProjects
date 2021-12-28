
import re



regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,6}$' 
def check(email):

    if(re.search(regex, email)):
        return True 
    else:
       return False

email = input()

if check(email)==False:
    print('WRONG')
else:
    print('OK')

   
    
