import random
import string
import re

# =============================================================================
# Random Password Generator and Validator
# =============================================================================
class Password:
    def Generator():
        combination  = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.sample(combination,random.randint(8,20)))
        return password
    def Validator(password):
       reg = "^.*(?=.{8,20})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!#$%&'()*+, -./:;<=>?@[\]^_`{|}~]).*$"
       comp = re.compile(reg)
       validator = re.search(comp,password)
       if validator:
           return True
       else:
           return False

sample = Password.Generator()
print(sample)
print(Password.Validator(sample))