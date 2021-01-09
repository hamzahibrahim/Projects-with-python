import time

the_hosts_file_path = r"C:\WINDOWS\System32\drivers\etc\hosts"
redirect = "127.0.0.1"


websites_to_block = ["instagram.com", "www.instagram.com",
                     "www.facebook.com", "facebook.com"]
try:
    with open(the_hosts_file_path,'r+') as fi:
        con = fi.readlines()
        fi.seek(0)
        for every_line in con:
            if not any(website in every_line for website in websites_to_block):
                fi.write(every_line)
                print('Printing the lines of the file without the websites ...')
        fi.truncate()

    print('done you are now unblocked!')
except:
    print('Something went wrong! are u sure you blocked the websites!!')

'''
If you lost anything here is whats in the hosts file 
------------

# Copyright (c) 1993-2006 Microsoft Corp.

#

# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.

#

# This file contains the mappings of IP addresses to host names. Each

# entry should be kept on an individual line. The IP address should

# be placed in the first column followed by the corresponding host name.

# The IP address and the host name should be separated by at least one

# space.

#

# Additionally, comments (such as these) may be inserted on individual

# lines or following the machine name denoted by a '#' symbol.

#

# For example:

#

# 102.54.94.97 rhino.acme.com # source server

# 38.25.63.10 x.acme.com # x client host

127.0.0.1 localhost

::1 localhost
'''