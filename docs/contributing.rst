============
Contributing
============

When contributing to this repository, please first discuss the change you wish to make via issue,
email, or any other method with the owners of this repository before making a change.

Pull Request Process
====================

Please note we have a code of conduct, please follow it in all your interactions with the project. The workflow advice below mirrors `SaltStack's own guide <https://docs.saltstack.com/en/latest/topics/development/contributing.html#sending-a-github-pull-request>`_ and is well worth reading.

1. `Fork warpnet/salt-lint <https://github.com/warpnet/salt-lint/fork>`_ on GitHub.

2. Make a local clone of your fork::

    git clone git@github.com:my-account/salt-lint.git
    cd salt-lint

3. Add `warpnet/salt-lint <https://github.com/warpnet/salt-lint>`_ as a git remote::

    git remote add upstream https://github.com/warpnet/salt-lint.git

4. Create a new branch in your clone. Create your branch from the develop branch::

    git fetch upstream
    git checkout -b add-cool-feature upstream/develop

5. Edit and commit changes to your branch::

    vim path/to/file1 path/to/file2
    git diff
    git add path/to/file1 path/to/file2
    git commit

Write a short, descriptive commit title and a longer commit message if necessary::

    Add cool feature

    Fixes #1

    # Please enter the commit message for your changes. Lines starting
    # with '#' will be ignored, and an empty message aborts the commit.
    # On branch fix-broken-thing
    # Changes to be committed:
    #       modified:   path/to/file1
    #       modified:   path/to/file2

6. Push your locally-committed changes to your GitHub fork::

    git push -u origin add-cool-feature

7. Find the branch on your GitHub salt fork.

8. Open a new pull request. Click on `Pull Request` on the right near the top of you fork. Choose `develop` as the base branch. Review that the proposed changes are what you expect. Write a descriptive comment. Include links to related issues (e.g. 'Fixes #1.') in the comment field. Click `Create pull request`.

9. Salt-lint project members will review your pull request and automated tests will run on it.

Feel free to raise issues in the repo if you don't feel able to contribute a code fix.

.. mdinclude:: ../CODE_OF_CONDUCT.md
