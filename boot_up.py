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
    comp_name = input("\nВведите имя ПК (пр. R54-630300THE01, Ctrl+C для выхода):\n> ")
    for r in expr_list:
        if match(r[0], comp_name):
            comp_name = "{}{}".format(r[1], comp_name)
            break
    if match(expr_list[2][0], comp_name):
        subprocess.Popen("powershell -ExecutionPolicy Unrestricted -Command \"Get-CimInstance -ClassName win32_operatingsystem -ComputerName "+comp_name+" | select csname, lastbootuptime\"").wait()
    else:
        print("Имя компьютера не распознано! Попробуйте еще раз.")
    main()  # Рекурсия наше все!...


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
