import re; from collections import Counter; from prettytable import PrettyTable
table=PrettyTable(["Name","Frequency"])
[table.add_row([char,count]) for char , count in Counter(re.sub(r'[^\w]',"",input(""))).items()]
print(table)
