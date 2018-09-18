#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Start XmlRps Server

Script to start the contact directory manager XmlRps Server

Usage:
   server.py <ip> <port>

Options:
    -h --help            Show this screen.
    <ip>                 Ip where the server will lisen
    <port>               Port where the server will lisen
"""

from __future__ import absolute_import
import os
from docopt import docopt
import logging.handlers
from xmlrpc.server import SimpleXMLRPCServer

from directory import Directory

PYTHON_LOGGER = logging.getLogger(__name__)
if not os.path.exists("log"):
    os.mkdir("log")
HDLR = logging.handlers.TimedRotatingFileHandler("log/server.log",
                                                 when="midnight", backupCount=60)
STREAM_HDLR = logging.StreamHandler()
FORMATTER = logging.Formatter("%(asctime)s %(filename)s [%(levelname)s] %(message)s")
HDLR.setFormatter(FORMATTER)
STREAM_HDLR.setFormatter(FORMATTER)
PYTHON_LOGGER.addHandler(HDLR)
PYTHON_LOGGER.addHandler(STREAM_HDLR)
PYTHON_LOGGER.setLevel(logging.DEBUG)

FOLDER_ABSOLUTE_PATH = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))


def is_even(n):
    return n % 2 == 0


def start_server(ip, port):

    server = SimpleXMLRPCServer((ip, port))
    PYTHON_LOGGER.info("Server listen at adresse {} port {}".format(ip, port))
    server.register_function(Directory(), "directory_class")
    server.serve_forever()
    PYTHON_LOGGER.info("Server stop")


if __name__ == "__main__":

    arguments = docopt(__doc__)
    ip = arguments["<ip>"]
    port = arguments["<port>"]
    try:
        start_server(ip, int(port))
    except Exception as e:
        PYTHON_LOGGER.error("Error in the server execution: {}".format(e))
