import re

p = re.compile('ca.e')

m = p.match('cakecare')

if m:
    print(m.group())
else:
    print(m.group())
