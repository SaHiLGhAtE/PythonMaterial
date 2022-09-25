# def function_name_print(a,b,c,d):
#     print(a,b,c,d)
#
# function_name_print("Harry","Rohan","Hamad","Shivam")

def funargs(normal,*args,**kwargs):
    print(normal)
    for item in args:
        print(item)
    print("\nNow I would like to introduce some of our heroes")
    for key,value in kwargs.items():
        print(f"{key} is a {value}")

har=["Harry","Rohan","Hamad","Shivam","The programmer"]
normal="I am a normal argument and the students are:"
kw={"Rohan":"Monitor","Harry":"Fitness Instructor","Hamad":"Coordinator","Shivam":"Cook"}
funargs(normal,*har,**kw)
