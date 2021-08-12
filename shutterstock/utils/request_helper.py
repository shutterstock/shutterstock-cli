""""
Request Helper.
"""

import os

from requests.auth import HTTPBasicAuth


class RequestHelper:
    """
    Request helper class.
    """

    def __init__(self):

        self.key = os.getenv("SHUTTERSTOCK_KEY")
        self.secret = os.getenv("SHUTTERSTOCK_SECRET")
        self.token = os.getenv("SHUTTERSTOCK_API_TOKEN")
        self.sandbox_mode = bool(os.getenv("SHUTTERSTOCK_SANDBOX"))
        self.custom_url = os.getenv("SHUTTERSTOCK_CUSTOM_URL")

        self._auth = None
        self._headers = None

        if self.token:
            self._headers = {"Authorization": f"Bearer {self.token}"}

        elif self.key and self.secret:
            self._auth = HTTPBasicAuth(self.key, self.secret)
            self._headers = {}

    @property
    def headers(self):
        """
        :return: Dict
        """
        return self._headers

    @property
    def auth(self):
        """
        :return: HTTPBasicAuth if key and secret is set, otherwise None.
        """
        return self._auth

    @property
    def base_endpoint(self):
        """
        :return: str
        """
        if self.sandbox_mode:
            return "https://api-sandbox.shutterstock.com"

        if self.custom_url is not None:
            return self.custom_url

        return "https://api.shutterstock.com"
