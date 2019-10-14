#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
用于Fsm的npc创建
"""
from Entity.Statement.Statement import *
from Entity.Statement.StatementReturn import *
from Entity.Variable.Variable.Variable import *
from Define.EditorDefine import VarType

fsm_npc_table_name = "FsmNpcObjTable"


class StatementFsmNpc(StatementReturn):

    def __init__(self, statement_name, params):
        ret_var = Variable(fsm_npc_table_name, VarType.T_TABLE, {})
        StatementReturn.__init__(self, True, ret_var, statement_name, params)

