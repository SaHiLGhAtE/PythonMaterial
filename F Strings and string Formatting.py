import math

me="Sahil"
a1=3
# a="this is %s %s"%(me,a1)
a="this is {} {}"
b=a.format(me,a1)
print(b)
a=f"this is {me} {a1} {math.cos(65)}"
print(a)

import time
value=time.process_time()
a=f"this is fstring {value}"
print(a)



