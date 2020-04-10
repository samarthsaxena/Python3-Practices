import requests
import lxml.html
import pprint

for version, url in [
    ('2.3', 'https://docs.python.org/2.3/lib/node130.html'),
    ('2.4', 'https://docs.python.org/2.4/lib/standard-encodings.html'),
    ('2.5', 'https://docs.python.org/2.5/lib/standard-encodings.html'),
    ('2.6', 'https://docs.python.org/2.6/library/codecs.html#standard-encodings'),
    ('2.7', 'https://docs.python.org/2.7/library/codecs.html#standard-encodings'),
    ('3.0', 'https://docs.python.org/3.0/library/codecs.html#standard-encodings'),
    ('3.1', 'https://docs.python.org/3.1/library/codecs.html#standard-encodings'),
    ('3.2', 'https://docs.python.org/3.2/library/codecs.html#standard-encodings'),
    ('3.3', 'https://docs.python.org/3.3/library/codecs.html#standard-encodings'),
    ('3.4', 'https://docs.python.org/3.4/library/codecs.html#standard-encodings'),
    ('3.5', 'https://docs.python.org/3.5/library/codecs.html#standard-encodings'),
    ('3.6', 'https://docs.python.org/3.6/library/codecs.html#standard-encodings'),
    ('3.7', 'https://docs.python.org/3.7/library/codecs.html#standard-encodings'),
    ('3.8', 'https://docs.python.org/3.8/library/codecs.html#standard-encodings')
]:
    html = requests.get(url).text
    doc = lxml.html.fromstring(html)
    standard_encodings_table = doc.xpath(
        '//table[preceding::h2[.//text()[contains(., "Standard Encodings")]]][//th/text()="Codec"]'
    )[0]
    codecs = standard_encodings_table.xpath('.//td[1]/text()')
    print("## Python %s (%i encodings)" % (version, len(codecs)))
    print('<pre><code>' + pprint.pformat(codecs) + '</code></pre>')