prompt = "Enter hours: "
hours = int(input(prompt))
prompt = "Enter rate: "
rate = float(input(prompt))

payment = 0
if hours <= 40:
    payment = hours * rate
elif hours > 40:
    diff = hours - 40
    payment = (hours - diff) * rate
    payment += (diff * (1.5 * rate))

print("Pay:", payment)