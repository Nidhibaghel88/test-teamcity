x = 0
while x < 20:
    x = x + 1
    if x % 2 == 0:
        continue
    print(x)

# Print even number
x = 0
while x < 20:
    x = x + 1
    if x % 2 != 0:
        continue  # continue wont allow rest of below statement to get execute
    print(x)

# Print with -end
set1 = []
set1 = [
    [1, 2, 3, 4, 5],
    [5, 6, 7, 8, 6],
    [1, 2, 3, 4, 7],
    [0, 0, 0, 0, 8]
]
for x in set1:
    for y in x:
        print(y, end=' ')

# convert list to string

list1 = ['Nidhi', 'Neha', 'Niti']
string1 = ' '.join(list1)
print("\n", string1)
