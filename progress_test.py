#!/usr/bin/env python

import time
import random
import sys
import collections
from multiprocessing import Process as Task, Queue

#from threading import Thread as Task
#from Queue import Queue

number = 50


def download(status, filename):
    count = random.randint(5, 30)
    for i in range(count):
        status.put([filename, (i+1.0)/count])
        time.sleep(1.1)


def print_progress(progress):
    global number
    progress_list = []
    for filename, percent in progress.items():
        bar = ('=' * int(percent * 20)).ljust(20)
        percent = int(percent * 100)
        xx = "%3s%% [%s] %s %s" % (percent, bar, filename, 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
#        if percent == 100:
#            continue
        progress_list.append(xx)
    sys.stdout.write('\r%s%s' % ('\x1b[A' * (int(len(progress_list)) - 1), '\n'.join(progress_list)))
    sys.stdout.flush()


def main():
    global number
    status = Queue()
    progress = collections.OrderedDict()
    workers = []
    sys.stderr.write("\x1b[2J\x1b[H")
    for filename in xrange(number):
        child = Task(target=download, args=(status, filename))
        child.start()
        workers.append(child)
        progress[filename] = 0.0
    while any(i.is_alive() for i in workers):
        time.sleep(1.0)
        sys.stderr.write("\x1b[2J\x1b[H")
        while not status.empty():
            filename, percent = status.get()
            progress[filename] = percent
            print_progress(progress)
    print '\nall downloads complete'

main()


#url = (<file location>)
#file_name = url.split('/')[-1]
#u = urllib2.urlopen(url)
#f = open(file_name, 'wb')
#meta = u.info()
#file_size = int(meta.getheaders("Content-Length")[0])
#print "Downloading: %s Bytes: %s" % (file_name, file_size)
#
#file_size_dl = 0
#block_sz = 8192
#while True:
#    buffer = u.read(block_sz)
#    if not buffer:
#        break
#
#    file_size_dl += len(buffer)
#    f.write(buffer)
#    status = r"%10d [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
#    status = status + chr(8)*(len(status)+1)
#    print status,
#
#f.close()