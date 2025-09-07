# import random

# def pizza():
#     piza= ["peperoni" , "garlick stake" , "meet and mashrooms"]
#     A=random.choice(piza)
#     print (A,"pizza")
# pizza()
# def taklif(num1, num2):
#     print(int(num1 + num2))

# taklif(5, 8)

# def dama (c):
#     d=31
#     print(d * 1.8 +32)
#     return 87.8

# dama(c)


# def mostatil(tol, arz):
#     t=int(input("andaze tol ro bego?"))
#     a=int(input("andaze arz ro bego?"))
#     masahat=(t*a)
#     mohit=(t+a )*2
#     return t*a
# def contdown():
#     number = input("ADADIRO mikhai")
#     shomaresh=len(number-1)
#     print(shomaresh)
# contdown()

# def countdown(adad):
#     for i in range(adad - 1):
#         print(i)

# countdown(10)


# def countdown(number):
#     for i in range(number, 0, -1):
#         print(i)
#     print("شمارش تمام شد!")
# countdown()

# def countdown(number):
#     for i in range(number, 0, -1):
#         print(i)
#     print("boom")
# user_input = input("adad bego ")
# try:
#     number = int(user_input)
#     countdown(number)
# except ValueError:
#     print("adad bego")

# import turtle
# pen =turtle.Turtle()
# def moraba(andaze):
#     for i in range(4):
#       pen.forward(andaze)  
#       pen.right(90)
#       print()
# moraba(int(input("andaze bego:")) )
# turtle.done()
import random 
def foodchoice():
    fud=["pizza" , "pasta" , "spaghetti" , "sandwich"]
    pick = random.choice(fud)
    print(pick)
foodchoice("salam")
