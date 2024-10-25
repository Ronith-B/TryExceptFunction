try:
  age = int(input("Enter your age "))
  if age>=18:
    print("You can Vote")
  else:
    raise ValueError
except ValueError:
    print("You can't vote")



try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input. Please enter a valid positive integer for age.")
    if age % 2 == 0:
        print("You are {age} years old, which is an even number.")
    else:
        print("You are {age} years old, which is an odd number.")
