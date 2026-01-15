# student_scores_v2.py
# Collect N student scores, validate input, print report + stats

names = []
scores = []

n = int(input("How many students? "))

for _ in range(n):
    name = input("Enter student name: ")

    score = float(input("Enter student score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Score must be between 0 and 100.")
        score = float(input("Enter student score (0-100): "))

    names.append(name)
    scores.append(score)

print("\n--- Report ---")
for i, name in enumerate(names, start=1):
    print(f"{i}. {name} - {scores[i-1]}")

avg = sum(scores) / len(scores)
highest = max(scores)
lowest = min(scores)

print(f"\nAverage score: {avg:.2f}")
print(f"Highest score: {highest}")
print(f"Lowest score: {lowest}")

top_index = scores.index(highest)
top_student = names[top_index]
print(f"Top student: {top_student} ({highest})")

