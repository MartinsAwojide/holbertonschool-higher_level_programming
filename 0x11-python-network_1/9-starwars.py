#!/usr/bin/python3
"""
A Python script that takes in a string and sends a search request to the
Star Wars API
"""

import requests
import sys

if __name__ == "__main__":
    # Get the info requesting the api
    url = 'https://swapi.co/api/people'
    params = (('search', sys.argv[1]),)
    r = requests.get(url, params=params)

    # Convert to json
    res = r.json()

    # Print the count key
    print("Number of results: {}".format(res['count']))

    # Isolate the characters that is a list
    # Print each one of the results
    characters = res['results']
    for name in characters:
        print(name['name'])
