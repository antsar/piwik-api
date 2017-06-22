# Piwik-Reporting

A Python 3 client for the Piwik Reporting API.

Very few API calls are currently implemented; but contributions are welcome.
Piwik Tracking API is not supported, as other libraries exist for that.

# Example Usage

```
from piwik_reporting import PiwikReportingAPI

p = PiwikReportingAPI(url='https://piwik.example.com',
                      token='e9f31a88fce426cd27aa4734ace348b8')

# Get list of sites with activity today
sites = p.multisites.getAll(period='day', date='today')

# Get stats for all pages, filtered by date range
from datetime import date
pages = p.actions.getPageURLs(site_id=1, period='range', date=date(2017, 6, 1),
                              end_date=date(2017, 6, 15))
```

# Setup for Development

* `pip install -e .`
