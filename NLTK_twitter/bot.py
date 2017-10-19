import nltk
from nltk.twitter import Twitter




# access_token = "918706943593549824-Z3gQO9jTS3UMxR2b4d1YP4gRrWstELr"
# access_token_secret = "Q93Y5ocsuLDKVrZIWgDkZTQaXEliO9KcikLHzpEFmpAaN"
# consumer_key = "xoUFitbD6pKfkjLBkF7SVj0iw"
# consumer_secret ="Lpgv9bgi2ns6wppoCyu8tX6JALe6vjAOZbxviEcaMo7S61sa2e"
# oauth_token = "918706943593549824-Z3gQO9jTS3UMxR2b4d1YP4gRrWstELr"
# oauth_token_secret = "Q93Y5ocsuLDKVrZIWgDkZTQaXEliO9KcikLHzpEFmpAaN"
# app_key = "xoUFitbD6pKfkjLBkF7SVj0iw"
# app_secret ="Lpgv9bgi2ns6wppoCyu8tX6JALe6vjAOZbxviEcaMo7S61sa2e"

tw = Twitter()

tw.tweets(keywords = 'cher, python, nlp, soccer, celine dion', limit =10)

