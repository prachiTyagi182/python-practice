students = [
    {'name': 'Aman', 'marks': 78},
    {'name': 'Riya', 'marks': 92},
    {'name': 'Kabir', 'marks': 85},
    {'name': 'Zoya', 'marks': 67},
    {'name': 'Neha', 'marks': 92}
]

# Simple helper function marks nikalne ke liye
def get_marks(student):
    return student['marks']

# Marks ke hisaab se sort (sabse zyada se kam)
students.sort(key=get_marks, reverse=True)

# Top 3 print karein
print("Top Students:")
print("1.", students[0]['name'], "-", students[0]['marks'])
print("2.", students[1]['name'], "-", students[1]['marks'])
print("3.", students[2]['name'], "-", students[2]['marks'])