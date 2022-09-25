list1 = ["harry", "carry", "larry", "marie"]
for item in list1:
    print(item)

list1 = [["harry", 1], ["carry", 2], ["larry", 3], ["marie", 4]]
for item in list1:
    print(item)

list1 = [["harry", 1], ["carry", 2], ["larry", 3], ["marie", 4]]
for item, lollypop in list1:
    print(item, "lolly is", lollypop)

list1 = [["harry", 1], ["carry", 2], ["larry", 3], ["marie", 4]]
dict1 = dict(list1)
print(dict1)

list1 = [["harry", 1], ["carry", 2], ["larry", 3], ["marie", 4]]
dict1 = dict(list1)
for item, lollypop in dict1.items():
    print(item, "and lolly is", lollypop)
