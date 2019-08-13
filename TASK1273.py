# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 23:50:32 2019

@author: User
"""

import re
id=input()
if re.search(r'201[6-9]+[AB]+[1-9]+[AB]?[1-9]?[PTH]\S+0+[1-9]*[PGH]+',id):
    print("match")
elif re.search(r'201[1-5]+[AB]+[1-9]+[AB]?[1-9]?[PHT]\S+[1-9]*[PGH]',id):
    print("match1")
    