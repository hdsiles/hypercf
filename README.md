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
argparse
os
json
multiprocessing
requests
time
sys


The intended output is supposed to be very basic so that the output can be piped into other linux programs such as grep,
while, or for loops etc...



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


    Long list of containers with numbering:
        hypercf -u username -k qwerty123456abcdefghij09876 -r ord ls -l -n

    expected output:
        1  Obj#: 1514       Size:   976.8MB  Name: test
        2  Obj#: 1000       Size:   723.2MB  Name: test2


    Simple list of objects in 'test' container:
        hypercf -u username -k qwerty123456abcdefghij09876 -r ord ls -c test

    expected output:
        example/path/078_max.jpg
        example/path/083_max.jpg
        example/path/093_max.jpg
        example/path/095_max.jpg
        example/path/096_max.jpg
        example/path/0IYXX.jpg
        example/path/0JSAnbM.jpg


    Long list of objects in 'test' container with numbering:
        hypercf -u username -k qwerty123456abcdefghij09876 -r ord ls -l -n

    expected output:
        1  Tue, 30 Jul 2013 00:01:03 GMT    425.3KB  /example/path/078_max.jpg
        2  Tue, 30 Jul 2013 00:01:04 GMT    165.9KB  /example/path/083_max.jpg
        3  Tue, 30 Jul 2013 00:01:06 GMT    140.5KB  /example/path/093_max.jpg
        4  Tue, 30 Jul 2013 00:01:07 GMT    456.1KB  /example/path/095_max.jpg
        5  Tue, 30 Jul 2013 00:01:08 GMT    118.8KB  /example/path/096_max.jpg
        6  Tue, 30 Jul 2013 00:01:17 GMT    231.3KB  /example/path/0IYXX.jpg
        7  Tue, 30 Jul 2013 00:01:19 GMT    702.5KB  /example/path/0JSAnbM.jpg


    Long list of containers with 'grep' (applies to container names only):
        hypercf -u username -k qwerty123456abcdefghij09876 -r ord ls -l -g t2

    expected output:
        Obj#: 1000       Size:   723.2MB  Name: test2



Download:

    Download 'test' container to /home/user/mycontainer
        hypercf -u username -k qwerty123456abcdefghij09876 -r ord dn -c test -d /home/user/mycontainer/

    Given object structure is like:
        test/example/path/078_max.jpg

    expected dir/file creation:
        mycontainer-|
                    |-test-|
                           |-example-|
                                     |-path-|
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

    Using the example/path structure above with full path (No trailing slash at the end):
        hypercf -u username -k qwerty123456abcdefghij09876 -r ord up -c newcontainer -d /home/user/container_dir

    expected object output inside the 'newcontainer' container:
        container_dir/example/path/078_max.jpg
        container_dir/example/path/083_max.jpg
        container_dir/example/path/093_max.jpg
        container_dir/example/path/095_max.jpg
        container_dir/example/path/096_max.jpg
        container_dir/example/path/0IYXX.jpg
        container_dir/example/path/0JSAnbM.jpg


    Using the example/path structure above with full path (with a trailing slash):
        hypercf -u username -k qwerty123456abcdefghij09876 -r ord up -c newcontainer -d /home/user/container_dir/

    expected object output inside the 'newcontainer' container:
        example/path/078_max.jpg
        example/path/083_max.jpg
        example/path/093_max.jpg
        example/path/095_max.jpg
        example/path/096_max.jpg
        example/path/0IYXX.jpg
        example/path/0JSAnbM.jpg



    Using the relative paths also works. (assuming already inside /home/user/container_dir directory):
        hypercf -u username -k qwerty123456abcdefghij09876 -r ord up -c newcontainer -d .

    expected container object output:
        example/path/078_max.jpg
        example/path/083_max.jpg
        example/path/093_max.jpg
        example/path/095_max.jpg
        example/path/096_max.jpg
        example/path/0IYXX.jpg
        example/path/0JSAnbM.jpg


Delete:

    Delete the newcontainer and all the files:
        hypercf -u username -k qwerty123456abcdefghij09876 -r ord del -c newcontainer


Copy (container to container):

    Copy entire container:
        hypercf -u username -k qwerty123456abcdefghij09876 -r ord cp -o: "source-container:my/path/obj.jpg = destination-container:my/new/path/newobj.jpg"

    Copy per object:
        hypercf -u username -k qwerty123456abcdefghij09876 -r ord cp -o "source-container:my/path/obj.jpg = destination-container:my/new/path/newobj.jpg"






Advanced usage (example below still works, but you can now append more than one source be it containers, or directories):

    Download multiple containers to mycontainers dir (this one will d/l them all):
        hypercf -u username -k qwerty123456abcdefghij09876 -r ord ls | while read cont;do hypercf -u username -k qwerty123456abcdefghij09876 -r ord dn -c $cont -d /home/user/mycontainer;done



