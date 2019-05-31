from __future__ import annotations

import inspect
import itertools
import typing

"""
Mixing a pure functional (implemented as callable) programming model,
with type model (implemented as frozenset)
Guideline : Category Theory, Computational Type Theory
Note : we use basic data types from python, to not have to reimplement them.
TODO : reimplement them, after we get computational type provability
"""


class Type:

    id: typing.AnyStr  # representation
    elems: typing.Union[typing.FrozenSet, Type]  # Recursive data structure

    def __init__(self, *elems: Type, id: typing.AnyStr = None):
        self.id = id
        self.elems = frozenset(e if isinstance(e, Type) else Type(*e) for e in elems)

    def __hash__(self):
        return hash(self.elems)

    def __eq__(self, other):
        return (e in other.elems for e in self.elems)

    def __getitem__(self, item):
        # This is not ideal : TODO compare various implementations (after we get computational types in place)
        for e in self.elems:
            if isinstance(e, Type) and item == e.id:
                return e
        return None  # explicit python semantics

    def __iter__(self):
        return iter(self.elems)

    def __len__(self):
        return len(self.elems)

    def __repr__(self):
        """
        Faithful representation : this is storage purpose
        :return:
        """
        return self.id

    def __str__(self):
        """
        Maximizing readibility : this is code purpose
        :return:
        """
        return self.id


class TypeValue(Type):
    """
    Type Values implemented in host language.
    Only to make construction easier in host language
    """

    def __init__(self,  val: typing.Hashable, id: TypeValue = None):
        self.id = id
        self.elems = val

    def __eq__(self, other):
        return self.elems == other.elems


class Map:

    compute: typing.Optional[typing.Callable]

    def __init__(self, compute: typing.Callable = None, repr = None):
        self.compute = compute
        self.repr = repr if repr is not None else inspect.getsource(compute)

    def __call__(self, arg):
        # priority to compute
        return self.compute(arg)

    def __repr__(self):
        """
        Faithful representation : this is storage purpose
        :return:
        """
        return self.repr

    def __str__(self):
        """
        Maximizing readibility : this is code purpose
        :return:
        """
        return self.repr


if __name__ == '__main__':

    # Boolean Logic in maps
    TRUE_COMPUTE = Map(compute=lambda x: True)
    FALSE_COMPUTE = Map(compute=lambda y: False)
    AND_COMPUTE = Map(compute=lambda x, y: x() and y())
    OR_COMPUTE = Map(compute=lambda x, y: x() or y())
    NOT_COMPUTE = Map(compute=lambda x: not x())

    # Boolean Logic in types
    TRUE_TYPE = TypeValue(val=True, id='TRUE')
    FALSE_TYPE = TypeValue(val=False, id='FALSE')
    AND_TYPE = Type(id='AND',
                    # Type constructor or dict are equivalent here
                    Type( id='TRUE', Type(TRUE= True, FALSE = False),
                    FALSE= {'TRUE': False, 'FALSE': False},)
    OR_TYPE = Type(id='OR',
                   # Type constructor or dict are equivalent here
                   TRUE= Type(TRUE= True, FALSE= True),
                   FALSE= {'TRUE': True, 'FALSE': False},)

    NOT_TYPE = Type(id='NOT', TRUE= False, FALSE= True)


    assert TRUE_TYPE == TRUE_TYPE
    assert AND_TYPE[TRUE_TYPE] == AND_TYPE[TRUE_TYPE]
    assert AND_TYPE[TRUE_TYPE][FALSE_TYPE] == AND_TYPE[FALSE_TYPE][TRUE_TYPE]


