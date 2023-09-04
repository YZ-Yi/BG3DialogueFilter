# Importing BeautifulSoup class from the bs4 module
from bs4 import BeautifulSoup
from pathlib import Path
  
import os
import os.path
import re

inpath = 'Dialogs'
outpath= 'output'
keyword = 'keyword'

# Parse func
def my_parse(fname, fdir):
    my_url = os.path.join(fdir, fname)
    with open(my_url, encoding="utf8") as fp:
        s = BeautifulSoup(fp, 'html.parser')
        if s.findAll(string=re.compile(keyword)):
            output_file(fname, fdir, s.prettify)

# Output file
def output_file(fname, fdir, content):
    path = outpath
    full_path = os.path.join(path, fdir)
    # Check if dir exists
    os.makedirs(full_path, exist_ok=True)
    # if not os.path.exists(full_path):
        # os.mkdir(full_path)
    full_name = os.path.join(full_path, fname)
    f = open(full_name, 'w', encoding="utf8")
    f.write(str(content))
    f.close

# Main func
def main():
    # Read all files
    for dir in Path(inpath).rglob('*.html'):
        d = os.path.join(dir.parent, dir.name)
        my_parse(dir.name, dir.parent)

if __name__ == "__main__":
    main()