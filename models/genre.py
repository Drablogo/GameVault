class Genre:
    def __init__(self, genre_id: int | None, name: str):
        self._id = genre_id
        self._name = name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        value = value.strip()

        if not value:
            raise ValueError("Genre name cannot be empty")

        self._name = value

    def __str__(self):
        return self._name