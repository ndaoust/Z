# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import argparse, codecs, sys

# Parseur de ligne de commande
parser = argparse.ArgumentParser(description="Sorts or inverts lines or characters from a file.")
parser.add_argument('-f', help="input file")
# seul -l ou -c est permis
lorc = parser.add_mutually_exclusive_group()
lorc.add_argument('-l', help='line sort (default)', action='store_true')
lorc.add_argument('-c', help='character sort', action='store_true')
parser.add_argument('mode', help='either "sort" or "invert"')
args = parser.parse_args()

# Lecture du fichier
lines = []
try:
	with codecs.open(args.f, 'r', encoding='utf8') as f:
		for line in f.readlines():
			# on élimine les retours à la ligne en vue de l'éventuel tri
			lines.append(line.rstrip('\n'))
except IOError:
	sys.exit('Error: file not found')

# Opérations sur le texte
# (si le paramètre -c est spécificié, chaque ligne est aussi
#	 triée ou inversée; le paramètre -l n'est jamais vérifié,
#  mais l'utilisateur peut l'utiliser pour se "rassurer")
if args.mode == 'sort':
	# tri selon l'ordre de Python
	if args.c:
		for i in range(0, len(lines)):
			lines[i] = ''.join(sorted(lines[i]))
	lines.sort()
elif args.mode == 'invert':
	# inversion
	# (c'est peu efficace de procéder à l'inversion explicitement,
	#  mais c'est plus clair, et 'sort' est bien pire de toute façon!)
	if args.c:
		for i in range(0, len(lines)):
			lines[i] = lines[i][::-1]
	lines.reverse()
else:
	# si un mode erroné est spécifié, les lignes ne sont pas modifiées
	sys.exit("Error: unrecognized mode (must be either 'sort' or 'invert')")

# Impression
for line in lines:
	sys.stdout.write(line+'\n')