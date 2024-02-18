# 1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.

# Program to display the Fibonacci sequence up to n-th term

# nterms = int(input("How many terms? "))

# # first two terms
# n1, n2 = 1, 1
# count = 0

# # check if the number of terms is valid
# if nterms <= 0:
#    print("Please enter a positive integer")
# # if there is only one term, return n1
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# # generate fibonacci sequence
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        # update values
#        n1 = n2
#        n2 = nth
#        count += 1


# fibonacci = [1, 1]
# while len(fibonacci) < 20:
#     fibonacci.append(fibonacci[-1] + fibonacci[-2])

# print(fibonacci)

# 2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.
# (Arş. Mükemmel sayı?)
# Kendisi hariç bütün pozitif bölenlerinin toplamı kendisine eşit olan sayılara mükemmel sayı denir.
# 6 bir mükemmel sayıdır. Çünkü 6’nın pozitif bölenleri 1,2,3 ve 6’dır. Kendisi hariç diğer bölenlerini toplarsak 1+2+3=6 eder.
# Bunun gibi 28 de mükemmel sayıdır. 28 = 1 + 2 + 4 + 7 + 14

# num = int(input("Please enter a number:"))
# total=0
 
# for i in range(1,num):
#     if(num%i == 0):
#         total +=i
        
# if(num == total):
#     print("is the perfect number.")
# else:
#     print("is not the perfect number.")

# 3- Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.
# import math
# firstNum = int(input("Please enter the first number : "))
# secondNum = int(input("Please enter the second number : "))
# ebob=math.gcd(firstNum,secondNum)
# ekok=(firstNum*secondNum)/ebob 
# print ("EBOB:", ebob)
# print ("EKOK:", ekok)

       
# 4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.

# num=int(input("Please enter a number : "))
# if num > 1:
   
#    for i in range(2,num):
#        if (num % i) == 0:
#            print(num," is not a prime number.")
#            break
#    else:
#        print(num," is a prime number.")
 
# else:
#    print(num," is not a prime number.")

# 5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 
num = int(input("Please enter a number: "))
factor = 2
print(num, "prime factors of a number:")
while factor <= num:
    if num % factor == 0:
        print(factor)
        num //= factor
    else:
        factor += 1