# create a robot name like RX837 or BC811
# Two uppercase letter followed by 3 numbers

import string
import random

def robotName():
    names = []
    letters = string.ascii_uppercase
    numbers = string.digits
    num = "".join(random.choice(letters) for i in range (2))
    let = "".join(random.choice(numbers) for i in range (3))
    name = num + let
    if name not in name:
        names.append(name)
        return name
    else:
  
