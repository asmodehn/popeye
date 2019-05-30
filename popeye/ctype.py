"""
Representing a type as a function.
Type represent interaction with environment.
"""
from __future__ import annotations
from typing import Bool, Callable

import enum
import prompt_toolkit

from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import CompleteStyle










def ismemberof(value, type) -> Bool:
    return isequalvalue(value, value, type)

def istype(maybe_type) -> Bool:
    return isequal(maybe_type,maybe_type)


def isequalvalue(me, other, type) -> Bool:
    return ismemberof(me, type) and ismemberof(other, type) and isequalvalue(me, other)


def behaves(program, type) -> Bool:
    pass



BoolCType = {TT, FF}

boolvalue = TT

assert behaves()


natvalue = 42



program = lambda x: x +1



highorderprogram = lambda x: lambda y: x + y






if __name__ == '__main__':

    ctt = CTType('CTT', 'B')


    ctt('not B so prompt')

    #ctt = ctt + 'B' + int



    #BorC = typing.NewType('BorC', CTType() )

    #CandD = CTType('C') * CTType('D')


    #td = BorC('WrongSoPrompt')
    #assert td == BorC.C



