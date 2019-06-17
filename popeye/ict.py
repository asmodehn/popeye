import prompt_toolkit
import typing

# Model : human friendly : context of name replacement mechanics -> dict implementation
# always default value (None, empty nested dict ?). semantics -> unknown, bottom, hole.
# always named (or any unique hash if not named explicitely).


class InteractiveValue:

    type:  typing.Union[int, float, str]

    def __init__(self, type = typing.Type[typing.Any]):
        assert type in [int, float, str]
        self.type = type

    def __call__(self,):  # call means creating/instantiating/drawing a value/move
        # strategy to draw from : user input (special case of game semantics/CCCTT)
        v = prompt_toolkit.prompt(message=f"{self.type}?")
        # typecheck/cast  # TODO : plug here typeckecer / string formatters, etc.
        return self.type(v)


class InteractiveProductType:
    # TODO : maybe later extend python types with interactive user input/output

    type: typing.Tuple[typing.Any]

    def __init__(self, type = typing.Tuple[typing.Any]):
        # TODO : different context depending on type semantics
        assert isinstance(type, tuple)
        self.type = type

    def __call__(self):
        for a in self.type:
            yield prompt_toolkit.prompt(message=f"{a}?")

    def __getitem__(self, item):
        # projections
        return self.type[item]


class InteractiveSumType:
    # TODO : maybe later extend python types with interactive user input/output

    type: typing.Set[typing.Any]

    def __init__(self, type = typing.Set[typing.Any]):
        # TODO : different context depending on type semantics
        assert isinstance(type, set)
        self.type = type

    def __call__(self):
        prompt_toolkit.prompt(message=f"{'|'.join(self.type)}?")


class InteractiveContext:

    storage: typing.Dict[typing.Hashable, typing.Any]

    def __init__(self, type):
        self.storage = {}
        # introspection on type (as data model). NOTE : parser like marhsmallow or others should be used here...
        for a in type.__annotations__:
            self.storage.setdefault(a, a)       # todo : get type and default and all that

    def __call__(self):
        for k, v in self.storage.items():
            yield prompt_toolkit.prompt(message=f"{k}: {v}?")

        # cmd, arg = prompt_toolkit.prompt(message=f"{self.type}?")
        #
        # if cmd == "browse":
        #     for n, c in self.storage.items():
        #         click.echo(n + ":")
        #         click.echo(c)
        #
        # elif cmd == "read":
        #     print(self.storage.get(arg))
        #
        # elif cmd == "add":
        #     self.storage[arg] = self.type()  # need default  # implicit edit on create ? conditional on defaults ?
        #
        # elif cmd == "edit":
        #     # recursive for code simplicity at first pass, could be changed later
        #     self.storage[arg].type.repl()
        #
        # elif cmd == "delete":
        #     self.storage.pop(arg)


class DataRepl:

    type: InteractiveValue

    def __init__(self, type = InteractiveValue(str)):
        self.type = type

    def __call__(self, *args, **kwargs):
        # defines the data
        return self.type()


class CmdRepl:

    type: InteractiveValue

    def __init__(self, type = InteractiveValue(str)):
        self.type = type

    def __call__(self, *args, **kwargs):
        # modifies data
        cmd, arg = prompt_toolkit.prompt(message=f"cmd?")

        if cmd == 'smthg':
            smthg(arg)



