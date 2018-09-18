#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
import os
import timeit
import logging.handlers

PYTHON_LOGGER = logging.getLogger(__name__)
if not os.path.exists("log"):
    os.mkdir("log")
HDLR = logging.handlers.TimedRotatingFileHandler("log/Annuaire.log",
                                                 when="midnight", backupCount=60)
STREAM_HDLR = logging.StreamHandler()
FORMATTER = logging.Formatter("%(asctime)s %(filename)s [%(levelname)s] %(message)s")
HDLR.setFormatter(FORMATTER)
STREAM_HDLR.setFormatter(FORMATTER)
PYTHON_LOGGER.addHandler(HDLR)
PYTHON_LOGGER.addHandler(STREAM_HDLR)
PYTHON_LOGGER.setLevel(logging.DEBUG)

FOLDER_ABSOLUTE_PATH = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))


class Directory:

    def __init__(self):

        self.directory = {}

    def add_contact(self, name, tel):
        """

        :param name: (String) Name of the new user
        :param tel: (String) Telephone of the user
        :return:
        """
        self.directory[name] = tel
        return self.directory

    def found_telephone(self, name):
        """
        Found telephone number
        :param name: (String) Name to found is telephone number
        :return:
        """
        try:
            return self.directory[name.strip().lower()]
        except KeyError as e:
            PYTHON_LOGGER.error("Error Can found the telephone with this name {}: {}".format(name, e))
            return None

    def nb_telephone_number(self):
        """

        :return:
        """
        return len(self.directory)

    def get_directory(self):
        """

        :return:
        """

        return self.directory

    def del_contact(self, name):
        """

        :param name: (String) Name to delete
        :return:
        """
        try:
            del self.directory[name]
            return True
        except KeyError as e:
            PYTHON_LOGGER.error("Error Can delete the name {}: {}".format(name, e))
            return False

    def help(self):
        """

        :return:
        """
        return ["del_contact", "get_directory", "nb_telephone_number", "found_telephone", "add_contact"]
