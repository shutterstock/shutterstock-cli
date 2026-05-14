import os
import unittest
from unittest.mock import patch

from requests.auth import HTTPBasicAuth
from shutterstock.utils.prettyprint import pretty_print
from shutterstock.utils.request import get, put, post, delete
from shutterstock.utils.request_helper import RequestHelper


class UtilTests(unittest.TestCase):
    """
    CLI Utility Tests
    """
    def test_pretty_print(self):
        """
        Tests pretty print function.
        """
        data = {"a": 1, "b": 2}
        self.assertLogs(pretty_print(data))


class RequestHelperTests(unittest.TestCase):
    """
    Request Helper Tests.
    """
    def setUp(self) -> None:
        self.key = "SHUTTERSTOCK_KEY"
        self.secret = "SHUTTERSTOCK_SECRET"
        self.token = "SHUTTERSTOCK_API_TOKEN"
        self.sandbox_mode = "SHUTTERSTOCK_SANDBOX"
        self.custom_url = "SHUTTERSTOCK_CUSTOM_URL"

        if self.key in os.environ:
            del os.environ[self.key]

        if self.secret in os.environ:
            del os.environ[self.secret]

        if self.token in os.environ:
            del os.environ[self.token]

        if self.sandbox_mode in os.environ:
            del os.environ[self.sandbox_mode]

        if self.custom_url in os.environ:
            del os.environ[self.custom_url]

    def test_request_helper_with_token(self):
        """
        Asserts we can set up header auth correctly.
        """
        os.environ[self.token] = "1"
        req = RequestHelper()
        self.assertEqual(req.headers, {"Authorization": "Bearer 1", "User-Agent": "Shutterstock-CLI", "x-shutterstock-application": "CLI"})
        self.assertIsNone(req.auth)

    def test_request_helper_with_auth(self):
        """
        Asserts we can set up basic auth correctly.
        """
        os.environ[self.key] = "a"
        os.environ[self.secret] = "b"
        req = RequestHelper()
        self.assertIsInstance(req.auth, HTTPBasicAuth)
        self.assertEqual(req.headers, {"User-Agent": "Shutterstock-CLI", "x-shutterstock-application": "CLI"})

    def test_request_helper_base_url(self):
        """
        Asserts we can set the base endpoint.
        """
        os.environ[self.sandbox_mode] = "true"
        req = RequestHelper()
        self.assertEqual(req.base_endpoint, "https://api-sandbox.shutterstock.com")


class RequestTests(unittest.TestCase):
    """
    Request Tests
    """

    def setUp(self) -> None:
        os.environ["SHUTTERSTOCK_API_TOKEN"] = "a"
        self.headers = {"x-shutterstock-application": "CLI", "User-Agent": "Shutterstock-CLI", "Authorization": "Bearer a"}
        self.response_data = {"a": 1, "b": 2}
        self.base_endpoint = "https://api.shutterstock.com"

    @patch("requests.get")
    def test_sandbox_enabled(self, mock_get):
        os.environ["SHUTTERSTOCK_SANDBOX"] = "true"
        mock_get.return_value.json.return_value = self.response_data
        url = "/v2/images/search"
        params = {"query": "poland"}
        get(url, params)
        mock_get.assert_called_with(
            url=f"https://api-sandbox.shutterstock.com{url}",
            params=params,
            headers=self.headers,
            auth=None,
        )
        self.assertLogs(pretty_print(self.response_data))

    @patch("requests.get")
    def test_sandbox_set_to_false(self, mock_get):
        os.environ["SHUTTERSTOCK_SANDBOX"] = "false"
        mock_get.return_value.json.return_value = self.response_data
        url = "/v2/images/search"
        params = {"query": "poland"}
        get(url, params)
        mock_get.assert_called_with(
            url=f"{self.base_endpoint}{url}",
            params=params,
            headers=self.headers,
            auth=None,
        )
        self.assertLogs(pretty_print(self.response_data))

    @patch("requests.get")
    def test_get(self, mock_get):
        """
        Asserts we are calling the GET function properly.
        """
        mock_get.return_value.json.return_value = self.response_data
        url = "/v2/images/search"
        params = {"query": "poland"}
        get(url, params)
        mock_get.assert_called_with(
            url=f"{self.base_endpoint}{url}",
            params=params,
            headers=self.headers,
            auth=None,
        )
        self.assertLogs(pretty_print(self.response_data))

    @patch("requests.post")
    def test_post(self, mock_post):
        """
        Asserts we are calling the POST function properly.
        """
        mock_post.return_value.json.return_value = self.response_data
        url = "/v2/images/search"
        params = {"query": "poland"}
        data = {"a": 1, "b": 2}
        post(url, params, data)
        mock_post.assert_called_with(
            url=f"{self.base_endpoint}{url}",
            json=data,
            params=params,
            headers=self.headers,
            auth=None,
        )
        self.assertLogs(pretty_print(self.response_data))

    @patch("requests.put")
    def test_put(self, mock_put):
        """
        Asserts we are calling the PUT function properly.
        """
        mock_put.return_value.json.return_value = self.response_data
        url = "/v2/images/search"
        params = {"query": "poland"}
        data = {"a": 1, "b": 2}
        put(url, params, data)
        mock_put.assert_called_with(
            url=f"{self.base_endpoint}{url}",
            params=params,
            json=data,
            headers=self.headers,
            auth=None,
        )
        self.assertLogs(pretty_print(self.response_data))

    @patch("requests.delete")
    def test_delete(self, mock_delete):
        """
        Asserts we are calling the DELETE function properly.
        """
        mock_delete.return_value.json.return_value = self.response_data
        url = "/v2/images/search"
        params = {"query": "poland"}
        data = {"a": 1, "b": 2}
        delete(url, params, data)
        mock_delete.assert_called_with(
            url=f"{self.base_endpoint}{url}",
            params=params,
            json=data,
            headers=self.headers,
            auth=None,
        )
        self.assertLogs(pretty_print(self.response_data))
