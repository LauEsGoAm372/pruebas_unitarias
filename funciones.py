def sumar(x,y):
    return x+y
    
print(sumar(2,4))

def es_primo(x):
   for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False
    #print("Es primo")
    return True