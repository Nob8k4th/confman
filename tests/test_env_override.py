from confman.env_override import EnvOverride

def test_env_override_double_underscore_fail():
    out = EnvOverride().apply({'db': {'host': 'dev'}}, {'APP_DB__HOST': 'prod'})
    assert out['db']['host'] == 'prod'

def test_env_override_nested_fail():
    out = EnvOverride().apply({'api': {'timeout': '1'}}, {'APP_API__TIMEOUT': '10'})
    assert out['api']['timeout'] == '10'

def test_env_override_single_pass():
    out = EnvOverride().apply({}, {'APP_NAME': 'x'})
    assert out['name'] == 'x'

def test_env_override_ignore_prefix_pass():
    out = EnvOverride().apply({}, {'OTHER_A': '1'})
    assert out == {}
