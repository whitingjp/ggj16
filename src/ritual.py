import subprocess
import os

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
for i in range(len(cards)):
	card = cards[i]
	if len(card) < 1 or card[0] == '-':
		continue
	table += '''
		<tbody>
			<tr>
				<td>%d</td>
				<td>%s</td>
			</tr>
		</tbody>
	''' % (i, card)
table += '''
	</table>
'''

s = s.replace('%%%CARD_TABLE%%%', table)

post.write(s)
post.close()
pre.close()
