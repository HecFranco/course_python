# Completa el ejercicio aquí
# range(0, 101, 2)

suma = sum( range(0, 101, 2) )
print(suma)

# Segunda forma con bucles
num = 0
suma = 0

while num <= 100:
    if num % 2 == 0:
        suma += num
    num += 1
    
print(suma)
# 2550
# 2550