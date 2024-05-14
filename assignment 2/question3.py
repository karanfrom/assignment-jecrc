# Given the list fruits = ['apple', 'banana', 'cherry', 'date'], how would you
# access the “na” from the ‘banana’? after that change it in upper case like “NA”

fruits=['apple','banana','cherry','date']
substring=fruits[1][2:4]
print(substring)
print(substring.upper())