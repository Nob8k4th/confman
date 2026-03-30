from dataclasses import dataclass
from confman.config import Config
from confman.schema import ConfigSchema

def test_dot_access_pass():
    c = Config({'database': {'host': 'localhost'}})
    assert c.database.host == 'localhost'

def test_merge_shallow_fail_nested_host_lost():
    c = Config.merge({'database': {'host': 'h1', 'port': 1}}, {'database': {'port': 2}})
    assert c.database.host == 'h1'

def test_merge_shallow_fail_nested_kept():
    c = Config.merge({'a': {'x': 1, 'y': 2}}, {'a': {'y': 3}})
    assert c.data['a']['x'] == 1

def test_merge_top_level_pass():
    c = Config.merge({'a': 1}, {'b': 2})
    assert c.data == {'a': 1, 'b': 2}

def test_schema_validate_pass():
    @dataclass
    class S:
        host: str
        port: int
    assert ConfigSchema.validate(S, {'host': 'x', 'port': 1})

def test_schema_type_error_pass():
    @dataclass
    class S:
        host: str
    try:
        ConfigSchema.validate(S, {'host': 1})
    except TypeError:
        assert True
    else:
        assert False
