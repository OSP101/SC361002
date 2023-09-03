scores = {
    "S321-6": 87,
    "S321-9": 54,
    "S321-7": 67,
    "S321-4": 65,
    "S321-1": 77,
    "S321-5": 91,
    "S321-3": 51,
    "S321-8": 89,
    "S322-0": 76,
    "S321-2": 80
}

odd_scores = {student_id: score for student_id, score in scores.items() if int(student_id[-1]) % 2 != 0}

if len(odd_scores) > 0:
    average_score = sum(odd_scores.values()) / len(odd_scores)
else:
    average_score = 0

print(f"Number of odd id = {len(odd_scores)}")
print(f"Odd id : {', '.join(odd_scores.keys())}")
print(f"Maximum score of odd id = {max(odd_scores.values()):.2f}")
print(f"Minimum score of odd id = {min(odd_scores.values()):.2f}")
