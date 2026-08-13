class Platform:
    def __init__(self, name, platform_id=None):
        self._id = platform_id
        self._name = name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @id.setter
    def id(self, value):
        self._id = value

    @name.setter
    def name(self, value):
        value = value.strip()

        if not value:
            raise ValueError("Platform name cannot be empty")

        self._name = value

    def __str__(self):
        return self._name