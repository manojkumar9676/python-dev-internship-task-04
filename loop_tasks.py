# loop_tasks.py
# Task 4: Loops & Iterations
# Python Developer Internship

print("1. For loop: Print numbers from 1 to 100")
for i in range(1, 101):
    print(i, end=" ")
print("\n")

print("2. While loop: Countdown timer")
count = 5
while count > 0:
    print("Countdown:", count)
    count -= 1
print("Countdown finished!\n")

print("3. break and continue example")
for i in range(1, 11):
    if i == 5:
        continue  # skip 5
    if i == 9:
        break     # stop at 9
    print(i)
print()

print("4. Iterating over string characters")
name = "Python"
for ch in name:
    print(ch)
print()

print("5. Multiplication table of 5")
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print()

print("6. range() with steps (even numbers)")
for i in range(2, 21, 2):
    print(i, end=" ")
print("\n")

print("7. Loop with conditions (find even & odd)")
for i in range(1, 11):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")
print()

print("8. Real-world example: Password attempts")
attempts = 3
while attempts > 0:
    print("Attempts left:", attempts)
    attempts -= 1
print("Account locked!")
