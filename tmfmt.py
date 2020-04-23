#! /usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime
import sys

timestamp = float(sys.argv[1])
if len(sys.argv[1]) == 13:
    timestamp = timestamp/1000.0
local_str_time = datetime.fromtimestamp(
    timestamp).strftime('%Y-%m-%d %H:%M:%S.%f')
print(local_str_time[:len(local_str_time)-3])
