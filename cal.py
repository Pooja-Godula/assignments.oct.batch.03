choice = int(input("Enter your choice:n"))  # User's choice[1,2,3,4]
if (choice>=1 and choice<=4):
  print("Enter two numbers: ")
  num1 = int(input())
  num2 = int(input())

  if choice == 1: # To add two numbers
     res = num1 + num2
     print("Result = ", res)

  elif choice == 2: # To subtract two numbers
     res = num1 - num2
     print("Result = ", res)

  elif choice == 3: # To multiply two numbers
     res = num1 * num2
     print("Result = ", res)

  elif choice == 4: # To get quotient with decimal value
    res = num1 / num2
    print("Result = ", res)

  elif choice == 5:
    exit()
else:
  print("Wrong input..!!")








list1=[1,2,3,4]
print("the list is",list1)
list1.append(5)
print("the list is",list1)
list1.clear()
print("the list is",list1)
list1.count(5)
print("the count is",list1)





string=("pooja g")
print("the name is",string)
string.capitalize()
print("the string is",string)
string.count(pooja)
print("the count is",string)





