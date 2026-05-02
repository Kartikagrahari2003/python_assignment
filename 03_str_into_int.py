# Q. Switch one string value with one integer value
n1 = 200
char2 = "java"

# print data type
print(type(n1),type(char2))
# ext = external variables for data handling

ext = n1
n1= char2
char2= ext

print(f"{n1},{char2}")