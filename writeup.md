# Challenge Project Writeup

## Differences from Production

* Sensitive data should be pulled out of the settings.py file
  * Secret keys, databse login information, etc. should be obfuscated
* Static files should be served through the web server, not Django, for performance reasons
* URLs should not include database keys, for security reasons
* When updating / creating records via Ajax, HTML characters should be escaped to prevent XSS attacks

## Currency

Currencies could be implemented in-house but it looks like there are some well-made plugins available, like django-currencies, and open source projects like openexchangerates.org

## Date and Time

A few issues could arise with date and time, especially regarding the entry_date field on the TimeEntry model. For instance, if somebody in a time zone several hours ahead created a record, its entry_date could appear to be one day ahead of the current user's time zone.

It would probably make more sense to implement the entry_date as a DateTime field rather than a DateField. If it is supposed to behave like a timestamp, then time information would probably be useful to have. Also we could take advantage of pytz to track time zones with this field. This would allow us to track the exact point in time a TimeEntry was created, regardless of time zone.


## Object Mutability

Mutability of objects is a concern. Two different sessions could be editing the same object, and only the most recent changed would be saved. To fix this, there should be a system in place to either notify the user or update the form to the latest information using some kind of long-polling or websockets (e.g. Tornado).
