def fakultet(n):
    if n == 0:
        return 1 
    return n * fakultet(n-1)

"""result = fakultet(4)"""
"""4*3*2*1 = 24"""

#1
def countdown(n):
    if n == 0:
        return print(0)
    print(n)
    countdown(n-1)

#countdown(10)

#2
def decimal_till_binär(n):
    #Basfall: Om talet är lika med 0, retuneras "0" för första anropet annars ""
    if n == 0:
        return "0"
    else:
        return decimal_till_binär(n // 2) + str(n % 2) if n > 1 else "1"

#resultat = decimal_till_binär(11)
#print(resultat)

#3
def mul(a,b):
    if b == 1:
        return a
    return a + mul(a,b-1)

#result = mul(3,4)
#print(result)

#4
def fib(n):
    if n <= 1:
        return 1

    return fib(n-1) + fib(n-2)

result = [fib(i) for i in range (10)]
print(result)
