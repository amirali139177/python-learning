# file= open("text.txt" , "r")
# print(file.read())

with open("text.txt" , "r") as file:
    print(file.read())

file.close()