import subprocess
import os

def card_num_string(n):
	if n == 1:
		return 'A'
	if n == 10:
		return 'T'
	if n == 11:
		return 'J'
	if n == 12:
		return 'Q'
	if n == 13:
		return 'K'
	return '%d' % n

def suit_symbol_string(n):
	if n == 0:
		return '&#x2666;' #diamonds
	if n == 1:
		return '&#x2660;' #spades
	if n == 2:
		return '&#x2665;' #hearts
	if n == 3:
		return '&#x2663;' #clubs

def suit_string(n):
	if n == 0:
		return 'Diamonds'
	if n == 1:
		return 'Spades'
	if n == 2:
		return 'Hearts'
	if n == 3:
		return 'Clubs'

content = subprocess.check_output(['markdown', 'src/ritual.md'])

pre = open('src/ritual.pre', 'r')
dest_filename=('build/index.html')

directory = os.path.dirname(dest_filename)
if not os.path.exists(directory):
	os.makedirs(directory)
post = open(dest_filename, 'w')

s = pre.read()
s = s.replace('%%%MARKDOWN%%%', content)

card_file = open('src/cards.txt', 'r')
cards = card_file.read()
cards = cards.split('\n')
table = ''
table += '''
	<table class="u-full-width">
		<thead>
			<tr>
				<th>Card</th>
				<th>Description</th>
			</tr>
		</thead>
	'''
card_count = 0;
for card in cards:
	if len(card) < 1 or card[0] == '-':
		continue
	suit = card_count/13
	card_number = (card_count)%13+1
	if suit == 1:
		suit_class = 'black_suit'
	else:
		suit_class = 'red_suit'
	if card_number == 1:
		table += '''
		<tbody>
			<tr>
				<td class="%s">%s</td>
				<th>%s</th>
			</tr>
		</tbody>
	''' % (suit_class, suit_symbol_string(suit), suit_string(suit))

	table += '''
		<tbody>
			<tr>
				<td class="%s">%s %s</td>
				<td>%s</td>
			</tr>
		</tbody>
	''' % (suit_class, suit_symbol_string(suit), card_num_string(card_number), card)
	card_count = card_count+1
table += '''
	</table>
'''


s = s.replace('%%%CARD_TABLE%%%', table)

post.write(s)
post.close()
pre.close()
