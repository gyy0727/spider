import re
res=re.match('[a-zA-Z_]+[/w]*','_name')
print(res.group())