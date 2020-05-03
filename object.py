
class MyCalss:
    variable = "bash"

    def functionName(self):
        print("This is a message inside the class.")

myobjectx = MyCalss()
myobjecty = MyCalss()

myobjecty.variable = "Edison"

print(myobjectx.variable)
print(myobjecty.variable)
myobjectx.functionName()