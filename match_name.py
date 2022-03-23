#!/usr/bin/python3
# -*- coding: utf-8 -*-

from re import match

# Список выражений по которым проводится проверка
# По дефолту стоит регион R54, индекс 630300
default_expr_list = [
    [r"^[a-zA-Z]+\d+$", "R54-630300"],  # THE01
    [r"^\d+[a-zA-Z]+\d+$", "R54-"],  # 630300THE01
    [r"^[rR]\d*[-]\d+[a-zA-Z]+\d+$", ""]  # R54-630300THE01
]


class MatchIO:
    def __init__(self, expr_list=None):
        self.expr_list = expr_list is None and default_expr_list or expr_list

    def check_arm_name(self, pc_name):
        for r in self.expr_list:
            if match(r[0], pc_name):
                pc_name = "{}{}".format(r[1], pc_name)
                break
        if match(self.expr_list[2][0], pc_name):
            return pc_name
        return False
