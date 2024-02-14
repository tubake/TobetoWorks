#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.

# h = float(input("Enter your height in meters: \n"))
# w = float(input("Enter your weight in kg: \n "))
# bmi = float(w / (h*h) )

# print("Body Mass Index:", bmi)



# #2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.
# salary = float(input("Enter your salary: \n"))
# raiseRate = float(input("Enter the raise rate: \n"))
# increasedSalary = float(salary * raiseRate / 100 + salary)
# print(increasedSalary)

# 3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.
# firstNum = int(input("Please enter the first number: \n"))
# secondNum = int(input("Please enter the second number: \n"))
# thirdNum = int(input("Please enter the third number: \n"))
# Maxnum=max(firstNum, secondNum, thirdNum)
# print("Max number:", Maxnum)


# 4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)
# import math
# radius = float(input("Input the radius of the circle : \n "))
# area = math.pi * radius ** 2
# perimeter = 2 * math.pi * radius
# print("Area of the circle:", area)
# print("Perimeter of the circle:", perimeter)


#5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
 
number=input("Please Enter Number:  \n") 
reverseNum = number[::-1]
if number == reverseNum:
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")


