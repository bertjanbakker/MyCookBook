#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (C) 2018, bertjanbakker
# License: GPL v 3

"""
SI metric prefix formatter

Formatter for numbers into a string with the
appropriate number and decimal prefix to denote
powers of 10 following the SI standard.

For example, the number 0.000001 (or 1e-06) formatted using
pretty(0.000001) yields "1 µ" meaning 1 micro and providing
an optional unit, pretty(423900, 'g') yields "423.900 kg".

See also
- https://en.wikipedia.org/wiki/Metric_prefix

"""

import math, decimal
from decimal import Decimal as D
import sys

decimal.getcontext().prec = 6

si_prefixes =	[ ( D('1e-24'), 'yocto', "y" ),
		  ( D('1e-21'), 'zepto', "z" ),
		  ( D('1e-18'), 'atto' , "a" ),
		  ( D('1e-15'), 'femto', "f" ),
		  ( D('1e-12'), 'pico' , "p" ),
		  ( D('1e-09'), 'nano' , "n" ),
#		  ( D('1e-06'), 'micro', u"\xb5"),
		  ( D('1e-06'), 'micro', "µ" ),
		  ( D('1e-03'), 'milli', "m" ),
		  ( D('1e0')  , ''     , ""  ),
		  ( D('1e03') , 'kilo' , "k" ),
		  ( D('1e06') , 'mega' , "M" ),
		  ( D('1e09') , 'giga' , "G" ),
		  ( D('1e12') , 'tera' , "T" ),
		  ( D('1e15') , 'peta' , "P" ),
		  ( D('1e18') , 'exa'  , "E" ),
		  ( D('1e21') , 'zetta', "Z" ),
		  ( D('1e24') , 'yotta', "Y" ) ]

def exp_for(x):
	return 0 if x==0 else int(math.log10(abs(x)))

def power_for(x):
	pri = exp_for(x)//3
	return si_prefixes[pri + 8][0]

def metric_prefix_name_for(x):
	pri = exp_for(x)//3
	return si_prefixes[pri + 8][1]

def metric_prefix_for(x):
	pri = exp_for(x)//3
	return si_prefixes[pri + 8][2]

def pretty(x, unit=''):
        #if type(x) is str:
        #    x = float(x)
        pr = metric_prefix_for(x)
        m = decimal.Decimal(str(float(x)))/power_for(x)
        return ("%s %s%s" % (m, pr, unit))

if __name__ == '__main__':
    for x in (3.62e-08, 0.000001, 0.001, 0.1, 0, 1, 42, 678, 1024.5, 423900, 234958234):
        print("{} -> {}".format(-x, pretty(-x)))
        print("{} -> {}".format(x, pretty(x, 'b')))

