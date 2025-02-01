#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
"""

# prompt: for each json file in directory D, run function "dothis"

import json
import os
import requests
#import sys

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

# google publisher tag
# https://developers.google.com/publisher-tag
mb_gpt = [ 'gpt.js' ]

# https://datatracker.ietf.org/doc/draft-ietf-httpbis-compression-dictionary/
mb_compressiondict = [ 'rel="compression-dictionary"', 'rel=compression-dictionary' ]
mh_compressiondict = [ 'Use-As-Dictionary', 'Available-Dictionary', 'Dictionary-ID' ]

def classify_origin(rfielddict, matchdict):
  matchp = 0
  for item in matchdict:
    if item in rfielddict:
      matchp = 1
  return matchp


# Take a single input url and return dictionary of classifier types.
def classify_origin_field(r, matchdict, field):
  if field == "headers":
    sfield = dict(r.headers);
  if field == "text":
    sfield = r.text;
  matchp = classify_origin(sfield, matchdict)
  return matchp


# Take a single serialize response json file and append to match sitelist file.
def classify_sitelist(file, tag, matchdict, field):
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


# Assumes input directory is the base directory of a sitelist scan that serialized responses.
# aka, results from run of origin_reachable_and_response.py
def classify_json_files(directory, tag, matchdict, field):
  origincount=0
  for filename in os.listdir(directory):
    if filename.endswith(".json"):
      filepath = os.path.join(directory, filename)
      classify_sitelist(filepath, tag, matchdict, field)
      origincount += 1
  print("sites total: " + str(origincount))


# Make sitelists for each of following.
def classify_web_content_sitelists(idir):
  classify_json_files(idir, "dns-prefetch", mb_dnsprefetch, "text")
  classify_json_files(idir, "preconnect", mb_preconnect, "text")
  classify_json_files(idir, "preload", mb_preload, "text")
  classify_json_files(idir, "prefetch", mb_prefetch, "text")
  classify_json_files(idir, "prerender", mb_prerender, "text")
  classify_json_files(idir, "compression-dictionary", mb_compressiondict, "text")
  classify_json_files(idir, "compression-dictionary", mh_compressiondict, "headers")
  classify_json_files(idir, "google-publisher-tag", mb_gpt, "text")


# Make sitelist for no matches.
def classify_web_content_zero(idir):
  origincount=0
  for filename in os.listdir(idir):
    if filename.endswith(".json"):
      filepath = os.path.join(idir, filename)
      try:
        with open(filepath, 'r') as f:
          data = json.load(f)

          data_text = data["text"];
          m1p = classify_origin(data_text, mb_dnsprefetch)
          m2p = classify_origin(data_text, mb_preconnect)
          m3p = classify_origin(data_text, mb_preload)
          m4p = classify_origin(data_text, mb_prefetch)
          m5p = classify_origin(data_text, mb_prerender)
          m6p = classify_origin(data_text, mb_gpt)
          m7p = classify_origin(data_text, mb_compressiondict)

          data_headers = data["headers"];          
          m8p = classify_origin(data_headers, mh_compressiondict)
          if not (m1p or m2p or m3p or m4p or m5p or m6p or m7p or m8p):
            with open("response_" + "all" + "_matches_" + "zero" + ".txt", "a") as ofile:
              ofile.write(data["url"] + '\n')
      finally:
        origincount += 1
  print("sites total: " + str(origincount))

def classify_web_content_traits(url):
  tdict = { }
  r = requests.get(url, timeout=10)

  compressiondictp = 0
  ztp = classify_origin_field(r, mb_compressiondict, "text")
  zhp = classify_origin_field(r, mh_compressiondict, "headers")
  if ztp or zhp:
    compressiondictp = 1
  tdict["compression-dictionary"] = compressiondictp;

  tdict["dns-prefetch"] = classify_origin_field(r, mb_dnsprefetch, "text")
  tdict["google-publisher-tag"] = classify_origin_field(r, mb_gpt, "text")
  tdict["preconnect"] = classify_origin_field(r, mb_preconnect, "text")
  tdict["prefetch"] = classify_origin_field(r, mb_prefetch, "text")
  tdict["preload"] = classify_origin_field(r, mb_preload, "text")
  tdict["prerender"] = classify_origin_field(r, mb_prerender, "text")

  return tdict
