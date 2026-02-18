import dataclasses


@dataclasses.dataclass(frozen=True)
class Demo(dict[str, any]):

    def __init__(self, id_=None, name=None):
        super().__init__()
        self["id"] = id_
        self["name"] = name

    @staticmethod
    def from_dict(d: dict):
        return Demo(**d)

    def get_id(self):
        return self["id"]

    def get_name(self):
        return self["name"]
