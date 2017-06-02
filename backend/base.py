#!/usr/bin/env python
# coding=utf-8


import logging
import logging.config

from db_wrapper import api as SQL



class Base(object):
    def __init__(self, logger_name):
        super(Base, self).__init__()

        # dadabase hanlder
        self.sql = SQL

        # log hanlder
        logging.config.fileConfig("logging.ini")
        self.log = logging.getLogger(logger_name)

        self.msg_success = "Operation completed."
        self.msg_failed = "Failed to complete the operation."

        

    def _response(self, msg, success=False, len=-1):
        response = {"state":0}
        if success:
            response["state"] = 1
        if len:
            response["len"] = len
        response["info"] = msg
        return response
