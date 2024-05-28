from coding import Coding


class CodeableConcept:
    def __init__(self, coding: list[Coding], text) -> None:
        self.coding = coding
        self.text = text
