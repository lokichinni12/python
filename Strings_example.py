mystring="hello world"
#Print Complete string
print(mystring)
print(mystring[::])

#indexing of string
print(mystring[0])
print(mystring[4])

#slicing
print(mystring[1:7])
print(mystring[0:10:2])

# Methods
print(mystring.upper())
print(mystring.split())

#formatting
print("hello world {},".format("Loki"))
print("hello world {}, {}, {}".format("Loki", "INSERTING", "NEWFORMATTING"))
print("hello world {1}, {2}, {0}".format("By Loki", "INSERTING", "NEWFORMATTING"))
