# Contributing
*ClusView* follows the following guidelines regarding issues, PRs and commit history.

## Issues
Issues are the main point of information about proposals, bugs, and any other type of discussion.

Explain the problem in detail and the proposed solution. No need to be explicit about code,
outlining the high-level view of the changes is sufficient.

Issues are always labeled into two categories:
- `type`: nature of the problem and changes:

  https://github.com/gcalcedo/clusview/labels/state%20%3A%20pending
  https://github.com/gcalcedo/clusview/labels/state%20%3A%20discarded
  https://github.com/gcalcedo/clusview/labels/state%20%3A%20accepted

- `state`: progress on the issue.

  https://github.com/gcalcedo/clusview/labels/type%20%3A%20enhancement
  https://github.com/gcalcedo/clusview/labels/type%20%3A%20docs
  https://github.com/gcalcedo/clusview/labels/type%20%3A%20bug

## Pull Requests
Pull requests must always have `develop` as the target.

The information on them should be minimal. Always start with a reference to the issue they are solving.
To do so, start your PRs in this way.

```markdown
Resolves #issueNumber.
```

If some additional clarification needs to be added that is not addressed in the corresponding issue,
feel free to do so.

Creating a PR directly without referring to an issue is possible if the change is trivial, like a typo.