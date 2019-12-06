pysigdump
=========

Use signal to show stacktrace and garbage collection stats of a Python process like `frsyuki/sigdump <https://github.com/frsyuki/sigdump>`_.

Usage
-----

Server example to enable sigdump is below:

.. code-block:: python

   import os
   from wsgiref.simple_server import make_server

   import sigdump


   def application(env, start_response):
       start_response('200 OK', [('Content-type', 'text/plain; charset=utf-8')])
       return [b'Hello World']


   if __name__ == '__main__':
       sigdump.enable(verbose=True)  # just calling sigdump.signal()

       print("pid:", os.getpid())
       httpd = make_server('', 8000, application)
       httpd.serve_forever()

.. code-block:: console

   $ pip install sigdump
   $ python example/wsgi.py
   pid: 57650
   SIGDUMP is enabled. The result is exported to /tmp/sigdump-57650.log.

Then sending a ``SIGCONT`` signal.
Please set ``SIGDUMP_SIGNAL`` environment variable if you want to change the signal.

.. code-block:: console

   $ kill -s SIGCONT 57650

See ``/tmp/sigdump-<pid>.log``.
Please set ``SIGDUMP_PATH`` environment variable if you want to change the output path.
You can set ``"-"`` here to dump to ``STDOUT``, or ``"+"`` to ``STDERR``.

.. code-block:: console

   $ less /tmp/sigdump-57650.log
   Sigdump at 2019-12-06 21:04:55.071633 process 57650

     Stacktrace:
     File "example/wsgi.py", line 15, in <module>
       httpd.serve_forever()
     File "/Users/c-bata/.pyenv/versions/3.7.1/lib/python3.7/socketserver.py", line 232, in serve_forever
       ready = selector.select(poll_interval)
     File "/Users/c-bata/.pyenv/versions/3.7.1/lib/python3.7/selectors.py", line 415, in select
       fd_event_list = self._selector.poll(timeout)

      GC stat:
        Generation 0:
          collections   : 33
          collected     : 99
          uncollectable : 0
        Generation 1:
          collections   : 2
          collected     : 253
          uncollectable : 0
        Generation 2:
          collections   : 0
          collected     : 0
          uncollectable : 0


LICENSE
-------

::

   MIT License

   Copyright (c) 2019 Masashi SHIBATA

   Permission is hereby granted, free of charge, to any person obtaining a copy
   of this software and associated documentation files (the "Software"), to deal
   in the Software without restriction, including without limitation the rights
   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
   copies of the Software, and to permit persons to whom the Software is
   furnished to do so, subject to the following conditions:

   The above copyright notice and this permission notice shall be included in all
   copies or substantial portions of the Software.

   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
   SOFTWARE.
