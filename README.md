# shutterstock-cli

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A command-line utility that allows you to interact with the Shutterstock public API. For more information about the CLI and the API, see the [Shutterstock API reference](https://api-reference.shutterstock.com/).

## Installation

The Shutterstock CLI is available on the [Python Package Index (PyPI)](https://pypi.org/project/shutterstock-cli/). You can install it using pip.

``` bash
pip install shutterstock-cli
```

## Authentication

### Basic authentication

All endpoints in the Shutterstock API require authentication.
The API accepts HTTP basic authentication for some endpoints and OAuth authentication for all endpoints.

The API accepts HTTP basic authentication (also known as _basic authentication_) for some endpoints that do not access specific customer information.
Follow these steps to use basic authentication:

1. Create an account at https://www.shutterstock.com if you don't already have one.
2. Set up an application at https://www.shutterstock.com/account/developers/apps and get the consumer key and consumer secret from the application.
3. Export the consumer key and consumer secret as environment variables:

```bash
export SHUTTERSTOCK_KEY='YOUR_KEY'
export SHUTTERSTOCK_SECRET='YOUR_SECRET'
```

### OAuth authentication

Most endpoints require OAuth 2.0 authentication.
In this type of authentication, you use an application and an individual user's login credentials to obtain a token.
Then you can use that token as credentials for API requests in place of a user name and password.

Some endpoints require one or more _scopes_, or permissions, which let the user control what the application can do with the token.
For example, to edit a user's collections, the token must include the `collections.edit` scope.
Applications can request multiple tokens with different scopes or a single token with multiple scopes.

#### Getting tokens from your account page

As a shortcut, you can get a token directly from an application on your account page:

1. Create an account at https://www.shutterstock.com if you don't already have one.
2. Set up an application at https://www.shutterstock.com/account/developers/apps.
3. On the application details page, under **Token**, click **Generate token**.
4. On the Select scopes page, select the scopes for the token.
   The token automatically has scopes that allow it to run basic tasks.
   You can add scopes that allow it to access your licenses and collections.
5. Click **Continue**.
6. In the popup window, sign in to your shutterstock.com account.

The popup window shows the token. Copy it immediately, because it is shown only once.
The token is valid until the user account that you logged in with changes its password or email address.

Keep this token private, because other people could use it to access the account's subscriptions and media.

To use this token to authenticate your CLI commands, set it as the value of the `SHUTTERSTOCK_API_TOKEN` environment variable:

```bash
export SHUTTERSTOCK_API_TOKEN='YOUR_BEARER_TOKEN'
```

## Usage

Run `shutterstock --help` to see the available commands. You can also run shutterstock groupName --help or shutterstock groupName commandName --help to get help on a group of commands or on an individual command.

```bash
Usage: shutterstock [OPTIONS] COMMAND [ARGS]

Options:
  --help  Show this message and exit.

Commands are organized into these groups. To get a list of commands in a group, run shutterstock groupName --help.

Groups:
  ai
  audio
  contributors
  cv
  editorial
  images
  test
  user
  videos
```

### Formatting JSON Output

If you would like to colorize the JSON response output you can set the `SHUTTERSTOCK_CLI_COLORIZE_OUTPUT` environment variable:

```bash
export SHUTTERSTOCK_CLI_COLORIZE_OUTPUT='true'
```

### Sandbox

To make requests to the licensing sandbox API instead of the main API, set the `SHUTTERSTOCK_SANDBOX` environment variable to true.

For more information about the sandbox, see https://api-reference.shutterstock.com/#licensing-and-downloading-licensing-sandbox.

```bash
export SHUTTERSTOCK_SANDBOX='true'
```

### Examples

Search for images of boats with an aspect ratio of 1.6.

```bash
shutterstock images search-images --query boats --aspect-ratio 1.6
```

Get information about an image, including a URL to a preview image and the sizes that it is available in.

```bash
shutterstock images get-image 1269188995
```

Get a list of existing image licenses for a specified time period.

```bash
shutterstock images get-image-license-list --start-date 2020-03-03T12:00:00Z --end-date 2020-03-04T12:00:00Z
```

Get images that are visually similar to an image that you specify.

```bash
shutterstock images get-similar-images 1269188995 --language en --per-page 200 --view minimal
```

License an image.

```bash
shutterstock images license-images path/to/payload.json --subscription-id s123abc
```

Get your image license history over a specified time period.

```bash
shutterstock images get-image-license-list --start-date 2021-01-01T12:00:00Z --end-date 2021-03-01T12:00:00Z
```

Get the public URL of the image that you have already received a license for.

```bash
shutterstock images download-image license-id-123 payload.json
```

For more examples, see the [Shutterstock API reference](https://api-reference.shutterstock.com/).

## Development

**Creating virtual environment**

```bash
python3 -m venv [NAME_FOR_YOUR_VIRTUAL_ENV]
```

**Activating virtual environment**

```bash
source [NAME_FOR_YOUR_VIRTUAL_ENV]/bin/activate
```

**Install app in virtual environment**

```bash
python setup.py install
```

**Install the requirements**

```bash
pip3 install -r requirements.txt
```

**Utilize installed app**

```bash
shutterstock --help
```

**Deactivating virtual environment**

You can deactivate the virtual environment by simply running the command below.

```bash
deactivate
```

### Running Tests

```
coverage run --omit 'env/*' -m unittest tests/*.py && coverage report -m
```

### Contributing

- Fork the project and clone locally.
- Create a new branch for what you're going to work on.
- Push to your origin repository.
- Create a new pull request in GitHub.
