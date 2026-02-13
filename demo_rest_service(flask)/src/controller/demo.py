class Demo(dict[str, any]):
    def __init__(self, id_=None, name=None):
        super().__init__()
        self["id"] = id_
        self["name"] = name

    @staticmethod
    def from_dict(d: dict):
        return Demo(
            d.get("id"),
            d.get("name")
        )

    @staticmethod
    def from_tuple(t: tuple):
        return Demo(t[0], t[1])

    def get_id(self):
        return self["id"]

    def get_name(self):
        return self["name"]
