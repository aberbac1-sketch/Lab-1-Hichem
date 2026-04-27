positive_count = 0
negative_count = 0

for i in range(10): 
 number = int(input("Enter an integer: "))
 
 if number > 0:
    positive_count += 1
 elif number < 0:
    negative_count += 1
    
print("Positive numbers:", positive_count)
print("Negative numbers:", negative_count)

choice = input("Type p for positive or n for negative: ")

if choice == "p": print("Positive numbers:", positive_count)
elif choice == "n": print("Negative numbers:", negative_count)
else: print("Invalid choice")