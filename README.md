# autoipwhois

Autoipwhois is a script that outputs the results of an RDAP query against a single IPv4 address or a list of IPv4 addresses. 

## Installation

Autoipwhois was built on Ubuntu 18.04, but should work in any Python 3 environment.

Create a virtual environment to satisfy the requirements, and activate it.
```
mkdir ~/virtualenvs/
python3 -m virtualenv ~/virtualenvs/autoipwhois
. ~/virtualenvs/autoipwhois/bin/activate
```

Clone the repository.
```
mkdir ~/repos
cd ~/repos
git clone https://github.com/lesservehicle/autoipwhois.git
```

Install the requirements for the script.
```
cd ~/repos/autoipwhois
pip install -r requirements.txt
```


## Usage

Autoipwhois accepts a single IP address or a list of IP addresses in a plain text file, one address on each line. The output can either be printed to STDOUT or to a tab-delimited file, which can be imported into everyone's favorite cybersecurity tool Microsoft Excel.

To get usage information, run it with the -h flag

```
(autoipwhois) adam@ubuntu:~/repos/autoipwhois$ python3 autoipwhois -h

usage: autoipwhois.py [-h] [-a ADDRESS] [-f FILENAME] [-t TSVOUTFILE]

optional arguments:
  -h, --help     show this help message and exit
  -a ADDRESS     An IPv4 address to query.
  -f FILENAME    A list of IPv4 addresses, one per line.
  -t TSVOUTFILE  Outputs results to a specified TSV file.
```

Return a result for a single IP address and output to STDOUT:
```
python autoipwhois -a 8.8.8.8
```

Return results for a list of IP addresses and output to STDOUT:
```
python autoipwhois -l list.txt
```

Return results for a list of IPv4 addresses and output to a TSV file:
```
$ python autoipwhois.py -f list.txt -t output.tsv
```

## Full Example With Installation and Usage

```
adam@ubuntu:~$ mkdir ~/virtualenvs

adam@ubuntu:~$ python3 -m virtualenv ~/virtualenvs/autoipwhois
Using base prefix '/usr'
New python executable in /home/adam/virtualenvs/autoipwhois/bin/python3
Also creating executable in /home/adam/virtualenvs/autoipwhois/bin/python
Installing setuptools, pip, wheel...
done.

adam@ubuntu:~$ . ~/virtualenvs/autoipwhois/bin/activate
(autoipwhois) adam@ubuntu:~$ mkdir ~/repos
(autoipwhois) adam@ubuntu:~$ cd ~/repos
(autoipwhois) adam@ubuntu:~/repos$ git clone https://github.com/lesservehicle/autoipwhois.git
Cloning into 'autoipwhois'...
remote: Enumerating objects: 19, done.
remote: Counting objects: 100% (19/19), done.
remote: Compressing objects: 100% (11/11), done.
remote: Total 19 (delta 7), reused 15 (delta 5), pack-reused 0
Unpacking objects: 100% (19/19), done.

(autoipwhois) adam@ubuntu:~/repos$ cd autoipwhois/

(autoipwhois) adam@ubuntu:~/repos/autoipwhois$ pip install -r requirements.txt
Collecting dnspython
  Using cached dnspython-1.16.0-py2.py3-none-any.whl (188 kB)
Collecting ipwhois
  Using cached ipwhois-1.1.0-py2.py3-none-any.whl (74 kB)
Collecting tqdm
  Using cached tqdm-4.42.0-py2.py3-none-any.whl (59 kB)
Installing collected packages: dnspython, ipwhois, tqdm
Successfully installed dnspython-1.16.0 ipwhois-1.1.0 tqdm-4.42.0

(autoipwhois) adam@ubuntu:~/repos/autoipwhois$ python autoipwhois -a 8.8.8.8
8.8.8.8	8.8.8.0/24	GOOGLE, US	dns.google.

(autoipwhois) adam@ubuntu:~/repos/autoipwhois$ echo "8.8.8.8" >> list.txt

(autoipwhois) adam@ubuntu:~/repos/autoipwhois$ echo "1.2.3.4" >> list.txt

(autoipwhois) adam@ubuntu:~/repos/autoipwhois$ python autoipwhois -l list.txt
8.8.8.8	8.8.8.0/24	GOOGLE, US	dns.google.
1.2.3.4	NA	NA	4.3.2.1.in-addr.arpa

(autoipwhois) adam@ubuntu:~/repos/autoipwhois$ python autoipwhois.py -f list.txt -t output.tsv
Writing output to output.tsv.

(autoipwhois) adam@ubuntu:~/repos/autoipwhois$ cat output.tsv 
8.8.8.8	8.8.8.0/24	GOOGLE, US	dns.google.
1.2.3.4	NA	NA	4.3.2.1.in-addr.arpa
```
