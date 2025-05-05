def func1(arg1):
    print("Function 1 is called with argument:", arg1)

def func2(func, arg2=10):
    func(arg2)

func2(func1, 30)