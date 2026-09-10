# Set up SSH keys and GitHub on Linux and macOS

[Back to the index](../README.md)

Git tracks changes on your computer. GitHub hosts repositories online. SSH keys let Git authenticate to GitHub from your terminal.

## 1. Prepare your account and tools

Create an account at [GitHub](https://github.com/signup), verify your email, and sign in. Open a terminal and check your tools:

```sh
git --version
ssh -V
```

If Git is missing, follow the [Git installation instructions](https://git-scm.com/downloads). On macOS, running `git --version` may prompt you to install Apple's Command Line Tools. On Linux, install Git and the OpenSSH client through your distribution's package manager if needed.

Set the name and email attached to your commits, replacing the examples:

```sh
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Use an email verified on GitHub, or your GitHub-provided private commit email from **Settings → Emails**. These settings label your commits; SSH handles authentication. `--global` applies to all repositories for your computer user. See [GitHub's Git setup guide](https://docs.github.com/en/get-started/git-basics/set-up-git).

## 2. Check for an existing key

```sh
ls -al ~/.ssh
```

A missing directory is normal on a new setup. A key pair commonly contains `id_ed25519` (private) and `id_ed25519.pub` (public). Reuse a suitable existing pair by skipping generation. Keep the private file on your computer; upload only the `.pub` file. Never commit private keys.

## 3. Generate a key and load it

Replace the email label:

```sh
ssh-keygen -t ed25519 -C "you@example.com"
```

Accept the default location only if unused. Never overwrite an existing key; choose another filename and substitute it throughout this guide. Enter and confirm a passphrase.

Start the agent:

```sh
eval "$(ssh-agent -s)"
```

On **Linux**, load the key:

```sh
ssh-add ~/.ssh/id_ed25519
```

On **macOS Monterey or later**, store the passphrase in Keychain:

```sh
/usr/bin/ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```

For automatic loading on macOS, create or edit `~/.ssh/config` in a text editor. Merge this into any existing GitHub entry, preserving other settings:

```text
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
```

Without a passphrase, omit `UseKeychain` and use plain `ssh-add`. Linux users may need to reload the key after signing in again. See [GitHub's key generation and agent instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) for platform details.

## 4. Add the public key to GitHub

On **macOS**, copy it directly:

```sh
pbcopy < ~/.ssh/id_ed25519.pub
```

On **Linux**, display it and copy the complete line:

```sh
cat ~/.ssh/id_ed25519.pub
```

1. Open GitHub **Settings → SSH and GPG keys**.
2. Choose **New SSH key**.
3. Give it a recognizable title, such as `School laptop`.
4. Select **Authentication Key** as the key type.
5. Paste the public key into **Key**, then select **Add SSH key**.
6. Complete any account confirmation GitHub requests.

Copy only the public key text, including its initial `ssh-ed25519`; exclude terminal prompts. See [GitHub's instructions for adding a key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

## 5. Test the connection

```sh
ssh -T git@github.com
```

Use the literal SSH user `git`, not your GitHub username. On the first connection, compare the displayed host fingerprint with [GitHub's published fingerprints](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints). Enter `yes` only if it matches; otherwise stop and investigate.

Success greets your GitHub username and reports successful authentication with no shell access. That is expected: GitHub provides Git hosting, not an interactive terminal. This successful test still exits with status `1`. See [GitHub's connection test guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection).

## 6. Use SSH with a repository

For a new local copy, open the repository on GitHub and select **Code → Local → SSH** to copy its address. Replace `OWNER` and `REPOSITORY` below:

```sh
git clone git@github.com:OWNER/REPOSITORY.git
cd REPOSITORY
```

If you already have a local clone, enter its directory and inspect the remote before changing it:

```sh
git remote -v
git remote set-url origin git@github.com:OWNER/REPOSITORY.git
git remote -v
```

Use your repository's actual SSH address. `set-url` expects an existing remote named `origin`; for a local repository without one, use `git remote add origin` with the address instead.

After editing a file, review and publish your change:

```sh
git status
git diff
git add path/to/changed-file
git commit -m "Describe your change"
git push -u origin HEAD
```

Replace the file path with the file you edited. The push targets your current branch, which you can check with `git branch --show-current`. You need write access, and repository rules may require pushing a feature branch and opening a pull request. For practice, use a repository you own.

## Troubleshooting

| Problem | What to check |
| --- | --- |
| `Permission denied (publickey)` | Run `ssh-add -l` to check loaded keys. Load the correct private key and confirm its matching public key is registered to your GitHub account. |
| Git still uses HTTPS | Run `git remote -v`; the URL should begin with `git@github.com:` for these instructions. |
| `Repository not found` | Check the owner, repository name, and your account's access. |
| `Could not open a connection to your authentication agent` | Start the agent and run `ssh-add` again in the same terminal. |
| Authentication works but a push is rejected | Check write access and branch rules. If your branch is behind, fetch and reconcile the changes before retrying. |

[Back to the index](../README.md) | [Next: Git commands and real-life examples](git-basics.md)
