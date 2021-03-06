# Quantum Programming API

This API aims to create an infrastructure where programmers can use the power of quantum systems and quantum algorithms in every day programs. The goal of this project is to eventually have plug-and-play package that allows progammers to easily incorporate real quantum computing power into their projects.

**NOTE:** This project is in the development stage.

## Installation

We highly recommend using a virtual environment when interacting with the API. You can create, activate, and install the dependencies with the command sequence:

```
python -m venv env
source env/bin/activate
pip install --upgrade pip && pip install -r requirements.txt
```

You can then activate and reactivate your environment to your liking with:

```
deactivate
source env/bin/activate
```

## Contributing

Contributions are only accepted via pull requests. See [Creating A Pull Request](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request#changing-the-branch-range-and-destination-repository) to see how to do so.

For now, you can either submit a pull request via a forked repository, or just create a branch pertaining to the issue and submit a PR from there.

#### If you're submitting from a forked repository:

Make sure to set your track the main repo with:

```
git remote add upstream https://github.com/seunomonije/quantum-programming-api.git
```

and then update your local master branch with the main repo's master branch with:

```
git fetch upstream
git checkout master
git merge upstream/master
```

Alternatively, you can use `git pull upstream master`.

Don't forget to `git push` after to sync your online and offline repositories.

#### If you're submitting from just a separate branch:

Make sure your local copy of the repo is up to date with `git pull origin master` before
you start making any changes, big or small. Failing to keep in touch with the master branch
can cause numerous conflicts.

