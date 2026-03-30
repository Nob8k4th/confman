from dataclasses import fields

class ConfigSchema:
    @classmethod
    def validate(cls, schema_cls, data):
        for f in fields(schema_cls):
            if f.name not in data:
                raise ValueError(f'missing {f.name}')
            if not isinstance(data[f.name], f.type):
                raise TypeError(f'{f.name} type mismatch')
        return True
