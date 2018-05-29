#!/usr/bin/env python3

import sys
import pathlib
from github3 import login

myFile = pathlib.Path.home().joinpath('.github_token').open()
myToken = myFile.readline()[:-1]

# print(myToken)

githubLogin = login(token=myToken)
repo = githubLogin.repository('CaelProjects', 'experiments')

pullRequest = repo.create_pull('my PR', 'master', 'CaelInria:branchForTest', 'foo')

sys.exit(1 if not pullRequest else 0)
