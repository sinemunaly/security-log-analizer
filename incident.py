from abc import ABC

class IncidentState(ABC):  # State
    name = ''
    def investigate(self, incident): raise ValueError('Invalid state transition')
    def resolve(self, incident): raise ValueError('Invalid state transition')

class NewState(IncidentState):
    name = 'Yeni'
    def investigate(self, incident): incident._state = InvestigatingState()

class InvestigatingState(IncidentState):
    name = 'İnceleniyor'
    def resolve(self, incident): incident._state = ResolvedState()

class ResolvedState(IncidentState):
    name = 'Çözüldü'

class Incident:  # State context
    def __init__(self, kind, ip_address, timestamp):
        self.kind, self.ip_address, self.timestamp = kind, ip_address, timestamp
        self._state = NewState()
    @property
    def status(self): return self._state.name
    def investigate(self): self._state.investigate(self)
    def resolve(self): self._state.resolve(self)
