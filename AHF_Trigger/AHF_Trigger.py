#! /usr/bin/python3
#-*-coding: utf-8 -*-
import sys
sys.path.append("../..")

from abc import ABCMeta, abstractmethod
from AutoHeadFix.AHF_Base import AHF_Base
import os
import inspect

class AHF_Trigger(AHF_Base, metaclass = ABCMeta):
    """
    Sends/receives signals as to another pi to start/stop recording

    """
    
    @abstractmethod
    def doTrigger(self, message):
       pass

    @abstractmethod
    def getTrigger(self):
        pass
