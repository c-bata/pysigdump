pysigdump: sigdump for Python
=============================

Use signal to show stacktrace and garbage collection stats of a Python process like [frsyuki/sigdump](https://github.com/frsyuki/sigdump).

Usage
-----

Example code to enable sigdump in a server is below:

.. code-block:: python

   import os
   from wsgiref.simple_server import make_server

   import sigdump


   def application(env, start_response):
       start_response('200 OK', [('Content-type', 'text/plain; charset=utf-8')])
       return [b'Hello World']


   if __name__ == '__main__':
       sigdump.enable(verbose=True)  # just callig sigdump.signal()

       print("pid:", os.getpid())
       httpd = make_server('', 8000, application)
       httpd.serve_forever()

Then sending a SIGCONT signal.
 Please set `SIGDUMP_SIGNAL` environment variable if you want to change the signal (default: `SIGCONT`).

.. code-block:: console

   $ kill -s SIGCONT <pid>

See ``/tmp/sigdump-<pid>.log`.
Please set `SIGDUMP_PATH` environment variable if you want to change the output path (default: /tmp/sigdump-<pid>.log).
You can set `"-"` here to dump to STDOUT, or "+" to STDERR.

.. code-block:: console

   $ less /tmp/sigdump-<pid>.log
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
         collections : 33
         collected   : 99
         uncollected : None
       Generation 1:
         collections : 2
         collected   : 253
         uncollected : None
       Generation 2:
         collections : 0
         collected   : 0

