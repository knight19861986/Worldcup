==================================
World Cup Groupping Tool
==================================

Description
============


   

Key Features
============

- Randomly result a grouping for FIFA world cup 2018, according to grouping rules of FIFA 
- Calculate the probability of  country teams being in one group
- Calculate the probability of a country team avoiding several certain country teams being in one group


Getting started
===============

Client
------

To retrieve something from the web:

.. code-block:: python

  import aiohttp
  import asyncio
  import async_timeout

  async def fetch(session, url):
      async with async_timeout.timeout(10):
          async with session.get(url) as response:
              return await response.text()

  async def main():
      async with aiohttp.ClientSession() as session:
          html = await fetch(session, 'http://python.org')
          print(html)

  if __name__ == '__main__':
      loop = asyncio.get_event_loop()
      loop.run_until_complete(main())


Server
------

This is simple usage example:

.. code-block:: python

    from aiohttp import web

    async def handle(request):
        name = request.match_info.get('name', "Anonymous")
        text = "Hello, " + name
        return web.Response(text=text)

    async def wshandler(request):
        ws = web.WebSocketResponse()
        await ws.prepare(request)

        async for msg in ws:
            if msg.type == web.MsgType.text:
                await ws.send_str("Hello, {}".format(msg.data))
            elif msg.type == web.MsgType.binary:
                await ws.send_bytes(msg.data)
            elif msg.type == web.MsgType.close:
                break

        return ws


    app = web.Application()
    app.router.add_get('/echo', wshandler)
    app.router.add_get('/', handle)
    app.router.add_get('/{name}', handle)

    web.run_app(app)


Documentation
=============

https://aiohttp.readthedocs.io/

External links
==============

* `Third party libraries
  <http://aiohttp.readthedocs.io/en/latest/third_party.html>`_
* `Built with aiohttp
  <http://aiohttp.readthedocs.io/en/latest/built_with.html>`_
* `Powered by aiohttp
  <http://aiohttp.readthedocs.io/en/latest/powered_by.html>`_

Feel free to make a Pull Request for adding your link to these pages!


Communication channels
======================

*aio-libs* google group: https://groups.google.com/forum/#!forum/aio-libs

Feel free to post your questions and ideas here.

*gitter chat* https://gitter.im/aio-libs/Lobby

We support `Stack Overflow
<https://stackoverflow.com/questions/tagged/aiohttp>`_.
Please add *aiohttp* tag to your question there.

Requirements
============

- Python >= 3.4.2
- async-timeout_
- chardet_
- multidict_
- yarl_

Optionally you may install the cChardet_ and aiodns_ libraries (highly
recommended for sake of speed).

.. _chardet: https://pypi.python.org/pypi/chardet
.. _aiodns: https://pypi.python.org/pypi/aiodns
.. _multidict: https://pypi.python.org/pypi/multidict
.. _yarl: https://pypi.python.org/pypi/yarl
.. _async-timeout: https://pypi.python.org/pypi/async_timeout
.. _cChardet: https://pypi.python.org/pypi/cchardet

License
=======

``aiohttp`` is offered under the Apache 2 license.


Keepsafe
========

The aiohttp community would like to thank Keepsafe
(https://www.getkeepsafe.com) for it's support in the early days of
the project.


Source code
===========

The latest developer version is available in a github repository:
https://github.com/aio-libs/aiohttp

Benchmarks
==========

If you are interested in by efficiency, AsyncIO community maintains a
list of benchmarks on the official wiki:
https://github.com/python/asyncio/wiki/Benchmarks
