import re
message = "We can be reached at (322) 593-5370 and (602) 456-6935"
data = re.findall(r"\(\d{3}\) \d{3}-\d{4}", message)
print(data)