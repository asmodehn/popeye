import inspect

if __package__ is None:
    from promptable import PromptableTypeError
else:
    from .promptable import PromptableTypeError

# TODO define parsers
# TODO : handle errors to display nicer message


def float_parser(v):
    try:
        return float(v)
    except ValueError as ve:
        raise PromptableTypeError(
            f"{v} cannot pass as a float",
            original=ve)


def int_parser(v):
    try:
        return int(v)
    except ValueError as ve:
        raise PromptableTypeError(
            f"{v} cannot pass as an int",
            original=ve)



def decorator(fun):

    # determine type of all args based on signature & annotations

    sig = inspect.signature(fun)

    # use the type as a parser identification.

    def wrapper(*args, **kwargs):  # untyped !
        # TODO : iterators

        ba = sig.bind(*args, **kwargs)

        for n, a in ba.arguments.items():
            if sig.parameters[n].annotation == float:
                ba.arguments[n] = float_parser(a)
            elif sig.parameters[n].annotation == int:
                ba.arguments[n] = int_parser(a)
            else:  # no or unknown annotation: rely on usual python ducktyping
                pass

        # cast all argument to the proper type to parse strings

        return fun(*ba.args, **ba.kwargs)  # TODO : typecheck it !

        # TODO :  attempt to convert return type.

    return wrapper
