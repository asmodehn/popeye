

from __future__ import annotations

import functools
import inspect
import random
from typing import Callable, Iterable, Deque, Mapping, Dict, Set
from collections import deque

import hypothesis as hypothesis


class LambdaChar:
    """
    Representing deterministic computation with a usual purely functional model.
    Useful lambda in python talk from D. Beazley https://www.youtube.com/watch?v=pkCLMl0e_0k

    This functional model can be implemented in various ways.
    Lambda expression is one, but there can be more (mappings from one value to another for instance)

    We will compute on character values only for simplicity at first.
    """
    repr: str
    fun: Callable

    def __init__(self, repr, fun: Callable = None):
        self.repr = repr
        # Using identity morphism relaying on representation in char for equality
        self.fun = fun if fun is not None else lambda: self.repr


    def __call__(self, *args):
        """
        Enforcing one arg only call.
        Keep the compute model simple, until we get proper computational typing in place to compare programs.
        """
        try:
            return functools.partial(self.fun, *args)  # partial application for one argument over multi arg lambdas
        except Exception as e:
            raise e

    def __eq__(self, other):
        """
        A notion of equality for any (possibly untyped) programs.
        ie. the good point of having a uniform lambda process model, there is a concet of overall common type (universe?) (TBD)
        :param other:
        :return:
        TODO : define a computational type for expression
        """

        return self.fun() == other.fun()


    def __ne__(self, other):
        """
        Refining the opposite of equality.
        NOT requires some amount of computation, ie state to be stored, somehow...
        :param other:
        :return:
        """

        return self.fun() != other.fun()

    def __aiter__(self):
        pass

    def __anext__(self):


    def __repr__(self):
        return self.repr



def scheduler(perfsafe: float):
    """scheduling performance/safety ratio (0..1)"""

    async def one_test_coro():
        # draw elem from domain

        # run test eval

        # keep going

    async def one_run_coro():
        # use provided elem

        # run eval

        # keep going


    while True:
        # scheduling algorithm # TODO
        r = random.random()
        if r > perfsafe:
            await one_run_coro()
        else:
            await one_run_coro()




if __name__ == '__main__':

    import asyncio

    # this is the event loop
    loop = asyncio.get_event_loop()

    # schedule both the coroutines to run on the event loop
    loop.run_until_complete(scheduler(0.5))




