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


The intended output is supposed to be very basic so that the output can be piped into other linux programs such as grep,
while, or for loops etc...


Examples of use

List:

    Simple list of containers:
        hypercf -u username -k qwerty123456abcdefghij09876 -r ord ls

    expected output:
        test
        test2


    Long list of containers:
        hypercf -u username -k qwerty123456abcdefghij09876 -r ord ls -l

    expected output:
        Obj#: 1514       Size:   976.8MB  Name: test
        Obj#: 1000       Size:   723.2MB  Name: test2


    Simple list of objects in 'test' container:
        hypercf -u username -k qwerty123456abcdefghij09876 -r ord ls -c test

    expected output:
        /example/path/078_max.jpg
        /example/path/083_max.jpg
        /example/path/093_max.jpg
        /example/path/095_max.jpg
        /example/path/096_max.jpg
        /example/path/0IYXX.jpg
        /example/path/0JSAnbM.jpg


    Long list of object in 'test' container:
        hypercf -u username -k qwerty123456abcdefghij09876 -r ord ls -l

    expected output:
        Tue, 30 Jul 2013 00:01:03 GMT    425.3KB  /example/path/078_max.jpg
        Tue, 30 Jul 2013 00:01:04 GMT    165.9KB  /example/path/083_max.jpg
        Tue, 30 Jul 2013 00:01:06 GMT    140.5KB  /example/path/093_max.jpg
        Tue, 30 Jul 2013 00:01:07 GMT    456.1KB  /example/path/095_max.jpg
        Tue, 30 Jul 2013 00:01:08 GMT    118.8KB  /example/path/096_max.jpg
        Tue, 30 Jul 2013 00:01:17 GMT    231.3KB  /example/path/0IYXX.jpg
        Tue, 30 Jul 2013 00:01:19 GMT    702.5KB  /example/path/0JSAnbM.jpg


    Long list of containers with 'grep' (applies to container names):
        hypercf -u username -k qwerty123456abcdefghij09876 -r ord ls -l -g t2

    expected output:
        Obj#: 1000       Size:   723.2MB  Name: test2




Download:

    Download 'test' container to /home/user/mycontainer
        hypercf -u username -k qwerty123456abcdefghij09876 -r ord dn -c test -d /home/user/mycontainer

    expected dir/file creation:
        mycontainer-|
                    |-example-|
                              |-path
                                  |
                                078_max.jpg
                                083_max.jpg
                                093_max.jpg
                                095_max.jpg
                                096_max.jpg
                                0IYXX.jpg
                                0JSAnbM.jpg

    Note: the base directory, '/home/user/mycontainer' must already exist.




Upload:

    Using the example/path structure above with full path:
        hypercf -u username -k qwerty123456abcdefghij09876 -r ord up -c newcontainer -d /home/user/mycontainer

    expected container object output:
        home/user/mycontainer/example/path/078_max.jpg
        home/user/mycontainer/example/path/083_max.jpg
        home/user/mycontainer/example/path/093_max.jpg
        home/user/mycontainer/example/path/095_max.jpg
        home/user/mycontainer/example/path/096_max.jpg
        home/user/mycontainer/example/path/0IYXX.jpg
        home/user/mycontainer/example/path/0JSAnbM.jpg


    Using the example/path structure with relative path from /home/user/mycontainer:
        hypercf -u username -k qwerty123456abcdefghij09876 -r ord up -c newcontainer -d .

    expected container object output:
        example/path/078_max.jpg
        example/path/083_max.jpg
        example/path/093_max.jpg
        example/path/095_max.jpg
        example/path/096_max.jpg
        example/path/0IYXX.jpg
        example/path/0JSAnbM.jpg


    Note: The 'path' info of the object will always use the directory (-d) as the root of the path info.
    Note: The ../   ./   .  will be removed from the leading part of the object path. This allows the download to
          always be relative the the base path you use when downloading.





Delete:

    Delete the newcontainer and all the files:
        hypercf -u username -k qwerty123456abcdefghij09876 -r ord del -c newcontainer





Copy (container to container):

    Note: This feature has not yet been implemented.




Advanced usage:

    Download multiple containers to mycontainers dir:
        hypercf -u username -k qwerty123456abcdefghij09876 -r ord ls | while read cont;do hypercf -u username -k qwerty123456abcdefghij09876 -r ord dn -c $cont -d /home/user/mycontainer;done


