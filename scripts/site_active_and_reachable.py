#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Jk73Ng9tssSQ4hYxxL2oXiWVtBb9PZsQ
"""

#@title setup, static and constant data
import numpy as np
import pandas as pd
import urllib.request
import requests

# useful constants
tab = "\t";
newline = "\n";

# sitelist data locations
data_prefix = 'https://raw.githubusercontent.com/bdekoz/mozilla-data-lcp/main/';
sitebase = 'sitelists/CrUX.2024-04/';
sitelist = 'rank-10M-phone-10k-sites';
sitefile = data_prefix + sitebase + sitelist + ".txt";

# sitelist currently reachable
errfile = sitelist + ".fail.txt";
okfile = sitelist + ".pass.txt";


#@title origin_check_readable(origin, log)
# check origin to see if it can be read within a timeout
def origin_check_readable(origin, logfile):
  try:
    r = requests.get(origin, timeout=10);
  except:
    logfile.write(origin + newline);
    raise;


#@title check sitelist, write to unbuffered log files
with urllib.request.urlopen(sitefile) as response:
  print("found: " + sitefile);
  errlog = open(errfile, "w", 1);
  passlog = open(okfile, "w", 1);
  print(errfile);
  print(okfile);
  for line in response.readlines():
    origin = line.decode("ascii").strip(newline); # utf-8, ascii
    print(origin)
    try:
      origin_check_readable(origin, errlog);
      passlog.write(origin + newline);
    except:
      continue;
  errlog.close();
  passlog.close();