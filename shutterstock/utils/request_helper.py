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
        self.sandbox_mode = (
            True if os.getenv("SHUTTERSTOCK_SANDBOX") == "true" else False
        )
        self.custom_url = os.getenv("SHUTTERSTOCK_CUSTOM_URL")

        self._auth = None
        self._headers = {
            "User-Agent": "Shutterstock-CLI",
            "x-shutterstock-application": "CLI",
        }

        if self.token:
            self._headers.update({"Authorization": f"Bearer {self.token}"})

        elif self.key and self.secret:
            self._auth = HTTPBasicAuth(self.key, self.secret)

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
