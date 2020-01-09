import argparse, requests, os

# banner design
def banner():
	print(' _                    ')
	print('| \o._|_|   .__|_ _ ._')
	print('|_/|| | ||_|| ||_(/_|  coded by: lucasbazan \n')

banner()

# arguments
parser = argparse.ArgumentParser(description = 'DirHunter - Hunt website directories')
parser.add_argument('-u', '--url', action = 'store', dest = 'url', required = True, help = 'Target URL (ex: http://testphp.vulnweb.com)')
parser.add_argument('-w', '--wordlist', action = 'store', dest = 'wordlist', required = True, help = 'Wordlist path to use for brute force')
arguments = parser.parse_args()

sc200 = [] # list of status code 200
file_wordlist = open(arguments.wordlist, 'r') # open wordlist
file_wordlist = file_wordlist.readlines() # read lines of wordlist

def brute_force(url, wordlist):
	i = 0 # accountant
	for line in file_wordlist:
		i += 1
		line = line.rstrip()
		domain = arguments.url + '/' + line
		url = requests.get((domain))
		if url.status_code == 200:
			sc200.append(domain) # add domain to list
			print('[{}]'.format(i), domain, '[+]')
			pass
		else:
			print('[{}]'.format(i), domain, '[-]')
			pass
	if len(sc200) != 0:
		os.system('cls' if os.name == 'nt' else 'clear') # clean the screen
		banner()
		print('Good Hunting xD')
		print('[✓] Available directories [✓]\n')
		for item in sc200:
			print(item) # print available directories
		print('')
	else:
		os.system('cls' if os.name == 'nt' else 'clear')
		banner()
		print('Bad Hunting x/')
		print('[!] No directory is available [!]\n')

brute_force(arguments.url, arguments.wordlist) # start script
