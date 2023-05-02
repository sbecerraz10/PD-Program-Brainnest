
def feeling():
    day_time = ["morning", "afternoon", "evening", "night"]
    for i in range(len(day_time)):
        print(f"+ Good {day_time[i]}! \n+ How are you feeling?")
        feeling = input()
        print(f"R./ I'm happy to hear that you're feeling {feeling} .")


if __name__ == "__main__":
    feeling()
