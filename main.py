import datetime
import requests
import tweepy
from os import environ

REPOS = 'repo:symfony/symfony repo:opsdroid/opsdroid repo:arduosoft/RawCMS repo:neovim/neovim repo:Marusyk/grok.net ' \
        'repo:unoplatform/uno repo:electron/electron repo:projectM-visualizer/projectm repo:yugabyte/yugabyte-db ' \
        'repo:LightTable/LightTable repo:sButtons/sbuttons repo:cockroachdb/cockroach repo:helm/helm ' \
        'repo:kubernetes/kubernetes repo:hashicorp/terraform repo:pingcap/tidb repo:bitfield/script ' \
        'repo:friendsofgo/killgrave repo:strongbox/strongbox repo:elastic/elasticsearch repo:JabRef/jabref ' \
        'repo:commons-app/apps-android-commons repo:authorjapps/zerocode repo:sirixdb/sirix repo:sirixdb/sirix ' \
        'repo:Swati4star/Images-to-PDF repo:trinodb/trino repo:appsmithorg/appsmith repo:osmlab/name-suggestion-index ' \
        'repo:openstreetmap/iD repo:Leaflet/Leaflet repo:eslint/eslint repo:webpack/webpack repo:TryGhost/Ghost ' \
        'repo:vercel/hyper repo:serverless/serverless repo:facebook/react repo:facebook/react-native ' \
        'repo:yarnpkg/yarn repo:vercel/next.js repo:keystonejs/keystone repo:Semantic-Org/Semantic-UI-React ' \
        'repo:electron/electron repo:botpress/botpress repo:cdnjs/cdnjs repo:wulkano/kap repo:fastify/fastify ' \
        'nodejs/node repo:facebook/jest repo:processing/p5.js repo:squirrellyjs/squirrelly ' \
        'repo:NativeScript/NativeScript repo:gatsbyjs/gatsby repo:vuejs/vue repo:oscarmorrison/md-page ' \
        'repo:jwu910/check-it-out repo:nukeop/nuclear repo:mui-org/material-ui repo:meteor/meteor repo:mochajs/mocha ' \
        'repo:babel/babel repo:danilowoz/create-content-loader repo:netlify/netlify-cms repo:imolorhe/altair ' \
        'repo:whyboris/Video-Hub-App repo:sirixdb/sirix-svelte-frontend repo:json-editor/json-editor ' \
        'repo:HabitRPG/habitica repo:reactjs/reactjs.org repo:ealush/vest repo: hoppscotch/hoppscotch repo: ' \
        'thamara/time-to-leave repo:Zooz/predator repo:vuejs/vue-cli repo:vuejs/vue-router repo:vuejs/vuepress ' \
        'repo:appsmithorg/appsmith repo:jayehernandez/letra-extension repo:swapagarwal/swag-for-dev ' \
        'repo:SimplQ/simplQ-frontendJuliaLang/julia repo:robstoll/atrium repo:sirixdb/sirix ' \
        'repo:LouisCAD/kotlin-libraries-playground repo:just-a-visitor/algorithmic-pseudocode repo:UPC/ravada ' \
        'repo:spatie/laravel-newsletter repo:appwrite/appwrite repo:nextcloud/server repo:PrestaShop/PrestaShop ' \
        'repo:flarum/core repo:CiviWiki/OpenCiviWiki repo:scrapy/scrapy repo:jupyter/notebook repo:zulip/zulip ' \
        'repo:aio-libs/create-aio-app repo:pandas-dev/pandas repo:saltstack/salt ' \
        'repo:legesher/tree-sitter-legesher-python repo:numpy/numpy repo:matplotlib/matplotlib ' \
        'repo:data-8/datascience repo:mindsdb/mindsdb repo:bokeh/bokeh repo:pytorch/pytorch ' \
        'repo:LucasPilla/Sorting-Algorithms-Visualizer repo:scikit-learn/scikit-learn '


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


def get_matching_issues():
    time = datetime.datetime.now() - datetime.timedelta(minutes=45)
    date = time.date()
    response = requests.get(f'https://api.github.com/search/issues?q={REPOS} created:>{date} label:"Good first issue"')
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
