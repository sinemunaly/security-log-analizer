from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class AnalysisConfig:  # Builder product
    threshold: int = 3
    window_seconds: int = 300
    ip_address: str | None = None
    start: datetime | None = None
    end: datetime | None = None
    method: str = 'both'

class AnalysisConfigBuilder:  # Builder
    def __init__(self): self.values = {}
    def with_threshold(self, value): self.values['threshold'] = value; return self
    def with_window(self, seconds): self.values['window_seconds'] = seconds; return self
    def with_ip(self, ip): self.values['ip_address'] = ip; return self
    def with_period(self, start, end): self.values.update(start=start, end=end); return self
    def with_method(self, method): self.values['method'] = method; return self
    def build(self):
        c = AnalysisConfig(**self.values)
        if type(c.threshold) is not int or c.threshold < 1 or type(c.window_seconds) is not int or c.window_seconds < 1:
            raise ValueError('Threshold and window must be positive integers')
        if c.start and c.end and c.start > c.end: raise ValueError('Invalid period')
        if c.method not in ('burst', 'success', 'both'): raise ValueError('Unknown method')
        return c
