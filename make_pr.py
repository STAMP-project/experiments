#!/usr/bin/env python

from github3 import login

# myToken="db9c0107e3cbc59effd12d063f7e70d9b3d80ba0"
myToken="75026ee8330c1dae2a0d31e69dda1d5e78828d73"

githubLogin = login(token=myToken)
repo = githubLogin.repository('CaelProjects', 'experiments')

pullRequest = repo.create_pull('my PR', 'master', 'CaelProjects:branchForTest', 'foo')

import sys
sys.exit(1 if not pullRequest else 0)
