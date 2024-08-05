# Git + GitHub Learning for Envisagenics Continuing Education #

### [W3 Schools Tutorial](https://www.w3schools.com/git/default.asp?remote=github) ###

## August 5, 2024 ##

### What is version control?

- Version: contents of a file at any given point in time
- Version control: group of systems/processes that manage changes made to documents, programs, directories
    - Should use if anything needs to be monitored or shared overtime
    - Allows tracking of files in different states, multiple people to work on anything at same time (simultaneous development)

### What is Git?

- Version control system for software development & data projects
    - Used for tracking code changes, tracking who made changes, coding collaboration
- Git is NOT Github!
    - You use git WITH GitHub
- Work with git using Terminal

### What is GitHub?

- Cloud-based git repository-hosting platform
- Makes tools that use Git

### Git Components Basics

- Store your project info in a repository (repo)
- Repos contain the files you create and edit, a "data" directory, and ".git" storage
    - .git is where Git records info about project's history --> DO NOT EDIT OR DELETE!
    - All info about a repo is stored under the repo's main directory, NOT any of the subdirectories (i.e. folders)

### Git Commandline Basics 

Check which version of git is installed in Terminal

```
cd
git --version
```

Configure Git
- Git needs to know who you are! Since typically working with git via Terminal, it's best to create a copy of your Git repos in your local computer directory (aka cloning)
- Connect your GitHub username and email

```
git config --global user.name "Floyd1229"
git config --global user.email "taylorfloyd36@gmail.com"
```

Create a Git folder and initialize Git on said folder

```
mkdir git_learning
cd git_learning
git init
```

Within the git_learning repo, create a markdown file called README.md and check it's Git status

```
nano README.md

# GitHub Practice Repository #

## This is a repository for me to practice and improve my Git and GitHub usage. ##

git status
```

Once finished making changes to README.md, next need to stage the file. Staged files = files ready to be committed (aka added) to the repo you want to add it to. Add README.md to the Staging Environment and check its status

```
git add README.md 
# Other ways to update all files you've created, copied, or worked on
# git add .
# git add --all
# git add -A

git status
```

Once files are staged, next step is to commit the changes we've made within the repo. Committing keeps tracks of progress and changes within a file as we work on it. Git considers each commit as a "save point" you can go back to. When making commits, ALWAYS include a short, concise message. Commits make it easier for you and others to see what changes were made and when.

Make a commit stating you created the README.md file

```
git commit -m "Created README.md file"
```

View history of comments for a repo

```
git log
```

In Git, a branch is a new/separate version of the main repo. 

Create a branch called "python_basics", check all available branches, and move into the python_basics branch

```
git branch python_basics
git branch
git checkout python_basics
# Can also do git switch python_basics
```

Copy the following script from the VM into the python_basics branch: /mnt/users/tfloyd/scripts/continuing_education/python_basics.py. Update README.md file 

```
cp /mnt/users/tfloyd/scripts/continuing_education/python_basics.py .
nano README.md
### Branches: ##
- python_basics: python learning scripts and resources
```

Check status of python_basics branch, add changes of both files to Staging Environment, check status again, and commit changes to python_basics branch. This new branch is different from the master/main branch.

```
git status
git add .
git status
git commit -m "Created python_basics branch, added python_basics.py script, updated README.md"
```

Let's imagine we're not done with the python_basics branch, but we made an error in README.md in master branch. You don't want to mess with master directly and not done working in python_basics branch, so create a new branch to deal with the emergency

```
git switch master
git checkout -b emergency_fix
nano README.md # Add the following after the first sentence.
Each branch will be associated with a programming language or test projects. Once scripts with the branches are "ready for production" (i.e. completed), they'll be merged onto the main branch.
```

Stage README.md, and commit

```
git add .
git commit -m "Fixed error in README.md"
```

Now we have a fix ready for the master branch, and we need to merge emergency_fix and master. Switch to the branch you want the changes to be in, then merge the branches together. Make sure README.md has the incorporated changes. Since master and emergency_fix are now the same, delete emergency_fix since it's no longer needed

```
git switch master
git merge emergency_fix
less README.md
git branch -d emergency_fix
```

Now try to merge python_basics with master. You'll get an error because you didn't stage and commit changes made to README.md when working in the python_basics branch BEFORE changing it in master with emergency_fix branch. Once you get the error, check out the status and fix README.md

```
git merge python_basics
git status
nano README.md
```

Stage README.md and python_basics.py. If the conflicts are all fixed, commit to complete the merge. Check README.md to make sure incorporated changes are there. If branch no longer needed, delete it.

```
git add .
git status
git commit -m "Merged with python_basics after fixing README.md conflicts"
#git branch -d python_basics
```

Do the following on github.com: To connect your local repo to GitHub, go to github.com and create a repo named "git-learning". Copy the URL of the GitHub "git_learning" repo 

Do the following in Terminal: Copy the git_learning URL, push the local master branch to git-learning in GitHub and set master branch as the default remote branch

```
git remote add origin https://github.com/Floyd1229/git-learning.git
git push --set-upstream origin master
```

START ON SECTION "Pull from GitHub"
https://www.w3schools.com/git/git_pull_from_remote.asp?remote=github