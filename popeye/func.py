
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

if __package__ is None:
    import typecast
else:
    from . import typecast

def type_error_fixer(te: TypeError, sig: inspect.Signature):
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

                    args.append(argvalue)  # typecast will be done by ht other decorator (typecast.decorator)
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
            except typecast.CastError as ce:
                fixer = cast_error_fixer(ce, sig)
                args, kwargs = fixer(args, kwargs)

        return res

    return wrapper


@prompt_missing
@typecast.decorator
def fun(a: int):
    for i in range(a):
        yield i


for f in fun('bob'):
    print(f)























