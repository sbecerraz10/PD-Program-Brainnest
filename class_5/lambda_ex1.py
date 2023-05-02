list = ["I am the goat", "Every day I'm better", "I'm a perfection seeker"]
print([(lambda a=list[x]: a.upper())() for x in range(len(list))])
