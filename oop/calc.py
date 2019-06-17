class calc():
    def add(self, a, b):
        return(a+b)
    def sub(self, a, b):
        return(a-b)
    def mul(self, a, b):
        return(a*b)
    def div(self, a, b):
        if b!=0:
            return (a/b)
        else:
            print('\n Cannot divide by zero!!!!!! \n')
        
calculator = calc()
print('Sum =',calculator.add(10,45))
print('Difference =',calculator.sub(10,45))
print('Multiplication =',calculator.mul(10,45))
print('Division =',calculator.div(10,11))