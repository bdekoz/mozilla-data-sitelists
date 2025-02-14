# sitelist generation

How to go from the CrUX site to a sorted list that will serve as input
for large-site surveys with browsertime.

1. Go to the CruX BigQuery [site](https://console.cloud.google.com/bigquery?p=chrome-ux-report&;d=all&;page=dataset&authuser=0&project=crux-2024&pli=1). Select CrUX segment: date, type of
computer, determine how large the site should be, and how many sites
you want back. You'll get a json file back.

2. Extract just the sitelist from the CrUX json files with jq. See script
[convert-crux-json-to-site-list.sh](https://github.com/bdekoz/mozilla-perf-browsertime-tools/blob/master/scripts/convert-crux-json-to-site-list.sh)

3. Sort this list (uniq|sort on linux), and check it in. This is the starting list, which will now be refined as per the survey.

4. Classify web content for subsets.

5. First pass is a quick run through as much of the subset as is possible with one itteration, get rough data on LCP elementt match, see which sites can be VisuallyComplete at 10 sec, etc. Pick matching LCP elmeents (across phone/tablet, phone/desktop, chrome/firefox). Pick quick completing, do a managable subset of 40, 100.

6. Strip NSFW

7. Second pass is higher iteration, looking for low variation on target metrics, try for 10 good sites in each web content category.