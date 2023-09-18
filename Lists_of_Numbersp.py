list_numeros = []
number = None

print("Enter a list of numbers, type 0 when finished. ")

while number != 0:
    number = int(input("Enter number: "))
    if number != 0:
        list_numeros.append(number)
         
for i in list_numeros :
    number += i
print (f'The sum is: {number}')
l = len(list_numeros)
ave = number / l
print (f'The average is: {ave:.2f}')
maxn = max(list_numeros)
print (f'The largest number is: {maxn}')
