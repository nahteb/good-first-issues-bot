import datetime
import requests
import tweepy
from os import environ


def authenticate_twitter():
    api_key = environ['TWITTER_API_KEY']
    api_secret_key = environ['TWITTER_API_SECRET_KEY']
    access_token = environ['TWITTER_ACCESS_TOKEN']
    access_token_secret = environ['TWITTER_ACCESS_TOKEN_SECRET']
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
    return api

def get_repos():
    repos = ''
    with open('repos.txt') as f:
        for line in f:
            repos += ' repo:' + line.strip()
        return repos


def get_matching_issues():
    time = datetime.datetime.now() - datetime.timedelta(hours=24)
    date = time.date()
    repos = get_repos()
    response = requests.get(f'https://api.github.com/search/issues?q={repos} created:>{date} label:"Good first issue"')
    data = response.json()
    return data['items']


def tweet_matching_issues(issues):
    for issue in issues:
        url = issue['html_url']
        language = get_repo_language(issue)
        if language is None:
            api.update_status(f'A new beginner friendly #openSource issue is ready for you! {url}')
        else:
            api.update_status(f'Want to learn #{language}? A new beginner friendly #openSource issue is ready for you! {url}')


def get_repo_language(issue):
    github_api_token = environ['API_TOKEN']
    repository_url = issue['repository_url']
    languages_url = f'{repository_url}/languages'
    languages = requests.get(languages_url, headers={'Authorization': f'token {github_api_token}'})
    data = languages.json()
    if len(data) < 1:
        return None
    else:
        language = list(data.keys())[0]
        return language


if __name__ == '__main__':
    api = authenticate_twitter()
    issues = get_matching_issues()
    tweet_matching_issues(issues)
