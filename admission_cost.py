# -*- coding: utf-8 -*-

age=input('age:')
if age.isdigit() == False:
    print('wrong')
else:
    age=int(age)
    if age<4:
        price=0
    elif age<18:
        price=5
    elif age<65:
        price=10
    elif age>=65:
        price=5
    print("Your admission cost is $"+str(price)+".")