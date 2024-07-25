# sitelist generation

How to go from the CrUX site to a sorted list that will serve as input
for large-site surveys with browsertime.

1. Go to the CruX BigQuery site. Select CrUX segment: date, type of
computer, determine how large the site should be, and how many sites
you want back. You'll get a json file back.

2. Extract just the sitelist from the CrUX json files with jq. See script
[convert-crux-json-to-site-list.sh](https://github.com/bdekoz/mozilla-perf-browsertime-tools/blob/master/scripts/convert-crux-json-to-site-list.sh)

3. Sort this list (uniq|sort on linux), and check it in. This is the starting list, which will now be refined as per the survey.