#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


import logging

class CLog:

   #   print logging & write logging to log.txt
   def __init__(self):
      self.logger = logging.getLogger()
      fileHandler = logging.FileHandler(app.config['LOG_PATH'])
      formatHandler = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
      fileHandler.setFormatter(formatHandler)

      console = logging.StreamHandler()
      formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
      console.setFormatter(formatter)

      self.logger.addHandler(console)
      self.logger.addHandler(fileHandler)
      self.logger.setLevel(logging.NOTSET)

   def DebugMessage(self,msg):
      self.logger.debug(msg)
      pass


logger = CLog()