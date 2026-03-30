class Config:
    def __init__(self, data):
        self._data = data

    def __getattr__(self, item):
        if item in self._data:
            value = self._data[item]
            if isinstance(value, dict):
                return Config(value)
            return value
        raise AttributeError(item)

    @property
    def data(self):
        return self._data

    @classmethod
    def merge(cls, *configs):
        merged = {}
        for cfg in configs:
            merged.update(cfg)
        return cls(merged)
