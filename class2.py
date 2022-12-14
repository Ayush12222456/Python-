def func1(param1):
    def func2(param2):
        return param1.upper()+param2.lower()
    return func2
y=func1('Compter')
print(y('Science'))