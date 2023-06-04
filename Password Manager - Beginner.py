#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add():
    name = input('Account Name: ')
    pwd = input('Password: ')
    with open('passwords.txt', 'a') as f:
        f.write(name + '|' + pwd )
                
# with function mostly used as substitute for try/finally and w: write over, r: read only, a: check if exists and create if not              

def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            data = line
            user,passw = data.split('|')
            print('user:',user,',''password:',passw)

while True:
    mode = input('Would you like to add new Password or View the existing one? (Add/View) or Q to quit').lower()
    if mode == 'q':
        break
    elif mode == 'add':
        add()
    elif mode == 'view':
        view()
    else:
        ('Please type add to create a new Password or view to view a existing one or Q to quit.')
        
print('Thanks!')        

