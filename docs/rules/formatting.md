# Formatting

Disable formatting checks using `-x formatting`.

## 201

**Trailing whitespace**

### Problematic code

_Please mind the trailing whitespaces on every line in the code snippet_
```yaml
/tmp/testfile:	⁠
  file.managed: ⁠
    - source:/salt://lorem/ipsum/dolor   ⁠
```

### Correct code
```yaml
/tmp/testfile:
  file.managed:
    - source:/salt://lorem/ipsum/dolor
```

### Rationale
There should not be any trailing whitespace

___

## 202

**Jinja statement should have spaces before and after: `{% statement %}`**

### Problematic code
```yaml
{%-set example='bad'+%}
```

### Correct code
```yaml
{%- set example='good' +%}
```

### Rationale
[Jinja dictates](https://jinja.palletsprojects.com/en/2.10.x/templates/#list-of-control-structures) that statements should always have spaces before and after `{% statement %}`
> A control structure refers to all those things that control the flow of a program - conditionals (i.e. if/elif/else), for-loops, as well as things like macros and blocks. With the default syntax, control structures appear inside {% ... %} blocks.

___

## 203

**Most files should not contain tabs**

### Problematic code
```yaml
/tmp/testfile:
	file.managed:
	- source:/salt://lorem/ipsum/dolor
```

### Correct code
```yaml
/tmp/testfile:
  file.managed:
    - source:/salt://lorem/ipsum/dolor
```

### Rationale
Tabs can cause unexpected display issues, use spaces

___

## 204

**Lines should be no longer than 160 chars**

### Problematic code
```yaml
/tmp/testfile:
  file.managed:
    - source: salt://lorem/ipsum/dolor/sit/amet/consectetur/adipiscing/elit/sed/do/eiusmod/tempor/incididunt/ut/labore/et/dolore/magna/aliqua/ut/enim/ad/minim/veniam
```

### Correct code
```yaml
/tmp/testfile:
  file.managed:
    - source: salt://state/file
```

### Rationale
Long lines make code harder to read and code review more difficult

___

## 205

**Use ".sls" as a Salt State file extension**

### Rationale
All files used by saltstack should have the `.sls` extension

___

## 206

**Jinja variables should have spaces before and after `{{ var_name }}`**

### Problematic code
```yaml
{{-variable+}}
```

### Correct code
```yaml
{{- variable +}}
```

### Rationale
[Jinja dictates](http://jinja.palletsprojects.com/en/2.10.x/templates/#expressions) that variables should always have spaces before and after `{{ variable }}`

___

## 207

**File modes should always be encapsulated in quotation marks**

### Problematic code
```yaml
testfile:
  file.managed:
    - name: /tmp/badfile
    - user: root
    - group: root
    - mode: 0700
    - file_mode: 0660
    - dir_mode: 0775
```

### Correct code
```yaml
testfile:
  file.managed:
    - name: /tmp/testfile
    - user: root
    - group: root
    - mode: '0700'
```

### Rationale
As described in the [saltstack documentation](https://docs.saltstack.com/en/latest/ref/states/all/salt.states.file.html):
> When using a mode that includes a leading zero you must wrap the value in single quotes. If the value is not wrapped in quotes it will be read by YAML as an integer and evaluated as an octal.

There's also an [open issue](https://github.com/saltstack/salt/issues/661) for this

___

## 208

**File modes should always contain a leading zero**

### Problematic code
```yaml
testfile:
  file.managed:
    - name: /tmp/badfile
    - user: root
    - group: root
    - mode: 700
    - file_mode: '660'
    - dir_mode: '775'
```

### Correct code
```yaml
testfile:
  file.managed:
    - name: /tmp/testfile
    - user: root
    - group: root
    - mode: '0700'
```

### Rationale
As described in the [saltstack documentation](https://docs.saltstack.com/en/latest/ref/states/all/salt.states.file.html):
> When using a mode that includes a leading zero you must wrap the value in single quotes. If the value is not wrapped in quotes it will be read by YAML as an integer and evaluated as an octal.

There's also an [open issue](https://github.com/saltstack/salt/issues/661) for this

___

## 209

**Jinja comment should have spaces before and after: `{# comment #}`**

### Problematic code
```yaml
{#-set example='bad'+#}
```

### Correct code
```yaml
{#- set example='good' +#}
```

### Rationale
[Jinja dictates](https://jinja.palletsprojects.com/en/2.10.x/templates/#comments) comments always have spaces before and after `{# comment #}`.
> To comment-out part of a line in a template, use the comment syntax which is by default set to {# ... #}. This is useful to comment out parts of the template for debugging or to add information for other template designers or yourself

___

## 210

**Numbers that start with `0` should always be encapsulated in quotation marks**

### Problematic code
```yaml
# Unquoted octal values with leading zero's.
testdirectory:
  file.recurse:
    - name: /tmp/directory
    - file_mode: 00
    - dir_mode: 0700
```

### Correct code
```yaml
testdirectory:
  file.recurse:
    - name: /tmp/directory
    - file_mode: 700
    - dir_mode: '0775'
```

### Rationale
As described in the [saltstack documentation](https://docs.saltstack.com/en/latest/ref/states/all/salt.states.file.html):
> When using a mode that includes a leading zero you must wrap the value in single quotes. If the value is not wrapped in quotes it will be read by YAML as an integer and evaluated as an octal.

There's also an [open issue](https://github.com/saltstack/salt/issues/661) for this

___

## 211

**`pillar.get` or `grains.get` should be formatted differently**

Correct ways:
* `salt['pillar.get']('item')`
* `pillar['item']`
* `pillar.get('item')`

Incorrect ways:

* `pillar.get['item']`

### Problematic code

```yaml
example_file:
  file.managed:
    - name: /tmp/bad.txt
    - contents: |
        {{ pillar.get['item'] }} # this line is broken
        {{ grains.get['saltversion'] }} # this line is broken
```

### Correct code

```yaml
example_file:
  file.managed:
    - name: /tmp/good.txt
    - contents: |
        {{ salt['pillar.get']('item') }}
        {{ pillar.get('item') }}
        {{ pillar['item'] }}
        {{ salt['grains.get']('saltversion') }}
        {{ grains.get('saltversion') }}
        {{ grains['saltversion'] }}
```

### Rationale

211 catches a common mistake of wrongly calling `grains` and `pillar` data.

___

## 212

**Most files should not contain irregular spaces**

### Problematic code
```yaml
/tmp/testfile:
    file.managed:
      - content:u"\u000B""foobar"
```
Please excuse above example, it's tough to write a proper example of this. Take this error seriously though ;-)

### Correct code
```yaml
/tmp/testfile:
    file.managed:
      - content: "foobar"
```

### Rationale
Irregular spaces can cause unexpected display issues, use spaces

___

## 213

**SaltStack recommends using `cmd.run` together with `onchanges`, rather than `cmd.wait`**

### Problematic code
```yaml
run_postinstall:
  cmd.wait:
    - name: /usr/local/bin/postinstall.sh
    - watch:
      - pkg: mycustompkg
```

### Correct code
```yaml
run_postinstall:
  cmd.run:
    - name: /usr/local/bin/postinstall.sh
    - onchanges:
      - pkg: mycustompkg
```

### Rationale
SaltStack recommends using `cmd.run` together with `onchanges` in [their documentation](https://docs.saltstack.com/en/3000/ref/states/all/salt.states.cmd.html#salt.states.cmd.wait).

___

## 214

**SLS file with a period in the name (besides the suffix period) can not be referenced**

As described by the [official SaltStack documentation](https://docs.saltstack.com/en/3000/topics/tutorials/starting_states.html#moving-beyond-a-single-sls):

> The initial implementation of top.sls and Include declaration followed the python import model where a slash is represented as a period. This means that a SLS file with a period in the name ( besides the suffix period) can not be referenced. For example, webserver_1.0.sls is not referenceable because webserver_1.0 would refer to the directory/file webserver_1/0.sls
>
> The same applies for any subdirectories, this is especially 'tricky' when git repos are created. Another command that typically can't render it's output is `state.show_sls` of a file in a path that contains a dot.

___

## 219

**Nested dictionaries should be over-indented**

As described by the [official SaltStack documentation](https://docs.saltproject.io/en/latest/topics/troubleshooting/yaml_idiosyncrasies.html#nested-dictionaries):

> When dictionaries are nested within other data structures (particularly lists), the indentation logic sometimes changes. Examples of where this might happen include context and default options

```yaml
/etc/http/conf/http.conf:
  file:
    - managed
    - source: salt://apache/http.conf
    - user: root
    - group: root
    - mode: 644
    - template: jinja
    - context:
        custom_var: "override"
    - defaults:
        custom_var: "default value"
        other_var: 123
```
> Notice that while the indentation is two spaces per level, for the values under the context and defaults options there is a four-space indent. If only two spaces are used to indent, then those keys will be considered part of the same dictionary that contains the context key, and so the data will not be loaded correctly.

### Problematic code
```yaml
/etc/http/conf/http.conf:
  file.managed:
    - source: salt://apache/http.conf
    - template: jinja
    - context:
      custom_var: "override"
    - defaults:
      custom_var: "default value"
      other_var: 123
```

### Correct code
```yaml
/etc/http/conf/http.conf:
  file.managed:
    - source: salt://apache/http.conf
    - template: jinja
    - context:
        custom_var: "override"
    - defaults:
        custom_var: "default value"
        other_var: 123
```

___

## 220

**SLS and JINJA files must end with only one newline character**

As described by the [POSIX standard](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_206)
>3.206 Line
> 
>A sequence of zero or more non- 'newline' characters plus a terminating 'newline' character.

### Problematic code
```yaml
# No <newline> in <End Of File>
debug_output:
  cmd.run:
    - name: echo hello<EOF>
```

### Problematic code
```yaml
# 2 or more <newline> in <End Of File>
debug_output:
  cmd.run:
    - name: echo hello

<EOF>
```


### Correct code
```yaml
# 1 <newline> in <End Of File>
debug_output:
  cmd.run:
    - name: echo hello
<EOF>
```
