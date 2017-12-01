# -*- coding: utf-8 -*-

current_users=['Daniel','Jane','Wenny','Eric','Liz']
new_users=['DANIEL','jane','Michael','Arrow']
for new_user in new_users:
    if new_user.title() in current_users:
        print(new_user+" USED!")
    else:
        print("WELCOME! "+new_user)