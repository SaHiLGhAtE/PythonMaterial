# ls=[]
# for i in range(100):
#     if i%3==0:
#         ls.append(i)
#
# print(ls)

# ls=[i for i in range(100) if i%3==0]
# print(ls)

# dict1={i:f"item {i}" for i in range(1,10001) if i%100==0}
# dict1={i:f"item {i}" for i in range(5)}

# dict2={value:key for key,value in dict1.items()}
# print(dict1,"\n",dict2)
#
# dresses={dress for dress in ["dress1","dress2","dress1","dress2"]}
# print(dresses)
# print(type(dresses))

# evens=(i for i in range(100) if i%2==0)
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())

# for item in evens:
#     print(item)


no_of_list=int(input("How many items you want to add"))
input_string=input("Enter elements in list separated by space")
list=input_string.split()
t=int(input("which type of comprehention you want to use"))
if t==1:
    ls=[i for i in list]
    print(ls)
    print(type(ls))
elif t==2:
    dict1={f"item{i}":i for i in list}
    print(dict1)
    print(type(dict1))
elif t==3:
    s={i for i in list}
    print(s)
    print(type(s))

