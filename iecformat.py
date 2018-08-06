#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (C) 2018, bertjanbakker
# License: GPL v 3

import math, decimal
from decimal import Decimal as D
import sys

decimal.getcontext().prec = 6

iec_prefixes =  [ ( D(1024**0), ''     , ""  ),
                  ( D(1024**1), 'kibi' , "ki"),
                  ( D(1024**2), 'mebi' , "Mi"),
                  ( D(1024**3), 'gibi' , "Gi"),
                  ( D(1024**4), 'tebi' , "Ti"),
                  ( D(1024**5), 'pebi' , "Pi"),
                  ( D(1024**6), 'exbi' , "Ei"),
                  ( D(1024**7), 'zebi' , "Zi"),
                  ( D(1024**8), 'yobi' , "Yi") ]

iec_log_factor = math.log(1024**(1/3))

def exp_for(x):
        return 0 if abs(x)<1 else int(math.log(abs(x))/iec_log_factor)

def power_for(x):
        pri = exp_for(x)//3
        return iec_prefixes[pri][0]

def prefix_name_for(x):
	pri = exp_for(x)//3
	return iec_prefixes[pri][1]

def prefix_for(x):
        pri = exp_for(x)//3
        return iec_prefixes[pri ][2]

def pretty(x, unit='B'):
        pr = prefix_for(x)
        m = decimal.Decimal(str(float(x)))/power_for(x)
        return ("%s %s%s" % (m, pr, unit))

if __name__ == '__main__':
    for x in (0.1, 1, 10, 1000, 1024, 2048, 234958234, 1024**2, 1024**4):
        print("{} -> {}".format(x, pretty(x)))
