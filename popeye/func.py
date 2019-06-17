
# python basic functional features

# INTROSPECTION
# values
# callables
# iterables
# modules (collection of values/callables/iterables)
# decorators (higher order callable)
# async

import inspect
import typing

import prompt_toolkit


def error_interp(te: TypeError, fixer: typing.Callable):
    # Interpreting python errors
    MISSING_ARG = "missing a required argument: "

    if te.args[0].startswith(MISSING_ARG):
        # extract argname from string

        argname = te.args[0][len(MISSING_ARG):]

        return (argname, fixer(argname))


def prompt_missing(fun):

    sig = inspect.signature(fun)

    def wrapper(*args, **kwargs):
        res = None
        while res is None:
            try:
                ba = sig.bind(*args, **kwargs)
                # fun should run only once args are all bound
                res = fun(ba)
            except TypeError as te:

                def fixer(argname):
                    nonlocal args
                    args[argname] = prompt_toolkit.prompt(message = f"{te}. Fix it! ")

                error_interp(te, fixer)

        return res

    return wrapper






@prompt_missing
def fun(a):
    for i in range(a):
        yield i



for f in fun():
    print(f)























