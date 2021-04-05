# Good first issues bot

Two things that the world needs are:
- More people contributing to open source, so we can share knowledge to create high quality software
- Another Twitter account

This is a [Twitter bot](https://twitter.com/liveOpenSource) that tweets when issues labelled as a good first issue are opened in [beginner-friendly open source Github repos](https://github.com/MunGell/awesome-for-beginners).

## To run locally
- Make sure you have Python 3 installed
- Apply for a [Twitter developer account](https://developer.twitter.com/en/apply-for-access) and create an app
- Set the environment variables TWITTER_API_KEY, TWITTER_API_SECRET_KEY, TWITTER_ACCESS_TOKEN, and TWITTER_ACCESS_TOKEN_SECRET with the variables generated for your app 
- Grant your app read and write permissions
- `pip install requests` and `pip install tweepy`
- Run main.py