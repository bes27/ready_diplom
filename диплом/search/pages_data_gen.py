import re
import pathlib
import bs4 as bs
import os

BLACK_LIST = re.compile(r'.*node_modules.*|_.*|.*[/\\]_.*')

out_path = 'search/pages_data.js'
input_paths = [
    '..',
]

CLEANR = re.compile(r'<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
data = []

id = 0

for path in input_paths:
    for doc in pathlib.Path(path).rglob('*.html'):
        if re.match(BLACK_LIST, str(doc)):
            continue
        soup = bs.BeautifulSoup(open(doc).read(),'lxml')
        title = soup.find('meta', {'name' : 'search-title'})
        title = title["content"] if title else None

        if not title:
            title = soup.find(id='title')
            title = title.text if title else None

        content = soup.find(id='content')

        if not title and not content:
            continue
        
        title = title if title else '(Без заголовка)'
        content = content.text if content else '(Без содержимого)'

        title = re.sub(CLEANR, ' ', title)
        content = re.sub(CLEANR, ' ', content)
        title = re.sub(r'\s+', ' ', title)
        content = re.sub(r'\s+', ' ', content)

        data += [{
            'id' : str(id),
            'link' : str(doc),
            'title' : title,
            'content' : content
        }]

        id += 1

if os.path.exists(out_path):
    os.replace(out_path, out_path + '.bak')

with open(out_path, 'w') as out:
    out.write('var pages_data = ' + str(data))
