# Basic Git commands with real-life examples

[Back to the index](../README.md)

Complete [SSH and GitHub setup](ssh-github-setup.md) first. These examples work in Linux and macOS terminals with a recent Git version. Run commands inside your project folder unless instructed otherwise. Each scenario is separate; replace example filenames, owners, and repository names with your own.

## Everyday command reference

Your **working directory** contains the files you edit. The **staging area** holds the changes selected for the next **commit**, a saved snapshot in local history. A **branch** is a named line of development. A **remote**, commonly `origin`, identifies another copy of the repository, such as the one on GitHub.

| Command | When you use it |
| --- | --- |
| `git status` | Check your branch and changed, staged, or untracked files. |
| `git diff` | Review unstaged changes to tracked files. |
| `git add README.md` | Stage the current contents of a specific file. |
| `git diff --staged` | Review what your next commit will include. |
| `git commit -m "Fix installation steps"` | Save the staged changes locally with a description. |
| `git log --oneline -5` | Read the five most recent commits. |
| `git show HEAD` | Inspect the latest commit. |
| `git branch` | List local branches; the asterisk marks the current one. |
| `git remote -v` | Check the remote addresses used for fetching and pushing. |

`git diff` does not display untracked file contents; open those files to review them. If you edit a file after staging it, run `git add` again to include the new edits. A commit stays on your computer until you push it. See the [official Git tutorial](https://git-scm.com/docs/gittutorial).

## Example 1: Start a personal portfolio

You have a new portfolio project and want to track its history. From a directory where you keep projects, create a fresh folder:

```sh
mkdir portfolio-practice
cd portfolio-practice
git init -b main
printf '# My portfolio\n' > README.md
git add README.md
git commit -m "Start portfolio project"
```

Use a new folder name if this one already exists. `git init` creates local Git metadata; it does not create a GitHub repository. See the [Git initialization reference](https://git-scm.com/docs/git-init).

To publish it, create an **empty** repository named `portfolio-practice` on GitHub, without adding a README, license, or `.gitignore`. Replace `YOUR-USERNAME`:

```sh
git remote add origin git@github.com:YOUR-USERNAME/portfolio-practice.git
git push -u origin main
```

The first push uploads `main`; `-u` sets its upstream so later pushes from this branch can use `git push`. See the [push reference](https://git-scm.com/docs/git-push).

## Example 2: Join a class project and fix a typo

Your team already has a repository. Clone it once; do not initialize a second repository inside it:

```sh
git clone git@github.com:OWNER/class-website.git
cd class-website
git switch -c fix/readme-typo
```

Open `README.md` in your editor and correct the typo. Then save and review it:

```sh
git status
git diff
git add README.md
git diff --staged
git commit -m "Correct course name in README"
git push -u origin fix/readme-typo
```

On GitHub, open a pull request from `fix/readme-typo` into the team's default branch and describe the correction. Your teammate can review it before merging. Pushing requires write access; otherwise use a fork according to your team's workflow. A push alone does not merge the branch.

## Example 3: Get your teammate's latest work

Before starting another feature, commit your current work or stash it using Example 6. These commands assume the team's default branch is `main`:

```sh
git switch main
git pull --ff-only origin main
git switch -c feature/contact-page
```

`pull --ff-only` fetches remote changes and updates your current branch only when it can advance without merging diverged history. If it refuses, inspect the histories and coordinate with your team before reconciling them. See the [pull reference](https://git-scm.com/docs/git-pull).

To inspect remote work before integrating it:

```sh
git fetch origin
git log --oneline HEAD..origin/main
git diff HEAD origin/main
```

`fetch` updates your local view of remote branches without changing your working files. The log shows incoming commits; the diff compares your current snapshot with `origin/main`.

## Example 4: Combine a finished feature locally

For a personal project without a required pull request workflow, suppose `feature/contact-page` has committed, tested changes and your working directory is clean:

```sh
git switch main
git pull --ff-only origin main
git merge feature/contact-page
```

Review and test the combined project. Once it works:

```sh
git push origin main
git branch -d feature/contact-page
```

The merge brings the feature into the currently checked-out branch. `branch -d` removes the merged local branch; it does not delete a remote branch. For team projects, follow the team's pull request workflow instead of this local merge example.

If a merge reports conflicts, run `git status`, open each conflicted file, and resolve the sections marked by `<<<<<<<`, `=======`, and `>>>>>>>`. Preserve the intended result and remove the markers. For a conflict in `index.html`:

```sh
git add index.html
git diff --staged
git commit -m "Merge contact page and resolve conflicts"
```

Test before pushing. To cancel an in-progress merge, use `git merge --abort`. Start merges with a clean working directory so unrelated edits are not involved. See the [merge reference](https://git-scm.com/docs/git-merge).

## Example 5: Undo a mistake

**You staged a file that belongs in a later commit.** In a repository with an existing commit:

```sh
git restore --staged notes.txt
```

This removes the file's changes from staging while keeping your edits on disk.

**You want to discard an unsaved Git change to a tracked file.** Review it first:

```sh
git diff -- styles.css
git restore -- styles.css
```

The second command discards unstaged edits, replacing them with the staged version (or the committed version if nothing is staged). Git cannot normally recover edits it never saved. See the [restore reference](https://git-scm.com/docs/git-restore).

**A commit already shared with the team introduced a bug.** With a clean working directory, find the ordinary, non-merge commit and create a new commit that reverses it:

```sh
git log --oneline -5
git revert COMMIT-ID
```

Replace `COMMIT-ID` with the actual identifier from the log. Save and close the commit-message editor if it opens. Test the result, then push your branch or submit a pull request as your team requires. Revert preserves shared history. If it conflicts, resolve and stage the affected files, then run `git revert --continue`, or cancel with `git revert --abort`. See the [revert reference](https://git-scm.com/docs/git-revert).

## Example 6: Pause unfinished work for an urgent fix

You are editing a contact form when a teammate asks for help on another branch. Save the unfinished work temporarily:

```sh
git stash push -u -m "Unfinished contact form"
git switch main
```

Handle the urgent task on its own branch and commit it. Return to the original feature branch and restore the saved work:

```sh
git switch feature/contact-page
git stash list
git stash pop
```

`-u` includes untracked files, but not ignored files. `pop` reapplies the latest stash and removes it if successful. If applying it causes conflicts, resolve them; Git retains the stash, so inspect it before dropping it. A stash is local temporary storage, not a GitHub backup. See the [stash reference](https://git-scm.com/docs/git-stash).

## A routine to practice

Start by checking your branch and updating it appropriately. Make one focused change, review the diff, stage the relevant files, inspect the staged diff, commit with a useful message, and push. Open a pull request when working with a team. Use `git status` whenever you are unsure what happens next.

[Back to the index](../README.md) | [SSH and GitHub setup](ssh-github-setup.md)
