#workflow


Sitelist building is via queries into CrUX for a given date. This data
can be exported in a variety of formats with a variable number of
entries. This is the raw sitelist.

Some sites on this list, culled from Google servers all over the
world, will be down or unreachable from network and time you are
trying to reach them. So, in order to remove long timeouts from the
test process, the sitelist must be refined before used.


1. Take note of the test computer, the test network, and the prevaling
network conditions. These are lumped into a set of characteristics
called "the experimental network topology." So, for instance, refining
and surveying on google collab-hosted scripts will not connect to Iran
(.ir) TLDs).

2. Refine the raw list by either/or:
a. only the URLS where ETLD+1 can be pinged from the terminal
b. only the URLs where python's urllib requests do not error


3. Survey sites
The refined list is then used to run performance tests using the
browsertime framework, surveying web performance with headless
browsers collecting data, being careful to run the tests on the same
network/setup that was used to refine the list. The survey must
include video for firefox and chrome so that the page loads can be
compared by others who are not on the setup/test network topology. Be
warned that running large sitelists with multiple iterations and a
matrix of different browsers can take up a lot of time (days/bleeding
into weeks) and monopolize machines.

The outputs of this survey are:

- sitelists and refined sitelists checked in to a github repo

- sitelist metadata in the form of CSV setasides where each site is
  queried to see if the web content contains advanced HTML or
  javascript characteristics, and if so a boolean true is put in the
  setaside, if not false is recorded.

- test results and videos stored as compressed data files on google
drive, organized by test date and sitelist used.

- dense data derivities built (via ETL) on this data set that extract given
metrics to either influx db entries of csv files, suitable for import
into python/Pandas data frame.


4. Analyze Survey

Load csv files into pandas in Google Collab. Results can be
partitioned via the setasides to focus on particular optimizations.
