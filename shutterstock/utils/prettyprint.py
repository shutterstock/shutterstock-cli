"""
Pretty printing.
"""

import json

from pygments import formatters
from pygments import highlight
from pygments import lexers


def pretty_print(data):
    """
    Pretty prints JSON data.
    :param data: Dict
    :return: None
    """
    formatted_json = json.dumps(data, sort_keys=True, indent=4)
    print(
        highlight(
            str(formatted_json).encode("utf-8"),
            lexers.JsonLexer(),
            formatters.TerminalFormatter(),
        )
    )
