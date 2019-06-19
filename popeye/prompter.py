


class Prompter:
    """
    A class tracking function calls and more...
    Basically the aim is to store the previous function call, so that it can be retried on an exception
    """

    def __init__(self):
        pass


    def __enter__(self):
        pass


    def __exit__(self, exc_type, exc_val, exc_tb):
        # grab exception

        # access traces to recover where error occured
        # https://docs.python.org/3/library/traceback.html

        # display

        # prompt for fix


        # loop (HOW ?)
        # See : https://github.com/asteriogonzalez/resume/blob/master/resume.py

    def __getattr__(self, item):
        # find item in external context

        # assume it was wrapped in a tracing decorator




class Retrier(object):

    max_retries = 3

    def __init__(self, ...):
        self.retries = 0
        self.acomplished = False

    def __enter__(self):
        return self

    def __exit__(self, exc, value, traceback):
        if not exc:
            self.acomplished = True
            return True
        self.retries += 1
        if self.retries >= self.max_retries:
            return False
        return True

