# confman

`confman` 用于统一管理多来源配置，支持文件读取、对象化访问和环境变量覆盖。

## 能力说明

- `Config`：把字典包装成支持点访问的配置对象
- `formats`：JSON/YAML/TOML/INI 的读写与解析函数
- `EnvOverride`：将指定前缀的环境变量映射到配置树
- `ConfigSchema`：基于 dataclass 的字段类型校验

## 快速使用

```bash
pip install -e .
```

```python
from dataclasses import dataclass
from confman import Config, EnvOverride, ConfigSchema
from confman import formats

base = {"database": {"host": "127.0.0.1", "port": 5432}}
cfg = Config(base)
print(cfg.database.host)

updated = EnvOverride().apply(base, {"APP_DATABASE_HOST": "db.internal"})
print(updated["database"]["host"])

@dataclass
class DbConf:
    host: str
    port: int

ConfigSchema.validate(DbConf, {"host": "localhost", "port": 5432})
formats.write_json("config.json", updated)
```

## 测试

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
pytest tests/ -v --tb=short --json-report --json-report-file=test_results.json
```
