dict_student = {
    "001": {"gender": "F", "GPA": 3.50},
    "003": {"gender": "M", "GPA": 3.28},
    "004": {"gender": "M", "GPA": 2.75},
    "005": {"gender": "F", "GPA": 3.21},
    "006": {"gender": "M", "GPA": 2.62},
    "007": {"gender": "F", "GPA": 3.00},
    "008": {"gender": "F", "GPA": 2.30}
}

male_count = 0
female_count = 0
total_gpa = 0.0

for student_id, student_info in dict_student.items():
    if student_info["gender"] == "M":
        male_count += 1
    elif student_info["gender"] == "F":
        female_count += 1
    total_gpa = total_gpa + student_info["GPA"]
    print(student_info)

average_gpa = total_gpa / len(dict_student)

print(f"There are {len(dict_student)} students")
print(f"Female = {female_count}")
print(f"Male = {male_count}")
print(f"Average GPA = {average_gpa:.2f}")
