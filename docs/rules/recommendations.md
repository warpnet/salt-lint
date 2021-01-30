# Recommendations

## 801

**It is recommended to use an identifier with `cron.present`**

### Problematic code
```yaml
hourly_reboot:
  cron.present:
    - name: '/sbin/reboot'
    - user: root
    - minute: '00'
    - hour: *
```

### Correct code
```yaml
hourly_reboot:
  cron.present:
    - name: '/sbin/reboot'
    - user: root
    - minute: '00'
    - hour: *
    - identifier: hourly-reboot
```

### Rationale

If an `identifier` is not specified, the state name is used as an `identifier`. It is however easier to (accidentally) change a state name, after which your cron entry will duplicate.

___
