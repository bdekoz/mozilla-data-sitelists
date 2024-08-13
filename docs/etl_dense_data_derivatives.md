# etl dense data

Extact, transform, load data steps.


0. Run browsertime according to [Andrew Creskey's browsertime scripts](https://github.com/acreskeyMoz/browsertime_scripts).


1. Consolidate the browsertime results folder into un-nested browser-specific directories with just data files. Separate into

   browser/site-1.json  
   browser/site-1.har  
   browser/site-2.json  
   browser/site-2.har  
   ...  
   browser/site-n.json  
   browser/site-n.har  

   Use the script [copy-json-files-to-one-dir-2024.sh](https://github.com/bdekoz/mozilla-perf-analysis-x/blob/main/scripts/copy-json-files-to-one-dir-2024.sh)

   Like so:

   copy-json-files-to-one-dir-2024.sh  browsertime-results
   
   Depending on the browsers and configurations tested, there may be a
different number of files in each browser-specific directory. For
example, the fenix_nightly directory may have 9447 files, and the
chrome_125 directory may have 9547. Don't be alarmed if this happens.


2. From consolidated results json folder above, generate individual csv files.
   Use $MOZPERFBTS/transform-dir-with-1-metric-cosmology-to-csv.sh

   This script uses a binary that reads a result browsertime json file
   and extracts LCP and metric information (from moz-perf-x-extract.cc,
   the function extract_browsertime_lcp). Like so:

   moz-perf-x-extract-lcp.exe site1.json sitelist

   Sample script invocation:
   transform-dir-with-1-metric-cosmology-to-csv.sh ./json.fenix_nightly ../../../../sitelists/CrUX.2024-04/rank-10M-phone-10k-sites.pass.txt


3. Take individual directory of csv files, and make a consolidated csv
file that is ordered exactly as the sitelist used for the survey. If
there are no results for a given origin/URL, then that space is empty.
Use $MOZPERFAX/bin/moz-perf-x-transform.exe (from
moz-perf-x-transform.cc), like so:

   moz-perf-x-transform.exe ./csv.fenix_nightly/ ../../../../sitelists/CrUX.2024-04/rank-10M-phone-10k-sites.pass.txt


4. Consistency check the consolidated csv file.
Make sure same number of delimiters on each file, no special characters, etc.
(from moz-perf-x-transform.cc)
moz-perf-x-csv-delim-consistent.exe ./chrome_125-consolidated.lcp.csv


5. Label fields of csv files
Add the following label as the first line to the consolidated csv file, so that it's easier to manipulate in python/pandas. This is the column index.

   url_id|url|power|fetchStart|connectStart|responseStart|SpeedIndex|VC85|fcp|lcp_load|lcp_render|lcp_element


6. Generate sitelists for web content setasides.

7. CSV to python.
8. CSV to influx.
