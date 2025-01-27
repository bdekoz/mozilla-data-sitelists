#!/usr/bin/env python

import sys
from origin_content_classifier import classify_web_content

idir = sys.argv[1];
classify_web_content(idir)
