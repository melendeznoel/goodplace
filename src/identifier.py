from codeable_concept import CodeableConcept
from identifier_use import IdentifierUse

class Identifier:
    def __init__(self, system, value) -> None:
        self.system = system
        self.value = value
    
    @property
    def use(self) -> IdentifierUse:
        return self._use
    
    @use.setter
    def use(self, data: IdentifierUse):
        self._use = data
    
    @property
    def type(self) -> CodeableConcept:
        return self._type
    
    @type.setter
    def type(self, data: CodeableConcept):
        self._type = data

    @property
    def period(self):
        return self._period
    
    @period.setter
    def period(self, data):
        self._period = data