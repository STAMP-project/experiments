#!/usr/bin/env python

from github3 import login

myToken="db9c0107e3cbc59effd12d063f7e70d9b3d80ba0"

githubLogin = login(token=myToken)
repo = githubLogin.repository('CaelProjects', 'experiments')

pullRequest = repo.create_pull('my PR', 'master', 'CaelProjects:branchForTest', 'foo')

import sys
sys.exit(1 if not pullRequest else 0)
