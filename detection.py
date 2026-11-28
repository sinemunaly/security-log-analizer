from abc import ABC, abstractmethod
from collections import defaultdict, deque
from incident import Incident

class DetectionStrategy(ABC):  # Strategy interface
    @abstractmethod
    def detect(self, records, config): ...

class FailureBurstStrategy(DetectionStrategy):
    def detect(self, records, config):
        windows = defaultdict(deque)
        incidents = []
        for r in records:
            if r.result != 'failure': continue
            q = windows[r.ip_address]
            while q and (r.timestamp-q[0]).total_seconds() > config.window_seconds: q.popleft()
            q.append(r.timestamp)
            if len(q) == config.threshold:
                incidents.append(Incident('Failure burst', r.ip_address, r.timestamp))
        return incidents

class FailureThenSuccessStrategy(DetectionStrategy):
    def detect(self, records, config):
        windows = defaultdict(deque)
        incidents = []
        for r in records:
            q = windows[(r.ip_address, r.username)]
            while q and (r.timestamp-q[0]).total_seconds() > config.window_seconds: q.popleft()
            if r.result == 'failure': q.append(r.timestamp)
            else:
                if len(q) >= config.threshold:
                    incidents.append(Incident('Failure then success', r.ip_address, r.timestamp))
                q.clear()
        return incidents

class AnalysisContext:  # Strategy context
    def __init__(self, strategy): self.strategy = strategy
    def set_strategy(self, strategy): self.strategy = strategy
    def analyze(self, records, config):
        selected = [r for r in records if (not config.ip_address or r.ip_address == config.ip_address) and (not config.start or r.timestamp >= config.start) and (not config.end or r.timestamp <= config.end)]
        return self.strategy.detect(sorted(selected, key=lambda r: r.timestamp), config)
