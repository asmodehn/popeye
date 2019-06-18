import unittest
import hypothesis
import hypothesis.strategies

if __package__ is None:
    from popeye import typecast
else:
    from .. import typecast


class TestCase(unittest.TestCase):

    @hypothesis.given(arg = hypothesis.infer)
    @hypothesis.settings(verbosity = hypothesis.Verbosity.verbose)
    def test_int_arg(self, arg: int):

        # turn it into a convertible type
        str(arg)

        @typecast.decorator
        def testfun(a: int):
            assert isinstance(a, int)

        testfun(arg)


    @hypothesis.given(arg = hypothesis.strategies.characters(min_codepoint=0, max_codepoint=127, blacklist_categories=('Nd',)))
    @hypothesis.settings(verbosity = hypothesis.Verbosity.verbose)
    def test_nonint_arg(self, arg):


        @typecast.decorator
        def testfun(a: int):
            assert not isinstance(a, int)  # just to have some obvious code here

        with self.assertRaises(typecast.CastError) as ce:
            testfun(arg)
        assert isinstance(ce.exception, ce.expected)
        assert ce.exception.args[0] == f"{arg} cannot pass as an int", ce.exception.args[0]

if __name__ == '__main__':
    unittest.main()
