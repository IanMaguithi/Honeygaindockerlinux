First off, thank you for considering contributing to honeygaindockerlinux. It’s people like you that make honeygaindockerlinux
such a great tool. Please take a moment to review this document in order to make the contribution process easy and effective for everyone involved.

Following these guidelines helps to communicate that you respect the time of the developers managing and developing this open source project. In return, they should reciprocate that respect in addressing your issue, assessing changes, and helping you finalize your pull requests.

## Bug Reports
A bug is a _demonstrable problem_ that is caused by the code in the repository.
Good bug reports are extremely helpful - thank you!

Guidelines for bug reports:

1. **Use the GitHub issue search** &mdash; check if the issue has already been
   reported.

2. **Check if the issue has been fixed** &mdash; try to reproduce it using the
   latest `main` or `next` branch in the repository.

3. **Isolate the problem** &mdash; ideally create a reduced test case.

A good bug report shouldn't leave others needing to chase you up for more
information. Please try to be as detailed as possible in your report. What is
your environment? What steps will reproduce the issue? What OS experiences the
problem? What would you expect to be the outcome? All these details will help
people to fix any potential bugs.

Example:

> Short and descriptive example bug report title
>
> A summary of the issue and the browser/OS environment in which it occurs. If
> suitable, include the steps required to reproduce the bug.
>
> 1. This is the first step
> 2. This is the second step
> 3. Further steps, etc.
>
> `<url>` - a link to the reduced test case
>
> Any other information you want to share that is relevant to the issue being
> reported. This might include the lines of code that you have identified as
> causing the bug, and potential solutions (and your opinions on their
> merits).

## Feature requests

Feature requests are welcome. But take a moment to find out whether your idea
fits with the scope and aims of the project. It's up to *you* to make a strong
case to convince the project's developers of the merits of this feature. Please
provide as much detail and context as possible.


## Pull requests

Good pull requests - patches, improvements, new features - are a fantastic
help. They should remain focused in scope and avoid containing unrelated
commits.

**Please ask first** before embarking on any significant pull request (e.g.
implementing features, refactoring code), otherwise you risk spending a lot of
time working on something that the project's developers might not want to merge
into the project.

### For new Contributors

If you have never created a pull request before, welcome :tada: :smile: [Here is a great tutorial](https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github)
on how to create a pull request.

1. [Fork](http://help.github.com/fork-a-repo/) the project, clone your fork,
   and configure the remotes:

   ```bash
   # Clone your fork of the repo into the current directory
   git clone https://github.com/<your-username>/<repo-name>
   # Navigate to the newly cloned directory
   cd <repo-name>
   # Assign the original repo to a remote called "upstream"
   git remote add upstream https://github.com/hoodiehq/<repo-name>
   ```

2. If you cloned a while ago, get the latest changes from upstream:

   ```bash
   git checkout main
   git pull upstream main
   ```

3. Create a new topic branch (off the main project development branch) to
   contain your feature, change, or fix:

   ```bash
   git checkout -b <topic-branch-name>
   ```

4. Make sure to update, or add to the tests when appropriate. Patches and
   features will not be accepted without tests. Run `python3 test` to check that
   all tests pass after you've made changes. Look for a `Testing` section in
   the project’s README for more information.

5. If you added or changed a feature, make sure to document it accordingly in
   the `README.md` file.

6. Push your topic branch up to your fork:

   ```bash
   git push origin <topic-branch-name>
   ```

7. [Open a Pull Request](https://help.github.com/articles/using-pull-requests/)
    with a clear title and description.

## Maintainers

If you have commit access, please follow this process for merging patches and cutting new releases.

### Reviewing changes

1. Check that a change is within the scope and philosophy of the component.
2. Check that a change has any necessary tests.
3. Check that a change has any necessary documentation.
4. If there is anything you don’t like, leave a comment below the respective
   lines and submit a "Request changes" review. Repeat until everything has
   been addressed.
5. If you are not sure about something, mention `@honeygaindockerlinux/maintainers` or specific
   people for help in a comment.
6. If there is only a tiny change left before you can merge it, and you think
   it’s best to fix it yourself, you can directly commit to the author’s fork.
   Leave a comment about it so the author and others will know.
7. Once everything looks good, add an "Approve" review. Don’t forget to say
   something nice 👏🐶💖✨
8. If the commit messages follow [our conventions](https://conventionalcommits.org)

   1. If there is a breaking change, make sure that `BREAKING CHANGE:` with
      _exactly_ that spelling (incl. the ":") is in body of the according
      commit message. This is _very important_, better look twice :)
   2. Make sure there are `fix: ...` or `feat: ...` commits depending on whether
      a bug was fixed or a feature was added. **Gotcha:** look for spaces before
      the prefixes of ` fix:` and ` feat:`, these get ignored by semantic-release.
   3. Use the "Rebase and merge" button to merge the pull request.
   4. Done! You are awesome! Thanks so much for your help 🤗

9. If the commit messages _do not_ follow our conventions

   1. Use the "squash and merge" button to clean up the commits and merge at
      the same time: ✨🎩
   2. Is there a breaking change? Describe it in the commit body. Start with
      _exactly_ `BREAKING CHANGE:` followed by an empty line. For the commit
      subject:
   3. Was a new feature added? Use `feat: ...` prefix in the commit subject
   4. Was a bug fixed? Use `fix: ...` in the commit subject

Sometimes there might be a good reason to merge changes locally. The process
looks like this:

### Reviewing and merging changes locally

```
git checkout main # or the main branch configured on github
git pull # get latest changes
git checkout feature-branch # replace name with your branch
git rebase main
git checkout main
git merge feature-branch # replace name with your branch
git push
```

When merging PRs from forked repositories, we recommend you install the
[hub](https://github.com/github/hub) command line tools.

This allows you to do:

```
hub checkout link-to-pull-request
```

meaning that you will automatically check out the branch for the pull request,
without needing any other steps like setting git upstreams! :sparkles:
