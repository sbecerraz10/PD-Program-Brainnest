def grade(score):
    grade = ''
    try:
        score = float(score)
        if score >= 0.0 and score <= 1.0:
            if score >= 0.9:
                grade = 'A'
            elif score >= 0.8:
                grade = 'B'
            elif score >= 0.7:
                grade = 'C'
            elif score >= 0.6:
                grade = 'D'
            elif score < 0.6:
                grade = 'F'
        else:
            raise Exception("Sorry, the score is out of range(0.0 and 1.0)") 
    except ValueError: 
        print("Only float values are allowed")

    return grade
        


if __name__ == "__main__":
    prompt = "Enter a score: "
    score = input(prompt)
    score_grade = grade(score)
    print("Score grade:", score_grade)