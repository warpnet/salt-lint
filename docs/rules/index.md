# Rules

**False Positives: Skipping Rules**

Some rules are bit of a rule of thumb. To skip a specific rule for a specific task, inside your state add `# noqa [rule_id]` at the end of the line. You can skip multiple rules via a space-separated list. Example:

```yaml
/tmp/testfile:
  file.managed:
    - source: salt://{{unspaced_var}}/example  # noqa: 206
```

**Formatting**

Disable formatting checks using `-x formatting`

Rule | Description
:-:|:--
[201](formatting/#201) | Trailing whitespace
[202](formatting/#202) | Jinja statement should have spaces before and after: `{% statement %}`
[203](formatting/#203) | Most files should not contain tabs
[204](formatting/#204) | Lines should be no longer than 160 chars
[205](formatting/#205) | Use ".sls" as a Salt State file extension
[206](formatting/#206) | Jinja variables should have spaces before and after `{{ var_name }}`
[207](formatting/#207) | File modes should always be encapsulated in quotation marks
[208](formatting/#208) | File modes should always contain a leading zero
[209](formatting/#209) | Jinja comment should have spaces before and after: `{# comment #}`
[210](formatting/#210) | Numbers that start with `0` should always be encapsulated in quotation marks
[211](formatting/#211) | `pillar.get` or `grains.get` should be formatted differently
[212](formatting/#212) | Most files should not contain irregular spaces
[213](formatting/#213) | SaltStack recommends using `cmd.run` together with `onchanges`, rather than `cmd.wait`
[214](formatting/#214) | SLS file with a period in the name (besides the suffix period) can not be referenced

___

**Jinja**

Disable jinja checks using `-x jinja`

Rule | Description
:-:|:--
[202](formatting/#202) | Jinja statement should have spaces before and after: `{% statement %}`
[206](formatting/#206) | Jinja variables should have spaces before and after `{{ var_name }}`
[209](formatting/#209) | Jinja comment should have spaces before and after: `{# comment #}`
[211](formatting/#211) | `pillar.get` or `grains.get` should be formatted differently

___

**Recommendations**

Disable recommendation checks using `-x recommendation`

Rule | Description
:-:|:--
[801](recommendations/#801) | Using the `quiet` argument with `cmd.run` is deprecated. Use `output_loglevel: quiet`

___

**Deprecations**

Disable deprecation checks using `-x deprecation`

Rule | Description
:-:|:--
[901](deprecations/#901) | Using the `quiet` argument with `cmd.run` is deprecated. Use `output_loglevel: quiet`
