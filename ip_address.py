# Python code for retrieving ip address

""" from urllib.request import urlopen
import re as r

def getIP():
	d = str(urlopen('http://checkip.dyndns.com/')
			.read())

	return r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)

print(getIP())
 """

from urllib.request import urlopen
import re as r

d = str(urlopen('http://checkip.dyndns.com/').read())
my_ipadd=r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)

print(my_ipadd)