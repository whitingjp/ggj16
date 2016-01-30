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
post.write(s)
post.close()
pre.close()
