#int
#float
#complex

x=1 #int
y=1.0 #float
z=1j #complex

print(type(x))
print(type(y))
print(type(z))

"""
Output
<class 'int'>
<class 'float'>
<class 'complex'>
"""

d= """convert from int to float"""
print(d)
a=float(x)
print(a)
e="""convert float to int"""
print(e)
b=int(y)
print(b)
f="""convert int to complex"""
print(f)
c=complex(x)
print(c)