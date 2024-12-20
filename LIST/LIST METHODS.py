'''
a=input("enter the string:\n")
b=input("enter the string2:\n")
c=a*3
d=b*3
print(a+b)
print(c)
print(d)
print(c+d)


a=int("enter the name:\n")
b=int(input("enter the value:\n"))
print(a+b)

'''


'''
l=str([23,45,12,895,34,23])
print(l)  #[23, 45, 12, 895, 34, 23]


l=['23',24,3+0j,False]
print(l)  #['23', 24, (3+0j), False]

#convert string to list
l="pavan"
print(list(l))  #['p', 'a', 'v', 'a', 'n']

#tuple to list
print(list(("banglore",34,4.5)))
#['banglore', 34, 4.5]


print(list({'banglore':45,34:45,4.5:True}))  #['banglore', 34, 4.5] In dict it gives by default key values

'''

'''
l=[23,45,12,895,34,23]
print(l[3])
print(l[1:4])
'''



'''
l=['23',[45,12,'895'],34.5,23,3+6j,False]
print(l)
print(l[1][2][2],l[-5])
print(l[0][1])


'''

'''
#program to get even index element
l=['23',[45,12,'895'],34.5,23,3+6j,False]
print(l)
print(l[::2])#program to get even index element
print(l[1::2])#program to get odd index element
print(l[::-1])#program to reverse the list
print(l[-2::-2])#program to get even index element in reverse order
print(l[-1::-2])#program to get odd index element in reverse order

'''

'''
l=['23',[45,12,'895'],34.5,23,3+6j,False]
#[45,12,'895'] in reverse
print(l[1][::-1])  #['895', 12, 45]
#'23' reverse
print(l[0][::-1])  #32
print(l[2:5])
print(l[4:2:-1])
print(l[:4:3])
'''

'''
l=['23',[45,12,'895'],34.5,23,3+6j,False]

print(1[:3:2]+l[3])

'''


'''
l=[45,3.5,2.3,"hey",[True,False]]
l[3]="HEy"
print(l)
#[45, 3.5, 'HEy', 'hey', [True, False]]

l[:2]=[3,7]
print(l)
l[2:]="apple"
print(l)
l[2:]=['apple']
print(l)
'''

#Append
'''
l=[2,34.5,'pavan',{1,2,3,4},[True,False]]
l.append(3+0j)
print(l)   #[2, 34.5, 'pavan', {1, 2, 3, 4}, [True, False], (3+0j)]
'''


#extend   it unpack the elements

l=[2,34.5,'pavan',{1,2,3,4},[True,False]]
l.extend('hai')
l.extend(['hai',45,False,7.8])
print(l)      #[2, 34.5, 'pavan', {1, 2, 3, 4}, [True, False], 'h', 'a', 'i', 'hai', 45, False, 7.8]




#insert   we can add any valu like integer and flaot in anu place
'''
l=[2,34.5,'pavan',{1,2,3,4},[True,False]]

l.insert(0,"kumar")  #['kumar', 2, 34.5, 'pavan', {1, 2, 3, 4}, [True, False]]
l.insert(4,45)  #['kumar', 2, 34.5, 'pavan', 45, {1, 2, 3, 4}, [True, False]]
print(l)     


'''

#pop
'''
l=[1,2,3,4,5,67]
l.pop(2)
print(l)


'''


#remove
'''
l=[1,2,3,4,5,6,7,3]
l.remove(3)
print(l)


'''


#del
'''
l=[1,2,3,4,5,6]
del l[2]    #[1, 2, 4, 5, 6]
del l[0:2]    #[3, 4, 5, 6]

print(l)

'''



#reverse
'''
l=[1,2,"45",[1,2,3],True,False]
l.reverse()
print(l)
'''



#index
'''
l=[1,2,0,"45",[1,2,3],True,False]
print(l.index(2))   #1
print(l.index(False))  #2
print(l.index(False,3))  #6

#count
l=[1,2,0,"45",[1,2,3],True,False]
print(l.count(1))#2
print(l.count([2,31,]))  #0
'''


'''
a=input("enter the string:\n")
b=input("enter the string2:\n")
c=a*3
d=b*3
print(a+b)
print(c)
print(d)
print(c+d)


a=int("enter the name:\n")
b=int(input("enter the value:\n"))
print(a+b)

'''


'''
l=str([23,45,12,895,34,23])
print(l)  #[23, 45, 12, 895, 34, 23]


l=['23',24,3+0j,False]
print(l)  #['23', 24, (3+0j), False]

#convert string to list
l="pavan"
print(list(l))  #['p', 'a', 'v', 'a', 'n']

#tuple to list
print(list(("banglore",34,4.5)))
#['banglore', 34, 4.5]


print(list({'banglore':45,34:45,4.5:True}))  #['banglore', 34, 4.5] In dict it gives by default key values

'''

'''
l=[23,45,12,895,34,23]
print(l[3])
print(l[1:4])
'''





'''
l=['23',[45,12,'895'],34.5,23,3+6j,False]
print(l)
print(l[1][2][2],l[-5])
print(l[0][1])


'''

'''
#program to get even index element
l=['23',[45,12,'895'],34.5,23,3+6j,False]
print(l)
print(l[::2])#program to get even index element
print(l[1::2])#program to get odd index element
print(l[::-1])#program to reverse the list
print(l[-2::-2])#program to get even index element in reverse order
print(l[-1::-2])#program to get odd index element in reverse order

'''

'''
l=['23',[45,12,'895'],34.5,23,3+6j,False]
#[45,12,'895'] in reverse
print(l[1][::-1])  #['895', 12, 45]
#'23' reverse
print(l[0][::-1])  #32
print(l[2:5])
print(l[4:2:-1])
print(l[:4:3])
'''

'''
l=['23',[45,12,'895'],34.5,23,3+6j,False]

print(1[:3:2]+l[3])

'''


'''
l=[45,3.5,2.3,"hey",[True,False]]
l[3]="HEy"
print(l)
#[45, 3.5, 'HEy', 'hey', [True, False]]

l[:2]=[3,7]
print(l)
l[2:]="apple"
print(l)
l[2:]=['apple']
print(l)
'''

#Append
'''
l=[2,34.5,'pavan',{1,2,3,4},[True,False]]
l.append(3+0j)
print(l)   #[2, 34.5, 'pavan', {1, 2, 3, 4}, [True, False], (3+0j)]
'''


#extend   it unpack the elements
'''
l=[2,34.5,'pavan',{1,2,3,4},[True,False]]
l.extend('hai')
l.extend(['hai',45,False,7.8])
print(l)      #[2, 34.5, 'pavan', {1, 2, 3, 4}, [True, False], 'h', 'a', 'i', 'hai', 45, False, 7.8]
'''



#insert   we can add any valu like integer and flaot in anu place
'''
l=[2,34.5,'pavan',{1,2,3,4},[True,False]]

l.insert(0,"kumar")  #['kumar', 2, 34.5, 'pavan', {1, 2, 3, 4}, [True, False]]
l.insert(4,45)  #['kumar', 2, 34.5, 'pavan', 45, {1, 2, 3, 4}, [True, False]]
print(l)     


'''

#pop
'''
l=[1,2,3,4,5,67]
l.pop(2)
print(l)


'''


#remove
'''
l=[1,2,3,4,5,6,7,3]
l.remove(3)
print(l)


'''


#del
'''
l=[1,2,3,4,5,6]
del l[2]    #[1, 2, 4, 5, 6]
del l[0:2]    #[3, 4, 5, 6]

print(l)

'''



#reverse
'''
l=[1,2,"45",[1,2,3],True,False]
l.reverse()
print(l)
'''



#index
'''
l=[1,2,0,"45",[1,2,3],True,False]
print(l.index(2))   #1
print(l.index(False))  #2
print(l.index(False,3))  #6

#count
l=[1,2,0,"45",[1,2,3],True,False]
print(l.count(1))#2
print(l.count([2,31,]))  #0
'''



#sort
'''
l=[3,4,12,4.5,78,0,2]
l.sort()   #[0, 2, 3, 4, 4.5, 12, 78]
print(l)
l.sort(reverse=True)  #[78, 12, 4.5, 4, 3, 2, 0]
print(l)



l=['apple','APPLE','grapes','van','Ta',"avocado"]
l.sort() #['APPLE', 'Ta', 'apple', 'avocado', 'grapes', 'van']
print(l)
l.sort(reverse=True)
print(l)

l=[3+2j,4+2j+1+2j]
l.sort()
print(l)  #error



l=['3+2j','4+2j','1+2j']
l.sort()   #['1+2j', '3+2j', '4+2j']
print(l)
'''


#copy:- Shallow copy and deep copy 











