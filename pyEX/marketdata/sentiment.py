# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the jupyterlab_templates library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from .sse import _runSSE, _runSSEAsync


def sentimentSSE(symbols=None, on_data=None, token="", version=""):
    """Stream social sentiment

    https://iexcloud.io/docs/api/#sse-streaming

    Args:
        symbols (str): Tickers to request
        on_data (function): Callback on data
        token (str): Access token
        version (str): API version
    """
    return _runSSE("sentiment", symbols, on_data, token, version)


async def sentimentSSEAsync(symbols=None, token="", version=""):
    """Stream social sentiment

    https://iexcloud.io/docs/api/#sse-streaming

    Args:
        symbols (str): Tickers to request
        on_data (function): Callback on data
        token (str): Access token
        version (str): API version
    """
    async for item in _runSSEAsync("sentiment", symbols, token, version):
        yield item
