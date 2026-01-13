names = []
scores = []

name = input("Enter student name: ")
score = float(input("Enter student score: "))
names.append(name)
scores.append(score)

name = input("Enter student name: ")
score = float(input("Enter student score: "))
names.append(name)
scores.append(score)

name = input("Enter student name: ")
score = float(input("Enter student score: "))
names.append(name)
scores.append(score)

print("\n--- Report ---")
for i, name in enumerate(names, start=1):
    print(f"{i}. {name} - {scores[i-1]}")

avg = sum(scores) / len(scores)

print(f"Average score: {avg:.2f}")
print(f"Highest score: {max(scores)}")
print(f"Lowest score: {min(scores)}")

