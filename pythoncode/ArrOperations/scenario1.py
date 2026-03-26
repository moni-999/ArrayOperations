import numpy as np

# Step 1: Enter marks of 3 students in 3 subjects
print("Enter internal marks for 3 students (3 subjects each)")

marks = np.zeros((3, 3))

for i in range(3):
    print(f"\nEnter marks for Student {i+1}")
    for j in range(3):
        marks[i][j] = float(input(f"  Subject {j+1}: "))

print("\nMarks Matrix (Students × Subjects):")
print(marks)

# Step 2: Calculate total marks for each student
total_marks = np.sum(marks, axis=1)

# Step 3: Bonus rule
# If total >= 240 → bonus = 10
# Else if total >= 180 → bonus = 5
# Else → bonus = 0

bonus = np.zeros(3)

for i in range(3):
    if total_marks[i] >= 240:
        bonus[i] = 10
    elif total_marks[i] >= 180:
        bonus[i] = 5
    else:
        bonus[i] = 0

# Step 4: Final marks after adding bonus
final_marks = total_marks + bonus

# Step 5: Display Student Report
print("\n-------- STUDENT REPORT --------")

for i in range(3):
    print(f"\nStudent {i+1}")
    print("Subject Marks:", marks[i])
    print("Total Marks :", total_marks[i])
    print("Bonus       :", bonus[i])
    print("Final Marks :", final_marks[i])

# Step 6: Subject-wise average
subject_average = np.mean(marks, axis=0)

print("\nSubject-wise Average Marks:")
for i in range(3):
    print(f"Subject {i+1}: {subject_average[i]:.2f}")

print("\nAll calculations completed successfully ✅")