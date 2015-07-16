# -*- coding:utf8 -*-

import os
from lastfmclient import LastfmClient


class ArtistInfo(object):

    def __init__(self, artist, client_api):
        self.name = artist['name']
        self.img = artist['image'][3]['#text']

        self.tags = []
        for tag in client_api.artist.get_top_tags(artist=self.name)['tag']:
            self.tags.append(tag['name'])

    def __repr__(self):
        return "{}".format(self.name)

    def __str__(self):
        return "{}".format(self.name)


class LastfmData(object):
    """
    Fetch some LastFm to publish.
    """

    def __init__(self, username, client_api):
        self.username = username
        self.api = client_api

    def get_user_info(self):
        user_info = self.api.user.get_info(user=self.username)
        return user_info

    def get_library_info(self):
        library_info = self.api.library.get_artist(user=self.username, limit=1)['@attr']
        return library_info

    def get_top_artists(self, limit=3, photo=True):
        top_artist = []

        for artist in self.api.user.get_top_artists(user=self.username, limit=limit)['artist']:
            top_artist.append(ArtistInfo(artist, self.api))

        return top_artist


if __name__ == '__main__':

    API_KEY = os.environ.get("API_KEY")
    API_SECRET = os.environ.get("API_SECRET")

    USERNAME = os.environ.get("USERNAME")

    api = LastfmClient(api_key=API_KEY, api_secret=API_SECRET)
    test = LastfmData(USERNAME, api)

    for a in test.get_top_artists():
        print "{0}: {1}".format(a.name, a.img)
