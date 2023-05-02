import re
message = "Find me in the site: https://www.arealhero.com"
url = re.findall(r'(https?://\S+)', message)
print(url)