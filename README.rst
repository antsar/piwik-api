Python 3 client library for the `Piwik Reporting
API <https://developer.piwik.org/api-reference/reporting-api>`__.

The `Piwik Tracking
API <https://developer.piwik.org/api-reference/tracking-api>`__ is not
supported.

Example Usage
=============

::

    from piwik_api import PiwikAPI

    p = PiwikAPI(url='https://piwik.example.com',
                 token='e9f31a88fce426cd27aa4734ace348b8')

    # Get list of sites with activity today
    sites = p.MultiSites.getAll(period='day', date='today')

    # Get stats for all pages, filtered by date range
    from datetime import date
    pages = p.Actions.getPageURLs(idSite=1, period='range', date=date(2017, 6, 1),
                                  end_date=date(2017, 6, 15))
