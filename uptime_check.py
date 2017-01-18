import os
import sys

# Add path to the uptime_monitor.py file so we can import it.
sys.path.append('./')

import uptime_monitor

emails = ["your-email@domain.com"]
websites = ['http://techblogsearch.com', 'http://abc.com']
for website in websites:
	if not uptime_monitor.monitor_uptime(website, emails):
    	    pass
