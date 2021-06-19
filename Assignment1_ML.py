#Assignment1
################
##Q2.
print(5**9)
print(3//2)
print(7//3)
print(7/3)
print(6==6)

a=20
a+=30
a%=3
print(a)

print(True*False)
print(True & False)
print(True and False)

print(((6>3)and(7<4)or(18==3))and (9>3))

print(True is False)
print('False' in 'False')
print(((True == False)or (False>True)) and (False<=True))

##############################################

##Q3.
s1="Nice to have it"
s2= "here"
print(s1+''+s2)

################################################

##Q4.
a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2][0])

################################################

##Q5.
a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
s1="Nice to have it"
s2= "here"
a.append(s2)
a.insert(0,s1)
print(a)

################################################

##Q6.
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))

##############################################

##Q7.
str=input('Enter a string: ')
alphabet='abcdefghijklmnopqrstuvwxyz'
flag=True
for char in alphabet:
    if char not in str.lower():
        flag=False

if(flag==True):
    print('String is Pangram')
else:
    print('String is not Pangram')

############################################

##Q8.
n=input('Enter an Integer:')
value=eval('{0}+{0}{0}+{0}{0}{0}'.format(n))
print(value)

#############################################

##Q9
w=input("Enter some words: ")
a=w.split(',')
a.sort()
print(a)

##############################################

##Q10.

d = {'Student': ['Rahul', 'Kishore','Vidhya', 'Raakhi'],'Marks':[57,87,67,79]}
d['Marks']
max(d['Marks'])
print(d['Student'][d['Marks'].index(max(d['Marks']))])









