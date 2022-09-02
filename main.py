#!/usr/bin/python3
# -*- coding: utf-8 -*-

# For embedded python
# from sys import path
# from os import getcwd
# path.append(getcwd())

from sys import exit, argv
from m_match_name.main import MatchIO
import subprocess
from json import loads
from datetime import datetime
from time import time

is_debug = False


def timedelta_to_string(delta, pattern):
    d = {'d': delta.days}
    d['h'], rem = divmod(delta.seconds, 3600)
    d['m'], d['s'] = divmod(rem, 60)
    for key, value in d.items():
        if len(str(value)) == 1:
            d[key] = "0" + str(value)
    return pattern.format(**d)


def main():
    global is_debug
    pc_name = input("\nВведите имя ПК (пр. R54-630300THE01, Ctrl+C для выхода):\n> ").strip()
    f_pc_name = matchio.check_pc_name(pc_name)
    if f_pc_name:
        # C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe
        # or
        # powershell
        (result, err) = subprocess.Popen(
            "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe -ExecutionPolicy Unrestricted -Command \"Get-CimInstance -ClassName win32_operatingsystem -ComputerName "+f_pc_name+" | select csname, lastbootuptime | ConvertTo-Json\"",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True).communicate()
        if is_debug is True:
            print("result: {}".format(result), "\n", "err: {}".format(err))
        if not err:
            info = loads(result)
            bootuptime = int(info.get("lastbootuptime")[6:-2]) / 1e3
            bootuptime = datetime.fromtimestamp(bootuptime)
            uptime = datetime.fromtimestamp(time()) - bootuptime
            result = "Имя компьютера: {}\n".format(info.get("csname"))
            result += "Дата последней загрузки: {}\n".format(bootuptime.strftime("%d.%m.%Y %H:%M:%S"))
            result += "Время работы (д:ч:м:с): {}".format(timedelta_to_string(uptime, "{d}:{h}:{m}:{s}"))
            print(result)
        else:
            print("Произошла ошибка! Попробуйте еще раз.")
    else:
        print("Имя компьютера не распознано! Попробуйте еще раз.")
    main()  # Рекурсия наше все!...


if __name__ == '__main__':
    try:
        if len(argv) > 1:
            is_debug = argv[1].strip() == "debug"
            # is_debug = argv[1].strip() == "debug" if len(argv) > 1
        matchio = MatchIO()
        main()
    except KeyboardInterrupt:
        exit()
