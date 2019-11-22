# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue,
email, or any other method with the owners of this repository before making a change.

## Things to keep in mind when creating new rules

1. Set the version to 'develop':

```python
# -*- coding: utf-8 -*-
# Copyright (c) 2019 Your name <your@email.com>

from saltlint.linter import SaltLintRule

class NewlyAddedRule(SaltLintRule):
    id = '999'
    shortdesc = 'This is an example'
    description = 'This too is an example'
    severity = 'LOW'
    tags = ['formatting']
    version_added = 'develop'
```

Versions will be correctly set when a new release is made.

2. Include an entry to your new rule in [README.md](README.md)

All rules are documented in the README, and on the wiki. We ask you to at least supply an entry
to the [Rules Section](README.md#rules) in your Pull Request.

```markdown
[999](https://github.com/warpnet/salt-lint/wiki/999) | This is an example
```

3. Inside your pull request, please supply information that needs to be added to the wiki

Documentation is important for linters, as such - we ask you to supply the following documentation for your new check:

````markdown
## This is an example

### Problematic code
```yaml
/tmp/testfile:
    file.managed:
      - content:u"\u000B""foobar"
```

### Correct code
```yaml
/tmp/testfile:
    file.managed:
      - content: "foobar"
```

### Rationale
Some explanation as to why this check exists, and why the problematic code is actually bad.
````

## Pull Request Process

Please note we have a code of conduct, please follow it in all your interactions with the project. The workflow advice below mirrors [SaltStack's own guide](https://docs.saltstack.com/en/latest/topics/development/contributing.html#sending-a-github-pull-request) and is well worth reading.

1. [Fork warpnet/salt-lint](https://github.com/warpnet/salt-lint/fork) on GitHub.

2. Make a local clone of your fork.
```bash
git clone git@github.com:my-account/salt-lint.git
cd salt-lint
```

3. Add [warpnet/salt-lint](https://github.com/warpnet/salt-lint) as a git remote.
```bash
git remote add upstream https://github.com/warpnet/salt-lint.git
```

4. Create a new branch in your clone. Create your branch from the develop branch.
```bash
git fetch upstream
git checkout -b add-cool-feature upstream/develop
```

5. Edit and commit changes to your branch.
```
vim path/to/file1 path/to/file2
git diff
git add path/to/file1 path/to/file2
git commit
```
Write a short, descriptive commit title and a longer commit message if necessary.
```
Add cool feature

Fixes #1

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch fix-broken-thing
# Changes to be committed:
#       modified:   path/to/file1
#       modified:   path/to/file2
```

6. Push your locally-committed changes to your GitHub fork.
```
git push -u origin add-cool-feature
```

7. Find the branch on your GitHub salt fork.
[https://github.com/my-account/salt-lint/branches/add-cool-feature](salt-lint)

8. Open a new pull request.
Click on `Pull Request` on the right near the top of the page,
[https://github.com/my-account/salt-lint/pull/new/add-cool-feature](https://github.com/my-account/salt-lint/pull/new/add-cool-feature).

Choose **develop** as the base branch. Review that the proposed changes are what you expect. Write a descriptive comment. Include links to related issues (e.g. 'Fixes #1.') in the comment field. Click `Create pull request`.

9. Salt-lint project members will review your pull request and automated tests will run on it.

Feel free to raise issues in the repo if you don't feel able to contribute a code fix.

## Code of Conduct

### Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to make participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, sex characteristics, gender identity and expression,
level of experience, education, socio-economic status, nationality, personal
appearance, race, religion, or sexual identity and orientation.

### Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
  advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
  address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

### Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

### Scope

This Code of Conduct applies within all project spaces, and it also applies when
an individual is representing the project or its community in public spaces.
Examples of representing a project or community include using an official
project e-mail address, posting via an official social media account, or acting
as an appointed representative at an online or offline event. Representation of
a project may be further defined and clarified by project maintainers.

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at info@warpnet.nl. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

### Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at https://www.contributor-covenant.org/version/1/4/code-of-conduct.html

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see
https://www.contributor-covenant.org/faq
