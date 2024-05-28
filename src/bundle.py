import json

from identifier import Identifier

class Bundle:
    def __init__(self) -> None:
        self._identifier: list[Identifier] = []

    @property
    def identifier(self):
        return self._identifier

    @identifier.setter
    def identifier(self, data: Identifier):
        found = any(map(lambda identifier: identifier.value == data.value and identifier.system == data.system, self._identifier))

        if found is False:
            self._identifier.append(data)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
