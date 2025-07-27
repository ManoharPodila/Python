
student_id = input("Enter Your ID: ")
student_name = input("Enter Your Name: ")
attendance = float(input("Enter Your Attendance (%): "))

total_score = 0
subject_count = 0

while True:
    subject_count += 1
    score = int(input(f"\nEnter score for Subject {subject_count}: "))
    total_score += score

    choice = input("Do you want to enter another score? (yes/no): ").lower()
    if choice != "yes":
        break

average_score = total_score / subject_count

if average_score >= 85:
    performance = "Excellent"
elif average_score >= 70:
    performance = "Good"
elif average_score >= 50:
    performance = "Average"
else:
    performance = "Needs Improvement"

if attendance < 75:
    attendance_status = "WARNING - Low Attendance"
else:
    attendance_status = "Attendance Satisfied"

print("\n===== STUDENT DETAILS ======")
print("Student ID:", student_id)
print("Student Name:", student_name)
print("Student Attendance:", str(attendance) + "%")
print("Total Score:", total_score)
print("Total Number Of Subjects:", subject_count)
print("Average Score:", round(average_score, 1))
print("Performance:", performance)
print("Attendance:", attendance_status)
