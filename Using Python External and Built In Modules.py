#using python external and built in modules
import random
random_number=random.randint(0,1)
print(random_number)

rand=random.random()*100
print(rand)

lst=["star plus","aaj tak","dd1"]
choice=random.choice(lst)
print(choice)

import math
a=math.factorial(5)
print(a)
b=math.floor(5.233)
print(b)

from datetime import date
date=date.today()
print(date)