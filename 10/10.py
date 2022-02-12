from textwrap import wrap

chars = []
letters = []
numbers = []
binary = []
binary_2 = []
numbers_2 = ""
numbers_3 = []
decimal = []
n = 2
even = 0
division_3 = 0
division_5 = 0 
division_7 = 0
even_percentage = 0
division_3_percentage = 0 
division_5_percentage = 0
division_7_percentage =  0
length = 0

#read file
with open('data.txt', 'r') as file:
    data = file.read().rstrip()

#split the text to a list with individual words
chars = data.split()
for i in range(len(chars) - 1):
    letters.append(list(chars[i]))

#convert each ascii character to number
for i in range(len(letters) - 1):
    for j in range (len(letters[i]) - 1):
        numbers.append(ord(letters[i][j]))

#convert each number to binary number
for i in range(len(numbers) - 1):
    binary.append(bin(numbers[i]))

#choose first two and last two digits from each binary number
for i in range(len(binary) - 1):
    two = binary[i][2:4] + binary[i][-2:]
    binary_2.append(two)

#make the list with digits a list with one long string
numbers_2 = "".join(binary_2)
#split the string at each 16 digits
numbers_3 = wrap(numbers_2,16)

#convert each 16 digits to a list with numbers in the decimal number system
for i in range(len(numbers_3) - 1):
    decimal.append(int(numbers_3[i],n))

length = len(decimal)

#check
for i in range(len(decimal)):
    #even numbers
    if decimal[i] % 2 == 0:
        even +=1
    #divided by 3
    if decimal[i] % 3 == 0:
        division_3 +=1
    #divided by 5
    if decimal[i] % 5 == 0:
        division_5 +=1
    #divided by 7
    if decimal[i] % 7 == 0:
        division_7 +=1

#percentages
even_percentage = ((length - even) / length) * 100 
division_3_percentage = ((length - division_3) / length) * 100
division_5_percentage = ((length - division_5) / length) * 100
division_7_percentage = ((length - division_7) / length) * 100

print(str(even_percentage) + "% are even")
print(str(division_3_percentage) + "% are divided by 3")
print(str(division_5_percentage) + "% are divided by 5")
print(str(division_7_percentage) + "% are divided by 7")












