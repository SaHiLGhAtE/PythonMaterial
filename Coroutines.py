import time
# def searcher():
#     # Some 4 seconds time consuming task
#     book="This is a book on Harry and Code with Harry"
#     time.sleep(4)
#
#     while True:
#         text=(yield)
#         if text in book:
#             print("Your text is in the book")
#         else:
#             print("Text is not in the book")
#
# search=searcher()
# print("Search started")
# next(search)
# print("Next method run")
# search.send("Harry")
# input("Press any key")
# search.send("Harry and")

# Challenge
def name_searcher():
    name_searcher="Sahil Shubham Soham"
    time.sleep(2)

    while True:
        text=(yield)
        if text in name_searcher:
            print("Name is in the list")
        else:
            print("Name is not in the list")

name=name_searcher()
next(name)
name.send(input("Enter ur name"))
input("press any key")
name.send("Soham")




