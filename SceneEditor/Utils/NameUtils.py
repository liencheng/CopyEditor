#!/usr/bin/python
# -*- coding: utf-8 -*-

def encode_func_name(script_id, raw_name):
    ret = str(script_id)
    ret = "x" + ret
    ret = ret + "_"
    ret = ret + str(raw_name)
    return ret

def encode_var_name(script_id, raw_name):
    ret = str(script_id)
    ret = "x" + ret
    ret = ret + "_"
    ret = ret + str(raw_name)
    return ret


