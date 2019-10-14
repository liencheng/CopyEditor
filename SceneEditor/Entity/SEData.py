#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
编辑器基础数据
"""


class SEData:
    script_id = 0


def set_script_id(script_id):
    SEData.script_id = script_id


def get_script_id():
    return SEData.script_id


def wrap_name(name):
    return "x" + str(SEData.script_id) + "_" + str(name)
