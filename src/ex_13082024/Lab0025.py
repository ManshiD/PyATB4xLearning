# Strings
name="Pramod"
# Str
print(type(name))
print(name.upper())
print(name.lower())
print(len(name))

a="90"
age=90
print(type(a))
print(type(age))

name_new = "This is a Big line"
print(name_new)
name_new=name_new+str(1)
print(name_new)

first_name="Pramod"
last_name="Dutta"
full_name=first_name+last_name #Concatenation
print(full_name)

how_many_planes_i_have = None
print(type(how_many_planes_i_have)) #NoneType
# None concept is not present in Python it is present in Java

val = 0 # This is int
# id
age=10
age2=10
print(id(age)) # 140736741636824 id of the object they are not same
print(id(age2)) # 140736741636824

age=10
age2=11
print(id(age)) # 140736741636824 id of the object as the value is not changed its same
print(id(age2)) # 140736741636856 id of the object as the value is changed its same