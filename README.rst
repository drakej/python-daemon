=================
python-daemon
=================

A simple python daemon which you can use to daemonize processes or 
to create cron like tasks in python.

===============
 Installation
===============

1. Download the tarball and run ``python setup.py install``

2. Copy the ``daemonexample.py`` to ``/etc/init.d`` and modify it to suite your needs

3. When you are done, make it an executable ``chmod +x /etc/init.d/daemonexample.py``. 
   
=========
 Usage 
=========

You can use it like any other UNIX daemon. On Linux

    ``invoke-rc.d daemonexample start|stop|restart|status``

And on MacOS

    ``python daemonexample.py start|stop|restart|status``

=================
 Additional notes
=================

Forked from martinrusev/python-daemon
Doesn't work well with ``virtualenv``

===============
 Requirements
===============

Python 2.5+
