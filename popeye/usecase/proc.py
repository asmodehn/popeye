from __future__ import annotations

import itertools
import typing


class Value:
    val: typing.Any

    def __init__(self, val: typing.Any):
        self.val = val

class Prog:

    fun: typing.Callable
    memoized: typing.Dict[typing.Hashable, typing.Optional[Prog]]
    # TODO : compress the memoized representation in this case : aggregate arguments in  the memoized key structure

    def __init__(self, fun: typing.Callable):
        self.fun = fun
        self.memoized = dict()

    def __call__(self, arg: typing.Hashable):
        self.memoized.setdefault(arg,self.fun(arg))
        if callable(self.memoized[arg]):
            return Prog(self.memoized[arg])
        else:
            return Value(self.memoized[arg])

    def __getitem__(self, item: typing.Hashable):
        if item in self.memoized:
            return self.memoized[item]
        else:
            return self(item)


    def __eq__(self, other):
        return self.fun is other.fun #  or TODO : compare compressed memoized structure < and make it total > (careful with infinity)


class Type:
    """
    A type
    """

    prog: typing.Dict[Prog]

    def __init__(self, **members: Prog):
        self.elems = {n: e for n, e in members.items()}

    def __call__(self, arg):

        return self.prog(arg)

    def __eq__(self, other):
        return all(e in other.elems for e in self.elems) and all(e in self.elems for e in other.elems)




class TypeValue(Type):
    """
    A type value
    """

    elems: typing.Set[typing.Hashable]

    def __init__(self, *elems):
        # Here we filter elements that are part of this type (relative to the equality)
        self.elems = set(e for e in elems if e == e)

    def __iter__(self):
        """This is equivalent to calling with unit type"""
        return iter(self.elems)

    def __eq__(self, other):
        # check relying on python equality (via in operator)
        return all(e in other.elems for e in self.elems) and all(e in self.elems for e in other.elems)


class TypeFamily(Type):
    """
    A Type Family : the dependent case
    """

    family: typing.Dict[typing.Hashable, typing.Optional[Type]]


    def __init__(self, **members: Type):
        self.elems = {n: e for n, e in members.items()}


    def __getitem__(self, item: typing.Hashable):
        """This is equivalent to calling function with an arg"""
        return self.family[item]




class Compute:
    candidates: typing.Any

    def __init__(self, *candidates, **named_candidates):
        typed = (itertools.chain(
            (TypeValue(c) for c in candidates),
            (TypeFamily(**{n: c}) for n, c in named_candidates.items())
        ))
        self.candidates = frozenset(typed)

    def __enter__(self):
        return tuple(self.candidates)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass














if __name__ == '__main__':

    FunA = True
    FunB = False

    with Compute(FunA, FunB) as (ba, bb):
        assert not (ba == bb)




