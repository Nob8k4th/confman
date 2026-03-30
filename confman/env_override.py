class EnvOverride:
    def apply(self, data, environ, prefix='APP_'):
        output = dict(data)
        for key, value in environ.items():
            if not key.startswith(prefix):
                continue
            parts = key[len(prefix):].lower().split('_')
            cur = output
            for part in parts[:-1]:
                cur = cur.setdefault(part, {})
            cur[parts[-1]] = value
        return output
