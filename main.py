#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import exit, argv
from match_name import MatchIO
import subprocess
from json import loads
from datetime import datetime


def main():
    pc_name = input("\nВведите имя ПК (пр. R54-630300THE01, Ctrl+C для выхода):\n> ").strip()
    f_pc_name = matchio.check_arm_name(pc_name)
    if f_pc_name:
        # C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe
        # or
        # powershell
        (result, err) = subprocess.Popen(
            "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe -ExecutionPolicy Unrestricted -Command \"Get-CimInstance -ClassName win32_operatingsystem -ComputerName "+f_pc_name+" | select csname, lastbootuptime | ConvertTo-Json\"",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True).communicate()
        if debug is True:
            print("result: {}".format(result), "\n", "err: {}".format(err))
        if not err:
            info = loads(result)
            bootuptime = int(info.get("lastbootuptime")[6:-2])
            bootuptime = datetime.fromtimestamp(bootuptime / 1e3)
            print("Имя компьютера: {}\nДата последней загрузки: {}".format(info.get("csname"), bootuptime.strftime("%d.%m.%Y %H:%M:%S")))
        else:
            print("Произошла ошибка! Попробуйте еще раз.")
    else:
        print("Имя компьютера не распознано! Попробуйте еще раз.")
    main()  # Рекурсия наше все!...


if __name__ == '__main__':
    try:
        if len(argv) > 1:
            debug = argv[1].strip() == "debug"
        matchio = MatchIO()
        main()
    except KeyboardInterrupt:
        exit()
