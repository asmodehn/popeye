
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


def error_fixer(te: TypeError, sig: inspect.Signature):
    # Interpreting python errors
    MISSING_ARG = "missing a required argument: "

    if te.args[0].startswith(MISSING_ARG):
        # extract argname from string
        argname = te.args[0][len(MISSING_ARG):].strip("'")
        argindex = None
        for i, p in enumerate(sig.parameters):
            if p == argname:
                argindex = i

        def fixer(args, kwargs):
            args = []
            found = False
            # dirty code, we can do better... but it works
            for i, p in enumerate(sig.parameters):
                if i == argindex:
                    argvalue = prompt_toolkit.prompt(message=f"{fun.__name__} call {te}. Fix it! ")

                    args.append(argvalue)  #TODO : type cast
                    found = True
                else:
                    args.append(args[i] if not found else args[i+1])

            # TODO : full iterator style ?

            new_args = tuple(args)
            kwargs = kwargs
            return new_args, kwargs

        return fixer
    else:
        raise NotImplementedError


def prompt_missing(fun):

    sig = inspect.signature(fun)

    def wrapper(*args, **kwargs):
        res = None
        while res is None:
            try:
                ba = sig.bind(*args, **kwargs)
                # fun should run only once args are all bound
                res = fun(*ba.args, **ba.kwargs)
            except TypeError as te:
                fixer = error_fixer(te, sig)
                args, kwargs = fixer(args, kwargs)

        return res

    return wrapper




def autocast(fun):

    # determine type of all args based on signature & annotations

    # use the type as a parser identification.

    def wrapper(*args, **kwargs):  # untyped !

        # cast all argument to the proper type to parse strings

        return f(*args, **kwargs)  # TODO : typecheck it !

    return wrapper




@prompt_missing
@autocast
def fun(a):
    for i in range(a):
        yield i


for f in fun():
    print(f)























