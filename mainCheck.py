import csv

file = open('input2.txt', "r", encoding="utf-8")
encods = [file.readline().rstrip().replace("\ufeff", ""), file.readline().rstrip(), file.readline().rstrip()]

s = ["", "", "", ""]
with open("table.csv", "r", newline="") as csv_file:
    reader = csv.reader(csv_file, delimiter=";")
    count = 0
    for row in reader:
        count += 1
        if count == 1:
            continue
        s[0] += row[0] + " "
        s[1] += row[1] + " "
        s[2] += row[2] + " "
        s[3] += row[3] + " "
        count += 1


def check(num):
    if s[num].find(encods[num-1]) != -1:
        print("столбик №%d верный" % num)
    else:
        print("в столбике №%d что-то не так, сравните (первая строка из input2.txt, вторая из таблицы)" % num)
        correct_array = encods[num-1].split()
        wrong_array = s[num].split()
        for i in range(min(len(correct_array), len(wrong_array))):
            if correct_array[i] == wrong_array[i]:
                print("   ", end='')
            else:
                print("!! ", end='')
        print()
        print(encods[num-1])
        print(s[num])
    print()


check(1)
check(2)
check(3)
