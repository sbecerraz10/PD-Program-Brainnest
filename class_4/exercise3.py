import re

text = "Count how many words I have!"
matches = re.findall(r'\w+', text)
num_words = len(matches)
print(num_words)