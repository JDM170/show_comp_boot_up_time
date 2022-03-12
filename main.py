#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import exit
from re import match
from subprocess import Popen


# Список выражений по которым проводится проверка
# По дефолту стоит регион R54, индекс 630300
expr_list = [
    [r"^[a-zA-Z]+\d+$", "R54-630300"],  # THE01
    [r"^\d+[a-zA-Z]+\d+$", "R54-"],  # 630300THE01
    [r"^[rR]\d*[-]\d+[a-zA-Z]+\d+$", ""]  # R54-630300THE01
]


def main():
    pc_name = input("\nВведите имя ПК (пр. R54-630300THE01, Ctrl+C для выхода):\n> ").strip()
    for r in expr_list:
        if match(r[0], pc_name):
            pc_name = "".join([r[1], pc_name])
            break
    if match(expr_list[2][0], pc_name):
        Popen("powershell -ExecutionPolicy Unrestricted -Command \"Get-CimInstance -ClassName win32_operatingsystem -ComputerName "+pc_name+" | select csname, lastbootuptime\"").wait()
    else:
        print("Имя компьютера не распознано! Попробуйте еще раз.")
    main()  # Рекурсия наше все!...


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
