
import inspect
trace_indent = 0


class Tracer:
    """Decorator to allow plugging custom behavior on routines call and return"""

    def __init__(self, ):
        pass

    def __call__(self, f):
        """
        the decorator method itself
        :param args:
        :param kwargs:
        :return:
        """
        sig = inspect.signature(f)

        def do_it(*args, **kwargs):
            # global trace_indent
            # ws = ' ' * (trace_indent * 2)
            # print("%sENTER %s: " % (ws, f.__name__))

            # for ix, param in enumerate(sig.parameters.values()):
            #     print("%s    %s: %s" % (ws, param.name, args[ix]))

            # trace_indent += 1

            try:
                ba = sig.bind(*args, **kwargs)
            except TypeError as te:

                # inspect stackframe

                # decide if recoverable

                # raise appropriate exception
                raise

            result = f(*ba.args, **ba.kwargs)
            # trace_indent -= 1
            # print("%sEXIT %s (returned %s)" % (ws, f.__name__, result))
            return result

        return do_it











@Tracer()
def testcall(arg):
    print(arg)


testcall("bouh")



testcall()



with Tracer() as t:
    t.testcall()

