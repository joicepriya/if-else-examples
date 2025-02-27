#own examples:
'''
books=("GOODNIGHTNOON","THEGRATESTORIESFORCHILDREN","THECATINTHEHAT","THESECRETGARDEN","HARRYPOTTER")
print(books)
your_books=input("enter the boook name:").upper()

if your_books in books:
    print("your book is availble")
else:
    print("your book is not available")
'''
'''
Brand_A=input("enter the brand A name:")
Brand_B=input("enter the brand B name:")

if Brand_A and Brand_B:
    print("same brand names")
else:
    print("enter the same name")

'''
'''
age=int(input("enter yoour age:"))
if age>=20 or age<=50:
    print ("your are enligble for join the meeting")
else:
    print("your not eligible for meeting")
'''

'''
number=int(input("enter the number:"))

if number %2 == 0:
    print("this is even number")
else:
    print("this is not even number")

'''
'''
foods=["dosa","idly","idiyappam","pongal","chappathi"]
your_chooice=input("enter your dish:")

if your_chooice  not in foods:
    print(f"{your_chooice} is not in the list")
else:
    print(f"{your_chooice} is in the list ")
 '''   

# google examples:
'''
a = input("enter the number:")
b = input("enter the number:")

if a == b:
    print("a is equal to b")
else:
    print("a is not equal to b")
'''
'''
a = 5
b = 8

if a == 5 or b == 10:
    print("At least one condition is True")
else:
    print("Both conditions are False")
'''
'''
user_input = "password123"
correct_password = "password456"

if user_input != correct_password:
    print("Incorrect password!")
else:
    print("Correct password!")
'''
'''
fruits = ["apple", "banana", "cherry"]

fruit = "banana"

if fruit in fruits:
    print(f"{fruit} is in the list!")
else:
    print(f"{fruit} is not in the list!")
'''
password = "1234"

if password == "password123":
    print("Access granted.")
else:
    print("Access denied.")
