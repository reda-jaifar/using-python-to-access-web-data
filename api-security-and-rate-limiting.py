__author__ = 'MJR2'
import urllib
import oauth
import hidden

def augment(url, parameters):
    secrets= hidden.oauth()
    consumer= oauth.oAuth