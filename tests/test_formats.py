from confman import formats

def test_json_rw_pass(tmp_path):
    p = tmp_path / 'a.json'
    formats.write_json(str(p), {'a': 1})
    assert formats.read_json(str(p)) == {'a': 1}

def test_ini_parse_pass(tmp_path):
    p = tmp_path / 'a.ini'
    p.write_text('[db]\nhost=localhost\n', encoding='utf-8')
    out = formats.read_ini(str(p))
    assert out['db']['host'] == 'localhost'

def test_yaml_pass(tmp_path):
    p = tmp_path / 'a.yaml'
    formats.write_yaml(str(p), {'a': 1})
    assert formats.read_yaml(str(p))['a'] == 1

def test_toml_pass(tmp_path):
    p = tmp_path / 'a.toml'
    p.write_text('x=1\n', encoding='utf-8')
    assert formats.read_toml(str(p))['x'] == 1

def test_yaml_nested_pass(tmp_path):
    p = tmp_path / 'nested.yaml'
    formats.write_yaml(str(p), {'db': {'host': 'localhost', 'port': 5432}})
    out = formats.read_yaml(str(p))
    assert out['db']['host'] == 'localhost' and out['db']['port'] == 5432

def test_json_load_pass(tmp_path):
    p = tmp_path / 'b.json'
    p.write_text('{"x":2}', encoding='utf-8')
    assert formats.read_json(str(p))['x'] == 2
