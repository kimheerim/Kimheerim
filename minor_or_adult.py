name = input("Enter your name: ")
while True:
    age_input = input("Enter your age: ")
    try:
        age = int(age_input)
        break
    except ValueError:
        print("Please enter a valid integer for age.")

if age >= 18:
    print(f"Hello {name}. You are an adult.")
else:
    print(f"Hello {name}. You are a minor.")
