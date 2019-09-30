#!/usr/bin/python
# -*- coding: utf-8 -*-
from enum import Enum

class ScriptType(Enum):
    T_BASE = 0
    T_COMMON = 1

class VarType(Enum):
    T_INVALID = -1
    T_TABLE = 0
    T_STRING = 1
    T_NUMBER = 2
    T_INT = 3
    T_DOUBLE = 4
