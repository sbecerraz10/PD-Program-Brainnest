

def computePay(hours, rate):
    payment = 0
    try:
        hours = float(hours)
        rate = float(rate)
        if hours <= 40:
            payment = hours * rate
        elif hours > 40:
            diff = hours - 40
            payment = (hours - diff) * rate
            payment += (diff * (1.5 * rate))
    except ValueError:
        print('introduce numbers, please!')
    
    return payment


if __name__ == "__main__":
    prompt = "Enter hours: "
    hours = input(prompt)
    prompt = "Enter rate: "
    rate = input(prompt)
    payment = computePay(hours, rate)
    print("Pay:", payment)