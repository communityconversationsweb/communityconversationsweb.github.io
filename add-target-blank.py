#!/usr/bin/python3

"""
This Python script was written by Kevin Massey on 10 Sep 2020 to ensure that
all of the <a href> elements contain:
    target="_blank"
so that clicking on them cause the page to open in a new tab.
"""

import re

P = re.compile('(.*<li>\s*<a href="http[^>]+)>(.*)')

lines = []
with open('cctablefinal.html') as f:
    for l in f.readlines():
        l = l.strip('\n')
        if 'href=" ' in l:
            l = l.replace('href=" ', 'href="')
        if 'targt="_blank"' in l:
            l = l.replace('targt=', 'target=')
        elif 'target="_blank"' not in l:
            m = P.match(l)
            if m:
                l = m.group(1) + ' target="_blank">' + m.group(2)
        lines.append(l)
print('\n'.join(lines))

