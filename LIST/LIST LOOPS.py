# create a list with elements and it's index and datatype in tuple (index, datatype
'''
s=[1,"pavan",[10,20],(1,2)]
#s=input("enter the string").split()
for i in s:
    print(((type(i),s.index(i))))

'''
# create a list with index and last char elements
'''
a=input().split()
for i in a:
    print(a.index(i),i[len(i)-1])
output:pavan kumar
0 n
1 r
'''
#print positive number until negative number
'''
l=[1,2,3,-1,4]
for i in l:
    if(i<0):
        break
    else:
        print(i)
'''
#common elements of 2 lits
'''
l=[1,2,3,4]
l1=[5,6,1,2]
l2=[]
for i in l:
    if(i in l1):
        l2.append(i)
print(l2)
'''
#maximum number in a list
'''
l=[1,2,3,4,5]
m=max(l)
print(m)

#or
l=[1,2,3,4,5]
a=l[0]
for i in l:
    if(i>a): 
        a=i
print(a)
'''

#secong largest element in a list
'''
l=[2,3,1,4,7,5,7,7,7]
a=sorted(l)
print(a)
d=[]
for i in a:
    if(i not in d):
        d.append(i)
print(d[len(d)-2])
'''
#to get half length list
'''
s=input().split()
a=len(s)
if(a%2!=0):
    a=a+1 
b=int(a/2)
print(s[:b])
#or
s=input().split()
a=len(s)
b=a//2
print(s[:b+1])
'''
#first half of numbers in a list
'''
n=input().split()
a=len(n)
if(a%2!=0):
    a+=1 
b=int(a/2)
c=n[:b]
L=[]
for i in c:
    L.append(int(i))
print(L)
'''
'''
n=input().split() #['1', '2', '3']
m=input().split() #['4', '5', '6']
a=m[::-1] #['6', '5', '4']
l=[]
for i in range(len(n)):
    print(n[i]+' '+a[i])
1 6
2 5
3 4
'''
#last half of the list
'''
n=int(input())
L=[]
for i in range(n):
    a=int(input())
    L+=[a]
print(L)
b=n/2
if(b%2==0):
    print(l[b:])
else:
    c=n+1
    b=int(c/2)
print(L[b:])
'''
#l=['pavan','kumar','python']
#output:   ['nohtyp','ramuk','navap']
'''
l=['pavan','kumar','python']
r=[]
for i in l:
    rev=i[0:len(i)][::-1]
    r.append(rev)
print(r[::-1])
'''

#most repeat element in list
'''
l=[1,2,34,1,2,2,3,1,2,2,7]
d={}
for i in l:
    if(i in d):
        d[i]+=1
    else:
        d[i]=1
print(d)
a=max(d.values())
for char,count in d.items():
    if(a==count):
        print(char)
output:{1: 3, 2: 5, 34: 1, 3: 1, 7: 1}
2 5
'''
########
'''
d=['hi','hello',10,'12.3',12,19,6.2]
for i in d:
    if(isinstance(i,int)):
        print(i,end=" ")
    elif(isinstance(i,float)):
        print(i,end=" ")
output:10 12 19 6.2
'''
######
'''
L=['apple','78','970.03']
n=int(input())
for i in range(n):
    m=input()
    L+=[m]
print(L)
output:
n=2
m=38 graphes
['apple', '78', '970.03', '38', 'grapes']
'''
######
'''
n = int(input())
L = []
for i in range(n):
    j = input()
    L = [j] + L # it gives char and space like [[new],[old]] 
print(L)
for k in L:
    print(k)

output:
n=5 we enter 5 names and these five names are given bottom to top
'''
########
'''
n=int(input())
m=int(input())
a=[]
for i in range(n):
    b=int(input())
    a.append(b)
print(a)
for j in range(m):
    x=int(input())
    print(a[x])
output:
n=4
m=2
b repeate n times
prints list a
j repeats m times
x are the index values with m times
4
2
1
2
3
4
[1, 2, 3, 4]
1
2
3
4
'''
#######
'''
n=int(input())
a=[]
for i in range(n):
    b=int(input())
    a=a+[b]
print(a[0:2]+a[len(a)-2:])

output
6
1
2
39
4
5
6
[1, 2, 5, 6]
'''
######
'''
a=int(input())
l=[]
for i in range(a):
    b=int(input())
    l.append(b)
print(l)
d={}
for j in l:
    if(j in d):
        d[j]+=1
    else:
        d[j]=1
for k,count in d.items():
    if(count>1):
        print("True")
        break
    else:
        print("false")
        break
output: if the element is repeated twice it prints true ortherwise false
4
1
2
3
1
[1, 2, 3, 1]
True
'''
#####
'''
n=input().split()
l=[]
for i in n:
    l.append(int(i))
print(l)
a=int(''.join(n))+1
b=str(a)
l=[]
for i in b:
    l.append(i)
print(l)
    
output:
1 2 3
[1, 2, 3]
['1', '2', '4']

9
[9]
['1', '0']
'''
#second element i in every element in the list
'''
l=[1,12,123,114]
l1=[]
for i in l:
    l1+=[str(i)]
for j in l1:
    if(len(j)==1):
        print(0)
    else:
        print(j[1])
'''
#middle value in every element
'''
s=['pavan','kumar','jagadesh']
for i in s:
    a=len(i)//2
    b=len(i)
    if(b%2==0):
        print(i[a-1:a+1])
    else:
        print(i[a])
'''

#remove the depulicate elements
'''
a=input().split()
s=set()
for i in a:
    s.add(i)
print(' '.join(s))

output:
1 2 3 4 1
2 3 4 1

#it removes duplicate char
a=input().split()
d=[]
for i in a:
    if(i in d):
        d.remove(i)
    else:
        d.append(i)
print(' '.join(d))

output:
1 2 3 1 4
2 3 4
'''
#Given a Python list, write a program to remove all occurrences of item 20
'''
l=[5, 20, 15, 20, 25, 50, 20]
a=[]
for i in l:
    if(i==20):
        pass
    else:
        a+=[i]
print(a)
'''
#replace 20 with 200
'''
l=[5, 20, 15, 20, 25, 50, 20]
a=[]
for i in l:
    if(i==20):
        a.append(200)
    else:
        a+=[i]
print(a)
'''
#Write a program to add item 7000 after 6000 in the following Python List

'''
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# understand indexing
# list1[0] = 10
# list1[1] = 20
# list1[2] = [300, 400, [5000, 6000], 500]
# list1[2][2] = [5000, 6000]
# list1[2][2][1] = 6000

# solution
list1[2][2].append(7000)
print(list1)
'''

#[45,45,45] true and 45,45,6,7,8 [6,7,8]
'''
s=input().split(',')
l=[]
for i in s:
    l.append(int(i))
print(l)
s=set()
a=l[0]
for j in l:
    if(j==a):
        s.add("TRUE")
    else:
        s.add(j)
if(len(s)==1):
    print("TRUE")
else:
    b=[]
    for k in s:
        if(k!="TRUE"):
            b.append(k)
    print(b)
'''
##if sum = given number print it as tuple
'''
l=input().split(',')
a=[]
for k in l:
    a.append(int(k))
n=int(input()) #12
p=set()
s=set()
for i in a: #[5,3,4,9,7,5]
    num=n-i
    if(num in s):
        p.add((min(i,num),max(i,num)))
    else:
        s.add(i)
for j in p:
    print(j)



output:
5,3,4,9,7,5
12
(3, 9)
(5,7)
'''

    
#######
'''
l=input().split(',')
n=int(input())
a=[]
for k in l:
    a.append(int(k))
print(a) #[1, 2, 3, 4, 5]
l=[]
l.append(a[n:])
l.append(a[:n])
b=[]
for i in l:
    for j in i:
        b.append(j)
print(b)
'''

#iterations
'''
l=input().split(',')
n=int(input())
a=[]
for i in l:
    a.append(int(i))
for j in range(1,n+1):
    a=a[1:]+a[:1]
print(a)
 output:
3,4,5,6
6
[5, 6, 3, 4]

'''
#missing numbers
'''
n=input().split(',')
l=[]
for i in n:
    l.append(int(i))
print(l)
a=len(l)+1
t=a*(a+1)//2
s=sum(l)
miss=t-s
print(miss)


n=input().split(',')
l=[]
for i in n:
    l.append(int(i))
#print(l)
a=l[0]
b=l[-1]
#print(b)
l1=[]
for j in range(a,b+1):
    l1.append(j)
#print(l1)
c=sum(l)
d=sum(l1)
print(d-c)
'''
#######
'''
n=input().split()
m=int(input())
l=[]
for i in n:
    l+=[int(i)]
    a=sorted(l,reverse=True)
    b=a[:m]
s=' '
for j in b:
    s=str(j)+' '+s
print(s)
'''
###merge sorted array
'''
num1=[0]#[1,2,3,0,0,0]
num2=[1]#[2,5,6]
m=int(input())
n=int(input())
a=num1[:m]
b=num2[:n]
print(sorted(a+b))
'''
#[0, 1, 3, 0, 4, '-', '-', '-']
'''
num=input().split(',')
val=int(input())
l=[]
for i in num:
    l.append(int(i))
for j in l:
    if(val in l):
        l.remove(val)
print(l,len(l))
a=len(num)-len(l)
b=a*['-']
print(l+b)
'''
#########
'''
n=[0,1,2,2,3,0,4,2]
val=2
w=0
for i in range(len(n)):
    if(n[i]!=val):
        n[w]=n[i]
        w+=1
for i in range(w,len(n)):
    n[i]='-'
print(n)
'''
##1,1,2
#[1, 2, '-']
'''
n=input().split(',')
l=[]
a=set()
for i in n:
    l.append(int(i))
for j in l:
    a.add(j)
    b=list(a)
    d='-'
    c=(len(n)-len(b))*'-'
    b.append(c)
print(b)
'''
#profit or lose
'''
p=[7,1,5,3,6,4]
n=int(input())
m=int(input())
a=p[n]
b=p[m]
if((b-a)>0):
    print(b-a)
else:
    print('0')
'''
#n=3 we give three inputs among them we print max of that inputs
'''
n=int(input())
a=[]
for i in range(n):
    b=[]
    c=input().split()
    for j in c:
        b.append(int(j))
    a.append(max(b))
print(a)

output:
3
1 2 3 4
10 20 30 
5
[4, 30, 5]
'''
#in a list any two elements are equal to h print in tuple form
'''
s=input().split(',')
h=int(input())
a=[]
for i in s:
    a.append(int(i))
b=set()
for j in a:
    for k in a:
        if(j+k==h):
            b.add((min(j,k),max(j,k)))
for c in b:
    print(c)

output;
5,3,7,9,5
12
(3, 9)
(5, 7)
'''
#n=[1,2,3,4]
#m=[2,4,1,3]
'''
n=[3,7,9]
m=[3,7,11]
a=m[:3][::-1]
m[:3]=a
b=m[1:3][::-1]
m[1:3]=b
c=m[2:][::-1]
m[2:]=c
if(m==n):
    print('TRUE')
else:
    print("false")
'''
#xyzABC and abcd
'''
n=ord(input())
m=int(input())
l=[]
for i in range(ord('A'),ord('z')):
    l.append(chr(i))
l1=[]
for j in l:
    if j.isalpha():
        l1.append(ord(j))
a=0
for k in l1:
    if(n==k):
        a=l1.index(k)
        c=a+(m+1)
        b=l1[a+1:c]
if(len(b)==m):
    for h in b:
        print(chr(h),end='')
else:
    d=m-len(b)
    e=b+l1[:d]
    for m in e:
        print(chr(m),end=' ')
'''
