import argparse, requests

def banner():
	print(' _                    ')
	print('| \o._|_|   .__|_ _ ._')
	print('|_/|| | ||_|| ||_(/_|  coded by: lucasbazan \n')

banner()
parser = argparse.ArgumentParser(description = 'DirHunter - Hunt website directories')
parser.add_argument('-u', '--url', action = 'store', dest = 'url', required = True, help = 'Target URL (ex: http://testphp.vulnweb.com)')
parser.add_argument('-w', '--wordlist', action = 'store', dest = 'wordlist', required = True, help = 'Wordlist path to use for brute force')
arguments = parser.parse_args()

sc200 = []
file_wordlist = open(arguments.wordlist, 'r')
file_wordlist = file_wordlist.readlines()

def brute_force(url, wordlist):
	for line in file_wordlist:
		line = line.rstrip()
		domain = arguments.url + '/' + line
		url = requests.get((domain))
		if url.status_code == 200:
			sc200.append(domain)
			pass
		else:
			pass
	if len(sc200) != 0:
		print('Good Hunting xD')
		print('[✓] Available directories [✓]\n')
		for item in sc200:
			print(item)
		print('')
	else:
		print('Bad Hunting x/')
		print('[!] No directory is available [!]\n')

brute_force(arguments.url, arguments.wordlist)
