# character-table-opd5

Генератор таблицы исходной строки в разных кодировках для 5 лабы по опд

## Проверяйте результаты тут https://dencode.com/string

## Как использовать?
В файл input.txt необходимо ввести 2 строчки: кодировка и строка, выданная преподавателем,  проверки вводимых нет.

Запускаете. Результат выводится в консоль, таблица будет лежать в файле table.csv

# ВАЖНО
лично у меня питон не адекватно переводил в UTF-16BE, поэтому в коде присутствуют костыли. Я НЕ РУЧАЮСЬ ЗА ПРАВИЛЬНОСТЬ ТАБЛИЦЫ.

кодировку в первой строке нужно вводить так, чтобы понял питон. 
КОИ-8 он не принимает, нужно koi8-r. Остальные кодировки (Windows-1251, ISO-8859-5) вроде работают как в генираторе

## Советую проверить результаты тут https://dencode.com/string

## Кoстыли
можете пробовать убирать по одному или оба if, у кого-то может работать адекватно.
```py
    if ord(char) < 128:
        table[count][1] = hex(ord(char))[2::].upper()
        table[count][2] = hex(ord(char))[2::].upper()
        table[count][3] = "00 " + hex(ord(char))[2::].upper()
    if len(table[count][3].split()[0]) != 2:
        table[count][3] = table[count][3][:2] + " " + hex(ord(table[count][3][2]))[2::].upper()
```
