try:
    age = int(input("How old are you?"))

except ValueError:
    print("type a numerical number, not in words.")
    age = int(input("How old are you?"))

if age > 18:
    print("You can drive at age {age}.")
