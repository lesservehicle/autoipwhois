#!/usr/bin/env python

from __future__ import print_function

import dns.reversename
n = dns.reversename.from_address("8.8.8.8")
print(n)
print(dns.reversename.to_address(n))