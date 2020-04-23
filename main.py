import csv

file = open('input.txt', "r", encoding="utf-8")
encoding = file.readline().rstrip()
string = file.readline()

table = [[''] * 4 for i in range(len(string) + 1)]
table[0][0] = "Символ"
table[0][1] = encoding.upper()
table[0][2] = "UTF-8"
table[0][3] = "UTF-16BE"

count = 1
for char in string:
    table[count][0] = char
    table[count][1] = str(char.encode(encoding))[1::].strip("'").replace("\\x", " ").upper().strip()
    table[count][2] = str(char.encode("UTF-8"))[1::].strip("'").replace("\\x", " ").upper().strip()
    table[count][3] = str(char.encode("UTF-16BE"))[1::].strip("'").replace("\\x", " ").upper().strip()
    if ord(char) < 128:
        table[count][1] = hex(ord(char))[2::].upper()
        table[count][2] = hex(ord(char))[2::].upper()
        table[count][3] = "00 " + hex(ord(char))[2::].upper()
    if len(table[count][3].split()[0]) != 2:
        table[count][3] = table[count][3][:2] + " " + hex(ord(table[count][3][2]))[2::].upper()
    count += 1

for line in table:
    print(line)

with open("table.csv", "w", newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=";")
    for line in table:
        writer.writerow(line)
print("Итог работы программы в файле table.csv")
