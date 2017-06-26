"""Partial implementation of a Piwik Reporting API Client."""

from urllib.parse import urlencode
from json.decoder import JSONDecodeError
import requests
from . import modules
from .base import BaseModule


class PiwikAPI:

    """Piwik Reporting API client class."""

    REQUEST_ARGS = {
        'format': 'json',
        'module': 'API'
    }

    def __init__(self, url, token):
        """Set up the API client instance."""
        self.url = url
        self.REQUEST_ARGS['token_auth'] = token

        for name in dir(modules):
            module = getattr(modules, name)
            if (isinstance(module, type) and
                    issubclass(module, BaseModule) and
                    name != BaseModule.__name__):
                setattr(self, name, module(self))

    def request(self, **kwargs):
        """Make a request to retrieve some data.

        Args:
            http_method str: HTTP verb (POST or GET).
            **kwargs: Other parameters to send with the request.

        Returns:
            An object corresponding to the JSON we received.
        """
        request_args = self.REQUEST_ARGS.copy()
        request_args.update(**kwargs)
        r = requests.get(self.url, request_args)
        try:
            json = r.json()
        except JSONDecodeError:
            raise PiwikAPIError('The Piwik API did not return valid JSON.')
        if isinstance(json, dict) and json.get('result') == 'error':
            raise PiwikAPIError(json.get('message'))
        return json

    def bulk_request(self, requests=[]):
        """Make multiple requests at once.

        Args:
            http_method str: HTTP verb (POST or GET).
            requests list[dict]: List of dictionaries of request args.

        Returns:
            list[object]: List of objects corresponding to the JSON we received.
        """
        request_args = {
            'method': 'API.getBulkRequest',
            'urls[]': [urlencode(r) for r in requests]
        }
        return self.request(**request_args)


class PiwikAPIError(Exception):

    """Piwik Reporting API error class."""

    pass
