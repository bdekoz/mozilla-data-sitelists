#!/usr/bin/env python

import sys
from origin_content_classifier import classify_web_content_traits

iurl = sys.argv[1];
tdict = classify_web_content_traits(iurl)
print(tdict)
