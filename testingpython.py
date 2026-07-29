"""learning Def"""
#อันแรกก
#def hello(name):
#    var = "hello " + name
#    return var
#print(hello("Auj"))
##output: hello Auj


#อันสอง

#def double(x):
#    return x*2
#print(double(5))
##output: 10


#อันสาม

#def is_even(x):
#    if x % 2 ==0:
#        return True
#    else:
#        return False

#print(is_even(8))
#print(is_even(5))
##output: True
##output: False

#อันสี่

def bigger(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    elif a == b:
        return a

print(bigger(5,8))
print(bigger(20,5))
print(bigger(10,10))
