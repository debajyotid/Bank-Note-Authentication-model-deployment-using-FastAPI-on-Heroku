# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:51:19 2020
Modified on Thurs Sep 2 18:30 2021

@author: KrishNaik
@modified by: DebajyotiDas
"""
from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class BankNote(BaseModel):
    variance: float 
    skewness: float 
    curtosis: float 
    entropy: float