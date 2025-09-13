# Student grades dictionary
grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78}

print("Grade Tracker")
print("Students:", grades)

# Calculating average grade
average = sum(grades.values()) / len(grades)
print("Average grade:", average)

# Finding highest scorer
highest_student = max(grades, key=grades.get)
print(f"Highest scorer: {highest_student} ({grades[highest_student]})")

# Finding lowest scorer
lowest_student = min(grades, key=grades.get)
print(f"Lowest scorer: {lowest_student} ({grades[lowest_student]})")
