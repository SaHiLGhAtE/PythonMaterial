# class Dad:
#     basketball=1
#
# class Son(Dad):
#     dance=1
#     def isdance(self):
#         return f"Yes I dance {self.dance} no of times"
#
# class Grandson(Son):
#     dance=5
#     def isdance(self):
#         return f"Jackson Yeah!" \
#                f"Yes I dance very awesomely {self.dance} times"
#
# darry=Dad()
# larry=Son()
# harry=Grandson()
#
# print(harry.isdance())
# print(harry.basketball)


class ElectronicDevice:
    tv=1

class PocketGadget(ElectronicDevice):
    mobile=1
    def ismobile(self):
        return f"Mobile is Pocket Gadget"

class Phone(PocketGadget):
    screen=1
    def isscreen(self):
        return f"Phone has one screen"

harry=ElectronicDevice()
larry=PocketGadget()
sarry=Phone()

print(sarry.isscreen())
print(sarry.ismobile())
print(harry.tv)

