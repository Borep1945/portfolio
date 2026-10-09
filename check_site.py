from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET

class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.local = []
        self.anchors = []
        self.ids = set()
        self.headings = 0
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, f"Duplicate id {attrs['id']}"
            self.ids.add(attrs['id'])
        if tag == 'h1':
            self.headings += 1
        if tag == 'img':
            assert 'alt' in attrs, 'Image missing alt'
        for attribute in ['src','href']:
            value = attrs.get(attribute, '')
            if value.startswith('#') and value != '#':
                self.anchors.append(value[1:])
            elif value and value != '#' and not urlsplit(value).scheme:
                self.local.append(value)

root = Path(__file__).resolve().parent
p = References()
p.feed((root / 'index.html').read_text())
assert p.headings == 1, 'Expected one main heading'
for name in p.anchors:
    assert name in p.ids, f'Missing section {name}'
for name in p.local:
    assert (root / name).is_file(), f'Missing asset {name}'
for path in (root / 'assets').glob('*.svg'):
    ET.parse(path)
print(f'PASS: {len(p.local)} local references, {len(p.anchors)} section links, all SVGs valid')
