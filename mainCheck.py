import csv

file = open('input2.txt', "r", encoding="utf-8")
encod1 = file.readline().rstrip().replace("\ufeff", "")
encod2 = file.readline().rstrip()
encod3 = file.readline().rstrip()

s0, s1, s2, s3 = "", "", "", ""
with open("table.csv", "r", newline="") as csv_file:
    reader = csv.reader(csv_file, delimiter=";")
    count = 0
    for row in reader:
        count += 1
        if count == 1:
            continue
        s0 += row[0] + " "
        s1 += row[1] + " "
        s2 += row[2] + " "
        s3 += row[3] + " "
        count += 1

if s1.find(encod1) != -1:
    print("первый столбик верный")
else:
    print("в первом столбике что-то не так, сравните (первая строка из input2.txt, вторая из таблицы)")
    correct_array = encod1.split()
    wrong_array = s1.split()
    for i in range(min(len(correct_array), len(wrong_array))):
        if correct_array[i] == wrong_array[i]:
            print("   ", end='')
        else:
            print("!! ", end='')
    print()
    print(encod1)
    print(s1)
print()

if s2.find(encod2) != -1:
    print("второй столбик верный")
else:
    print("во втором столбике что-то не так, сравните (первая строка из input2.txt, вторая из таблицы)")
    correct_array = encod2.split()
    wrong_array = s2.split()
    for i in range(min(len(correct_array), len(wrong_array))):
        if correct_array[i] == wrong_array[i]:
            print("   ", end='')
        else:
            print("!! ", end='')
    print()
    print(encod2)
    print(s2)
print()

if s3.find(encod3) != -1:
    print("третий столбик верный")
else:
    print("в третьем столбике что-то не так, сравните (первая строка из input2.txt, вторая из таблицы)")
    correct_array = encod3.split()
    wrong_array = s3.split()
    for i in range(min(len(correct_array), len(wrong_array))):
        if correct_array[i] == wrong_array[i]:
            print("   ", end='')
        else:
            print("!! ", end='')
    print()
    print(encod3)
    print(s3)

