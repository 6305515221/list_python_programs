#['213423M75234', '23455M90324', '134543M4023']
'''
l=input().split()
s=[]
for j in l:
    s.append(j)
print(s)
c=0
d=[]
for i in s:
    a=i.split('M')
    b=a[1][:2]
    if(int(b)>60):
        c+=1
        d.append(i)
print(c,d)
'''
#['213423M75234', '23455f90324', '134543f4023']
'''
l=input().split()
s=[]
for i in l:
    s.append(i)
print(s)
c=0
for j in s:
    for k in j:
        if(k.isalpha()):
            a=j.index(k)
            b=j[a+1:a+3]
            if(int(b)>60):
                c+=1
print(c)
'''
#find single element
'''
l=input().split()
s=[]
for i in l:
    s.append(i)
print(s)
d={}
for j in s:
    if(j in d):
        d[j]+=1
    else:
        d[j]=1
for char,count in d.items():
    if(count==1):
        print(char)


output:1 1 2 2 4 3 3
['1', '1', '2', '2', '4', '3', '3']
4


def single_element(n):
    d={}
    for i in n:
        if(i in d):
            d[i]+=1
        else:
            d[i]=1
    for char,count in d.items():
        if(count==1):
            print(char)
            
n=input().split()
single_element(n)

'''
#input:-2
'''
9
16
sum=9+16=25
25 is perfect square so its yes else no
n=int(input())
s=0
for i in range(n):
    a=int(input())
    s+=a
print(s)
l=[]
for j in range(1,s**2):
    b=j*j
    l.append(b)
if(s in l):
    print("YES")
else:
    print("NO")
'''
