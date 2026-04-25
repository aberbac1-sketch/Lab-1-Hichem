# Lab-1-Hichem #
#This lab introduces basic Python programming through short exercises on strings, conditionals, input/output, and loops. Students should complete the core exercises first, then continue with the optional practice set if time permits.#

#Exercise C1#

print("I have eaten " + str(99) + " burritos.")
count = input("How many burritos did you eat? ")
print("I have eaten " + count + " burritos.")

#Exercise C2#

positive_count = 0
negative_count = 0
for i in range(10):
    number = int(input("Enter an integer: "))

    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1

choice = input("Type p for positive or n for negative: ")

if choice == "p":
    print("Positive numbers:", positive_count)
elif choice == "n":
    print("Negative numbers:", negative_count)
else:
    print("Invalid choice")

#Exercise C3#

for row in range(1, 5):
    print("#" * row)

for row in range(3, 0, -1):
    print("#" * row)
