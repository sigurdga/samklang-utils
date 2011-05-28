# encoding: utf-8

from BeautifulSoup import BeautifulSoup
from markdown import markdown as original_markdown
from unidecode import unidecode

import re

def markdown(content, *args, **kwargs):
    """
    Converts markdown and makes it safe html with Beautiful Soup.
    """

    marked = original_markdown(content, ['def_list', 'codehilite'], *args, **kwargs)
    return unicode(BeautifulSoup(marked, fromEncoding="utf-8"))

def slugify(value):
    """
    Normalizes a string using unidecode library. Lowercase it, remove
    punctuation and replace spacing with hyphens.

    >>> slugify(u'Blåbærsyltetøy')
    'Blabaersyltetoy'
    """
    value = unidecode(value)
    value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
    return re.sub('[-\s]+', '-', value)



