#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Start XmlRps Client

Script to start the contact directory manager XmlRps Client

Usage:
   server.py <ip> <port>

Options:
    -h --help            Show this screen.
    <ip>                 Ip of the server
    <port>               Port wod the server
"""

from __future__ import absolute_import
import os
import xmlrpc.client
import logging.handlers

from docopt import docopt

PYTHON_LOGGER = logging.getLogger(__name__)
if not os.path.exists("log"):
    os.mkdir("log")
HDLR = logging.handlers.TimedRotatingFileHandler("log/client.log",
                                                 when="midnight", backupCount=60)
STREAM_HDLR = logging.StreamHandler()
FORMATTER = logging.Formatter("%(asctime)s %(filename)s [%(levelname)s] %(message)s")
HDLR.setFormatter(FORMATTER)
STREAM_HDLR.setFormatter(FORMATTER)
PYTHON_LOGGER.addHandler(HDLR)
PYTHON_LOGGER.addHandler(STREAM_HDLR)
PYTHON_LOGGER.setLevel(logging.DEBUG)

FOLDER_ABSOLUTE_PATH = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))


def start_client(ip, port):
    """

    :param ip:
    :param port:
    :return:
    """
    with xmlrpc.client.ServerProxy("http://{}:{}".format(ip, port)) as proxy:
        while True:
            command = input("Function\n\tdel_contact(name)\n\tget_directory()\n\t"
                            "nb_telephone_number()\n\tfound_telephone(name)\n\t"
                            "add_contact(name, telephone)\n'exit' to stop the client\n>>>")

            if command == "exit":
                break

            try:
                function_name, param = command.split("(")
                param = param.replace(")", "")
                param_list = param.split(",")
            except Exception as e:
                PYTHON_LOGGER.error("Error syntax: {}".format(e))
                continue

            if function_name == "del_contact":
                result = proxy.directory_class.del_contact(*param_list)
            elif function_name == "get_directory":
                result = proxy.directory_class.get_directory(*param_list)
            elif function_name == "nb_telephone_number":
                result = proxy.directory_class.nb_telephone_number(*param_list)
            elif function_name == "found_telephone":
                result = proxy.directory_class.found_telephone(*param_list)
            elif function_name == "add_contact":
                result = proxy.directory_class.add_contact(*param_list)
            else:
                result = "Command not found"

            PYTHON_LOGGER.info("Result: {}".format(result))


if __name__ == "__main__":

    arguments = docopt(__doc__)
    ip = arguments["<ip>"]
    port = arguments["<port>"]
    try:
        start_client(ip, port)
    except Exception as e:
        PYTHON_LOGGER.error("Error in the client execution: {}".format(e))


