import json

with open("class_7\students.json", "r") as file:
    data = json.load(file)
    students_json = data
    print(students_json)

    for student in students_json['students']:
        avg = sum(student['grades']) / len(student['grades'])
        student['average_grade'] = avg
        
    class_average = sum([student['average_grade'] for student in students_json['students']]) / len(students_json['students'])
    for student in students_json['students']:
        if student['average_grade'] > class_average:
            student["above_average"] = True
        else:
            student["above_average"] = False
    
    print(f"These are the students: {students_json}")
    




#list(map(lambda x: sum(students_json[x])/len(students_json[x]), students_json))