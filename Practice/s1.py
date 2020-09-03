x = 20    #having global scope
def f1():
    x = 30      
    def f2():
        nonlocal x
        x = 40    #accessing x belonging to f1()
        print(x)
    f2()
    print(x)
f1()
print(x)