import simplejson as json
import oauth2
import requests
import argparse
from pprint import pprint
import sys
import urllib
import urllib2
import oauth2


# OAuth credential placeholders that must be filled in by users.
CONSUMER_KEY = 'EXMisJNWez_PuR5pr06hyQ'
CONSUMER_SECRET = 'VCK-4cDjtQ9Ra4HC5ltClNiJFXs'
TOKEN = 'AWYVs7Vim7mwYyT1BLJA2xhNTs_vXLYS'
TOKEN_SECRET = 'Rv4GrlYxYGhxUs14s0VBfk7JLJY'

API_HOST = 'api.yelp.com'
DEFAULT_TERM = 'pizza'
DEFAULT_LOCATION = 'Washington, DC'
SEARCH_LIMIT = 5
SEARCH_PATH = '/v2/search/'
BUSINESS_PATH = '/v2/business/'



from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

def search(term,location):

    auth = Oauth1Authenticator(
        consumer_key='EXMisJNWez_PuR5pr06hyQ',
        consumer_secret='VCK-4cDjtQ9Ra4HC5ltClNiJFXs',
        token='AWYVs7Vim7mwYyT1BLJA2xhNTs_vXLYS',
        token_secret='Rv4GrlYxYGhxUs14s0VBfk7JLJY'
    )

    client = Client(auth)

    params = {
        'term': term
    }

    results = []
    # ar = client.search(location, **params)
    response = client.search(location, **params)
    bizlist = response.businesses
    print(len(bizlist))
    for b in bizlist:
        bdict = {}
        bdict['name'] = b.name
        bdict['lat'] = float(b.location.coordinate.latitude)
        bdict['lon'] = float(b.location.coordinate.longitude)
        bdict['city'] = "{0}, {1}".format(b.location.city, b.location.state_code)
        bdict['address'] = b.location.address[0]

        results.append(bdict)


    return results


def search2(term, location):
    """Query the Search API by a search term and location.

    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.
        distance (int): The search distance to query from each route point.

    Returns:
        dict: The JSON response from the request.
    """

    print location
    # if float(distance) <= 5.0:
    #     radius = 0.75
    # elif float(distance) > 5.0 and float(distance) <= 10.0:
    #     radius = 1.5
    # elif float(distance) > 10.0 and float(distance) <= 25.0:
    #     radius = 4
    # elif float(distance) > 25.0 and float(distance) <= 100.0:
    #     radius = 8
    # elif float(distance) > 100.0:
    #     radius = 15

    # metradius = int(float(1609) * float(radius))
    # print metradius
    url_params = {
        'term': term.replace(' ', '+'),
        # 'radius_filter': metradius,
        'll': location.replace(' ', '+').replace(',',''),
        'limit': SEARCH_LIMIT
    }
    return request(API_HOST, SEARCH_PATH, url_params=url_params)


def locationsearch(location):
    """Query the Search API by a search term and location.

    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.
        distance (int): The search distance to query from each route point.

    Returns:
        dict: The JSON response from the request.
    """

    print location

    url_params = {
        'radius_filter': 2000,
        'll': location.replace(' ', '+').replace(',',''),
        'limit': 10
    }
    return request(API_HOST, SEARCH_PATH, url_params=url_params)



def request(host, path, url_params=None):
    """Prepares OAuth authentication and sends the request to the API.

    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        url_params (dict): An optional set of query parameters in the request.

    Returns:
        dict: The JSON response from the request.

    Raises:
        urllib2.HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    pprint(urllib.quote(path.encode('utf8')))
    url = 'https://{0}{1}?'.format(host, urllib.quote(path.encode('utf8')))

    consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    oauth_request = oauth2.Request(
        method="GET", url=url, parameters=url_params)

    oauth_request.update(
        {
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_timestamp': oauth2.generate_timestamp(),
            'oauth_token': TOKEN,
            'oauth_consumer_key': CONSUMER_KEY
        }
    )
    token = oauth2.Token(TOKEN, TOKEN_SECRET)
    oauth_request.sign_request(
        oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()

    print u'Querying {0} ...'.format(url)

    conn = urllib2.urlopen(signed_url, None)
    try:
        response = json.loads(conn.read())
    finally:
        conn.close()

    return response