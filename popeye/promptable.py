import prompt_toolkit


class PromptableError(Exception):
    session: prompt_toolkit.PromptSession
    original: ValueError

    def __init__(self, message: str, original: Exception, **session_kwargs):
        self.session = prompt_toolkit.PromptSession(**session_kwargs)
        self.original = original

    def __call__(self):
        return self.session.prompt(message=f"{self.args[0]} call {te}. Fix it! ")



class PromptableTypeError(PromptableError, TypeError):

    def __init__(self, message: str, original: Exception,  ):

        super(PromptableTypeError, self).__init__(
            message=message, original=original,

        )


    def __call__(self):
        """
        This errors occurs on routine calls. we need to loop on it without too much recursion....
        :return:
        """

        while():

            # doing the prompt
            newval = super(PromptableTypeError, self).__call__()
            try:
                # doing the call

            except TypeError as te: # catching same error as the one we are currently extending (think identity morphism).







class PromptableValueError(PromptableError, ValueError):

    def __init__(self, message: str, original: Exception, ):
        pass


# trigger type error

def testfun(v):
    v


try:
    testfun()
except TypeError as te:
    raise PromptableTypeError("arg missing", te) from TypeError


# trigger value error

def testvalerr(v):
    v * v

try:
    testvalerr('bob')
except ValueError:
    raise PromptableValueError from ValueError


with Tracer() as t:

    try:
        t.testfun()
    except Exception:
        t.tryagain
