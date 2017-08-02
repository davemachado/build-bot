#!/usr/bin/env python3
import os
import sys
import json
import requests


def comment_on_pull_request(pr_number, slug, token, comment):
    """ Comment message on a given GitHub pull request. """
    url = '{api_url}/repos/{slug}/issues/{number}/comments'.format(
        api_url=GITHUB_API_URL, slug=slug, number=pr_number)
    response = requests.post(url, data=json.dumps({'body': comment}),
                             headers={'Authorization': 'token ' + token})
    return response.json()


if __name__ == '__main__':
    GITHUB_API_URL = 'https://api.github.com'
    TOKEN = os.environ.get('GH_TOKEN')
    PR_NUMBER = os.environ.get('TRAVIS_PULL_REQUEST')
    REPO_SLUG = os.environ.get('TRAVIS_REPO_SLUG')
    MESSAGE = os.environ.get('BUILD_BOT_MSG', None)

    results = sys.stdin.read().strip()
    comment = (
        """
-- Build Results --
```
{build_results}
```
        """).format(build_results=results)

    if all([PR_NUMBER, REPO_SLUG, TOKEN]):
        if results:
            comment_on_pull_request(PR_NUMBER, REPO_SLUG, TOKEN, comment)
        elif MESSAGE:
            comment_on_pull_request(PR_NUMBER, REPO_SLUG, TOKEN, MESSAGE)
    else:
        print('Not all neccesery enviroment variables are set')
