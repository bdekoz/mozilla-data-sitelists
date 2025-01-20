#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
"""

# prompt: for each json file in directory D, run function "dothis"

import json
import os
import sys

# Web Content string fragments
# <link rel="preconnect" or <link rel=preconnect
# <link rel="dns-prefetch"
# https://developer.mozilla.org/en-US/docs/Web/Performance/Speculative_loading
# https://developer.mozilla.org/en-US/docs/Web/Performance/dns-prefetch
# https://fetch.spec.whatwg.org/#concept-request-destination
mb_dnsprefetch = [ 'rel="dns-prefetch"', 'rel=dns-prefetch' ]
mb_preconnect = [ 'rel=preconnect', 'rel="preconnect"' ]
mb_preload = [ 'rel="preload"', 'rel=preload' ]
mb_prefetch = [ 'rel="prefetch"', 'rel=prefetch' ]
mb_prerender = [ 'rel="prerender"', 'rel=prerender' ]

# https://datatracker.ietf.org/doc/draft-ietf-httpbis-compression-dictionary/
mb_compressiondict = [ 'rel="compression-dictionary"', 'rel=compression-dictionary' ]
mh_compressiondict = [ 'Use-As-Dictionary', 'Available-Dictionary', 'Dictionary-ID' ]

def classify(file, tag, matchdict, field):
  """
  This is a placeholder function. Replace this with your actual logic.
  """
  try:
    with open(file, 'r') as f:

      # Process the JSON data here
      #print(f"file: {file}")

      data = json.load(f)
      data_url = data['url']
      #data_text = data['text']
      data_field = data[field]            
      
      #print(data.keys())

      # data = {
      #  'url': r.request.url,
      #  'text': r.text,
      #  'headers': dict(r.headers),
      #  'status_code': r.status_code,
      #  'datetime': datetime.datetime.now().isoformat(),
      #}

      matchp = False
      for item in matchdict:
        if item in data_field:
          matchp = True
        #print(f"item: {item}")
        #print(f"txt: {data_text}")        

      if matchp:
        with open("response_" + field + "_matches_" + tag + ".txt", "a") as ofile:
          ofile.write(data_url + '\n')

  except json.JSONDecodeError as e:
      print(f"Error decoding JSON in {file}: {e}")
  except Exception as e:
    print(f"Error processing {file}: {e}")

def process_json_files(directory, tag, matchdict, field):
  origincount=1
  for filename in os.listdir(directory):
    if filename.endswith(".json"):
      filepath = os.path.join(directory, filename)
      classify(filepath, tag, matchdict, field)
      origincount += 1
  print("sites total: " + str(origincount))

# Usage:
# origin_content_classifer.py ./rank-10-responses
idir = sys.argv[1];

process_json_files(idir, "dns-prefetch", mb_dnsprefetch, "text")
process_json_files(idir, "preconnect", mb_preconnect, "text")
process_json_files(idir, "preload", mb_preload, "text")
process_json_files(idir, "prefetch", mb_prefetch, "text")
process_json_files(idir, "prerender", mb_prerender, "text")

process_json_files(idir, "compression-dictionary", mb_compressiondict, "text")
process_json_files(idir, "compression-dictionary", mh_compressiondict, "headers")
