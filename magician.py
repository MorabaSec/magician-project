secret_number = 777
 


secret_number = int(input("enter an integer number:"))

while secret_number:
    if secret_number == 777:
        print("Well done, muggle! You are free now")
    elif secret_number:
     if secret_number > 777:
        print("Ha ha! you're stuck in my loop")
    else:
      if secret_number != 777:
        print("Ha ha you're stuck in my loop")
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")