# Error Handling
while True:
  try:
    x=int(input("What's your age?"))
    print(10/x)
  except ValueError:
    print("Please Enter a Number")
  except ZeroDivisionError:
    print("Please Enter a Number greater than 0")
  else:
    print("Thanks!")
    break