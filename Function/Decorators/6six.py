def testCase(func):
    def inner(a,b):
        if b==0:
            print("b cant be 0")
        else:
            return func(a,b)

    return inner
    
@testCase
def calc(a,b):
    print(a/b)
    
calc(10,0)