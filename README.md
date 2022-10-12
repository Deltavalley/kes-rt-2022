# kes-rt-2022
Solutions to rt 2022 problems 

## Contribution rules
To avoid people's solutions conflicting and causing confusion, each question will have its own folder.  In that folder, create a folder with your name (eg "adam smith") to save your work into.  You can make changes to other people's code but only through a pull request.

## Contributing
1. Create a GitHub account and login
2. Clone `kes-rt-2022` (this repo) into your IDE of choice (the link is: `https://github.com/Deltavalley/kes-rt-2022/`)
    - _this will clone the main branch, which has restricted write permission_
3. Go to your IDE of choice and create a new branch called your name (eg "adam-smith")
    - _this is copying the main branch. you can change this copy_
4. Code (or dont..?) however you want, you can make as many commits as you want since its your own branch
5. After you have finished, go to GitHub.com, find your branch on this repo and submit a "Pull Request" 
    - _a pull request is a request to have your branch merged with the master branch_
6. I'll approve your commit (hopefully) and it'll get merged into `kes-rt-2022/master`, so other people can download and view it.
    - _technically anyone can rebase off any branch so you dont have to submit a pull request to master to share your code with a friend_

## Resetting your branch
Your branch remains static in relation to the `master` branch from the moment it is created or reset.  This means you cannot fetch any changes that are made to `kes-rt-2022` directly by just fetching your branch.
To fetch changes made to `kes-rt-2022/master` into your branch, you need to reset your branch.  This updates your branch to the latest version of `kes-rt-2022/master`.  You will lose any changes to your branch that have not been committed and approved.  
To reset your branch in VS2022:
1. In the top bar, go to `Git>Manage Branches`
2. On the left panel, right click the `master` branch and press "Checkout"
3. Right click the `master` branch and press pull
4. Right click your branch and press `Reset>Delete Changes (--hard)`
5. Confirm your choice
