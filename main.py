#!/usr/bin/python3
# -*- coding: utf-8 -*-

# For embedded python
# from sys import path
# from os import getcwd
# path.append(getcwd())

from sys import exit, argv
from match_name import MatchIO
import subprocess
from json import loads
from datetime import datetime
from time import time


def timedelta_to_string(delta, pattern):
    d = {'d': delta.days}
    d['h'], rem = divmod(delta.seconds, 3600)
    d['m'], d['s'] = divmod(rem, 60)
    return pattern.format(**d)


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
            bootuptime = int(info.get("lastbootuptime")[6:-2]) / 1e3
            bootuptime = datetime.fromtimestamp(bootuptime)
            uptime = datetime.fromtimestamp(time()) - bootuptime
            result = "Имя компьютера: {}\n".format(info.get("csname"))
            result += "Дата последней загрузки: {}\n".format(bootuptime.strftime("%d.%m.%Y %H:%M:%S"))
            result += "Время работы: {}".format(timedelta_to_string(uptime, "{d}:{h}:{m}:{s}"))
            print(result)
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
