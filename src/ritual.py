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


def create_table(cards, start_suit):
	table_header = '''
		<table class="u-full-width">
			<thead>
			</thead>
			<tbody>
	'''
	table_image = '<p><img src="minidisc.png" /></p>'
	table_image_final = '<p><img src="minidisc.png" class="no-break" /></p>'
	table_footer = '''
			</tbody>
		</table>

	'''


	table = table_header
	card_count = 0;
	for card in cards:
		if len(card) < 1 or card[0] == '-':
			continue
		suit = card_count/13+start_suit
		card_number = (card_count)%13+1
		if suit == 1 or suit == 3:
			suit_class = 'black_suit'
		else:
			suit_class = 'red_suit'
		if card_count > 0:
			header_class = 'margin'
		else:
			header_class = ''
		if card_number == 1:
			table += '''
				<tr>
					<th class='%s'></th>
					<th class='%s'>%s</th>
				</tr>
		''' % (header_class, header_class, suit_string(suit))

		table += '''
				<tr>
					<td><span class="%s">%s</span>%s</td>
					<td>%s</td>
				</tr>
		''' % (suit_class, suit_symbol_string(suit), card_num_string(card_number), card)

		if len(cards) > 20:
			num_cards = 39
		else:
			num_cards = 13
		if card_count%13 == 12 and card_count != num_cards-1:
			table += table_footer
			table += table_image
			table += table_header

		card_count = card_count+1
	table += table_footer
	if card_count < 20:
		table += table_image
	else:
		table += table_image_final
	return table

content = subprocess.check_output(['markdown', 'src/ritual.md'])

pre = open('src/ritual.pre', 'r')
dest_filename=('build/index.html')

directory = os.path.dirname(dest_filename)
if not os.path.exists(directory):
	os.makedirs(directory)
post = open(dest_filename, 'w')

s = pre.read()
s = s.replace('%%%MARKDOWN%%%', content)

bootstrap_file = open('src/bootstrap.txt', 'r')
bootstrap_cards = bootstrap_file.read().split('\n')
bootstrap_table = create_table(bootstrap_cards, 3)
s = s.replace('%%%BOOTSTRAP_TABLE%%%', bootstrap_table)

card_file = open('src/cards.txt', 'r')
cards = card_file.read().split('\n')
card_table = create_table(cards, 0)
s = s.replace('%%%CARD_TABLE%%%', card_table)

post.write(s)
post.close()
pre.close()
