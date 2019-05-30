

from __future__ import annotations

"""
Basic transition system as computation model
2 dimensions :
  - compute (CPU time) -> transitions are function calls
  - storage (Memory space) -> transitions are maps

These are somewhat equivalent in theory, although not in application.

if the function calls are pure mathematical functions, memoizing (caching) is a way to trade one for the other.
It has however various limitations.
"""
import functools
import inspect
from typing import Callable, Iterable, Deque, Mapping, Dict
from collections import deque


class Process:
    """
    Representing deterministic computation with a usual purely functional model.
    Useful lambda in python talk from D. Beazley https://www.youtube.com/watch?v=pkCLMl0e_0k
    Category Theory / Grue's Map Theory are our guides.

    This functional model can be implemented in various ways.
    Lambda expression is one, but there can be more (mappings from one value to another for instance)

    Using python operational semantics, two interacting concept need to be represented here:
    - Container of the computation (expression not yet evaluated)
    - Iterator of the computation (evaluation of the expression)

    Ref: https://docs.python.org/3/library/stdtypes.html#iterator-types

    TODO : Implicit memoization for optimization.
    TODO : Control Theory needed to make choice between memory and compute power needed
    TODO : See Virtual Machine concepts...
    """


    class Expression:
        repr: str
        fun: Callable

        def __init__(self, fun: Callable, repr: str=None):
            self.fun = fun
            self.repr = repr if repr is not None else inspect.getsource(self.fun)

        def __call__(self, arg):
            """
            Enforcing one arg only call.
            Keep the compute model simple, until we get proper computational typing in place to compare programs.
            """
            try:
                return functools.partial(self.fun, arg)  # partial application for one argument semantics
            except Exception as e:
                raise e

        def __eq__(self, other):
            """
            A notion of equality for our programs.
            ie. the good point of having a uniform lambda process model, there is a common type (TBD)
            :param other:
            :return:
            TODO : define a computational type for expression
            """

            # fill up arguments

            return self.fun(1) == other.fun(1)
        #
        # def __iter__(self) -> Iterable[Callable]:
        #     return Process.Evaluation(self)

        def __repr__(self):
            return self.repr


if __name__ == '__main__':

    # Testing Expression

    TRUE = Process.Expression(lambda x, y: x, repr='\\xy.x')
    FALSE = Process.Expression(lambda x, y: y, repr='\\xy.y')

    # validating equality of expression

    assert TRUE == TRUE
    assert FALSE == FALSE

    # computing in Bool

    T = Process.Bool(TRUE)
    F = Process.Bool(FALSE)

    assert T and T == T
    assert T and F == F
    assert F and T == F
    assert F and F == F

    assert T or T == T
    assert T or F == T
    assert F or T == T
    assert F or F == F









