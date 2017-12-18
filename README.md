# pihole-alerts

## Overview

Simple monitoring app for the Pi-hole DNS server & ad-blocker. Specify "blacklist" domains, email configuration, and your Pi-hole auth token in `config.py`. Ideally, the scripts are called via cron once per 24 hours to search across the rolling query data; individual email alerts are generated if a domain was requested within the rolling time window.

Use cases could include stealth monitoring via email of domain requests on your network, or situations where automated alerts would be ideal.

### TBD
* Spec for RPM build
* Error handling, logging
* Improved email content and granularity
* Store auth passwords as non-plaintext
