# etl dense data

Extact, transform, load data steps.

0. Run browsertime according to [Andrew Creskey's browsertime scripts](https://github.com/acreskeyMoz/browsertime_scripts).

1. From the browsertime results folder, separate into
   browser/site-1.json
   browser/site-2.json
   ...
   browser/site-n.json

   Use the script [copy-json-files-to-one-dir-2024.sh](https://github.com/bdekoz/mozilla-perf-analysis-x/blob/main/scripts/copy-json-files-to-one-dir-2024.sh)

   Depending on the browsers and configurations tested, there may be a
different number of files in each browser-specific directory. For
example, the fenix_nightly directory may have 9447 files, and the
chrome_125 directory may have 9547.

2. From consolidated results json folder above, generate individual files csv.
Use $MOZPERFBTS/transform-dir-with-1-metric-cosmology-to-csv.sh

3. Take individual directory of csv files, and make a consolidated csv
file that is ordered exactly as the sitelist used for the survey. If
there are no results for a given origin/URL, then that space is empty.
Use $MOZPERFAX/bin/moz-perf-x-transform.exe.

4. Generate sitelists for web content setasides.

5. CSV to python.
6. CSV to influx.
