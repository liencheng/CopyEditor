#!/usr/bin/python
# -*- coding: utf-8 -*-
from Define.EditorDefine import VarType

b_init: bool = False
fun_factory = {}

def build_local_var_table(script_id, name):
    ret = "local" + " " + str(script_id) + name + "={}"
    return ret

def build_local_var_simple(script_id, name):
    ret = "local" + " " + str(script_id) + name
    return ret

def build_local_var_string(script_id, name):
    return build_local_var_simple(script_id, name)

def build_local_var_double(script_id, name):
    return build_local_var_simple(script_id, name)

def build_local_var_float(script_id, name):
    return build_local_var_simple(script_id, name)

def build_local_var_int(script_id, name):
    return build_local_var_simple(script_id, name)

def build_local_var_number(script_id, name):
    return build_local_var_simple(script_id, name)

def build_variable(script_id, var_type, var_name, default_value):
    func = fun_factory.get(var_type)
    if func:
        return func(script_id, var_name)

    return "info:build_variable error"

def build_block_for(items):
    """
    :param items:
    :return:
    for i,v in pairs(items) do

    end
    """
    pass

def register(value_type, func):
    fun_factory[value_type] = func

def register_factory():
    register(VarType.T_TABLE, build_local_var_table)
    register(VarType.T_STRING, build_local_var_string)
    register(VarType.T_NUMBER, build_local_var_number)
    register(VarType.T_INT, build_local_var_int)
    register(VarType.T_DOUBLE, build_local_var_double)


def init():
    b_init = True
    register_factory()


if ~b_init:
    init()
    print("hello variableutile.py init.")

print("hello variableutile.py")