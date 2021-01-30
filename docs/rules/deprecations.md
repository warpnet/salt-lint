# Deprecations

## 901

**Using the `quiet` argument with `cmd.run` is deprecated. Use `output_loglevel: quiet`**

### Problematic code
```yaml
getpip:
  cmd.run:
    - name: /usr/bin/python /usr/local/sbin/get-pip.py
    - quiet
```

### Correct code
```yaml
getpip:
  cmd.run:
    - name: /usr/bin/python /usr/local/sbin/get-pip.py
    - output_loglevel: quiet
```

### Rationale
SaltStack has deprecated using the `quiet` argument with `cmd.run` since release `2014.1.0`

___
