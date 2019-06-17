from __future__ import annotations

import datetime
import functools
import random
import types

import hypothesis
from hypothesis.strategies import builds, integers, booleans, one_of
import typing
from pydantic import BaseModel, ValidationError, validate_model
import unittest

import prompt_toolkit
from prompt_toolkit.patch_stdout import patch_stdout

import datetime as dt
from dataclasses import dataclass

from marshmallow import Schema, fields, pprint, validates, ValidationError


class CoercionDump:
    """
    Implement computational coercion to a basic python data structure: dict
    """

    schema: Schema  # should contain dicts only (see marshmallow load behavior)

    def __init__(self, s: Schema):
        self.schema = s

    def __enter__(self):
        return self.schema.dump  # or load ?

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    # TODO : bunch of tests to make sure any coercion is transitive and reflexive...
    # TODO : let user implement its own coercions...


class ComputationalType:  # todo find proper type hint to make static type checker happy
    """
    Computational Game Semantics
    """

    impl: typing.Any # Python implementation


    # TODP : make this a 'trait' with python types ??
    def __init__(self, impl):
        """Constructing the instance for runtime typecheck"""
        self.impl = impl

    def __call__(self, *args, **kwargs):
        """Initial move: environment (opponent) asks/calls"""


class ComputationalEquality(ComputationalType):

    def __init__(self, impl):
        super().__init__(impl)

    def __eq__(self, other):

        def impl_equality():
            return self.impl == other.impl

        return ComputationalType(impl=impl_equality)




class Value(ComputationalType):

    def __init__(self, val):
        super().__init__(impl=val)

    def __call__(self):
        return self.impl


class Union(ComputationalType):
    vals: typing.Tuple[ComputationalType]

    def __init__(self, *vals: ComputationalType):
        self.vals = vals

    def __call__(self, *args, **kwargs):
        # TODO : implement union semantics here ! parallel or ? undeterministic choice ? some kind of competition ?
        choice = random.randint(len(self.vals))
        return self.vals[choice]


class Product(ComputationalType):
    vals: typing.Tuple[ComputationalType]

    def __init__(self, *vals: ComputationalType):
        self.vals = vals

    def __call__(self, *args, **kwargs):
        return self.vals


class Callable(ComputationalType):
    fun: typing.Callable[[arg], res]

    def __init__(self, fun):
        self.fun = fun

    def __call__(self):
        def wrapped(*args, **kwargs):
            # TODO typecheck arg

            res = self.fun(args, kwargs)

            # TODO typecheck res
            return res

        return wrapped




def usage_test():

    class Answer(Schema):
        value: int

    a = prompt_toolkit.prompt(message="enter 42:")

    # Using a context to make explicit the coercion used for equality checking.
    with CoercionDump(Answer) as cd:
        assert cd(a) == cd(42)












# MODELS

@dataclass(frozen=True)
class Email:
    user: str  # HOW TO enforce string content via types
    hostname: str  # HOWTO enforce string content via types ?


@dataclass(init=False)
class User:
    name: str
    email: Email
    created_at: datetime.datetime

    @validates('quantity')
    def validate_quantity(self, value):
        if value < 0:
            raise ValidationError('Quantity must be greater than 0.')
        if value > 30:
            raise ValidationError('Quantity must not be greater than 30.')

    def __init__(self, name: str, email: Email):
        self.name = name
        self.email = email
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return '<User(name={self.name!r})>'.format(self=self)


# SCHEMAS ( how to convert to / from strings )
# Not a type check but a parsing validation ( not as strict, but probably more practical in python)


class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()


user = User(name="Monty", email="monty@python.org")
schema = UserSchema()
result = schema.dump(user)
pprint(result)
# {"name": "Monty",
#  "email": "monty@python.org",
#  "created_at": "2014-08-17T14:54:16.049594+00:00"}


user_data = {
    'created_at': '2014-08-11T05:26:03.869245',
    'email': u'ken@yahoo.com',
    'name': u'Ken'
}
schema = UserSchema()
result = schema.load(user_data)
pprint(result)
# {'name': 'Ken',
#  'email': 'ken@yahoo.com',
#  'created_at': datetime.datetime(2014, 8, 11, 5, 26, 3, 869245)},

# TODO : plug tests (hypothesis) on that
# TODO : plug click on that
# TODO : plug repl prompt on that
# Note plugging json load/dump for neetwork already managed by marshmallow
