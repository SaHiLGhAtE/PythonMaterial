import json
data='{"var1":"sahil","var2":56}'
print(data)

parsed=json.loads(data)
print(parsed["var1"])

# task1=json.load
# It used to read the json document from file

data2={"channel_name":"CodeWithHarry",
       "cars":['Bmw','audi','ferrari'],
       "fridge":('roti',540)
       }