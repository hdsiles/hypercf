hypercf
=======

A Rackspace Cloud Files MultiProcess copy script.

The initial goal of this script is to speed up Cloud Files uploads and download by running concurrent transfers in batches. 

I recommend using Ubuntu 12.04 or higher as it has python 2.7 by default and should only need the requests module installed.
Install the requests module by doing the following:
 pip install requests
       or
 easy_install requests

The following modules are imported:
argparse,
os,
json,
urllib,
urllib2,
multiprocessing,
signal,
sys,
time,
request
