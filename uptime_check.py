import os
import sys

# Add path to the uptime_monitor.py file so we can import it.
sys.path.append('./')

import uptime_monitor

emails = ["thuan.nguyen@8bitrockr.com"]
websites = ['http://techblogsearch.com', 'http://puppy.vn', 'https://www.dataflowplus.org', 'http://www.everystay.com']
for website in websites:
	if not uptime_monitor.monitor_uptime(website, emails):
    	    pass
