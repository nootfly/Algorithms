from os import listdir
from os.path import isfile, join
import os, fnmatch
from datetime import datetime


global all_files
NAME_CACHE = "name_cache"
all_files = []

class Record(object):
      def __init__(self, filename, name, created = None):
          self.filename = filename
          self.name = name
          self.created = created

      def created_time(self):
          return datetime.fromtimestamp(float(self.created)).strftime('%d %B %Y')

      def __str__(self):
          return "filename={}, name={}, created={}".format(self.filename, self.name, self.created_time())     

def fetch_files(dirname):
    global all_files
    for root, _, files in os.walk(dirname):
       for file in files:
          if file.endswith(".md"):
             filename = os.path.join(root, file)
             stat = os.stat(filename)
             created = None
             try:
                created = stat.st_birthtime
             except AttributeError:
                created = stat.st_mtime
             name = open(filename).readline().rstrip().replace('# ', '')   
             record = Record(filename, name, created)
             all_files.append(record) 

def generate_readme_str():
    sorted_files = sorted(all_files, key=lambda x:x.created, reverse=True)
    text = '# CodeMoments\n\r'
    for record in sorted_files:
        temp = '[{}]({}) - {}\n\n'.format(record.name, record.filename.replace('./', ''), record.created_time())
        text += temp
    return text
            

if __name__ == "__main__":
    fetch_files('.')
    print(generate_readme_str())
    with open('README.md', 'w') as f:
          f.write(generate_readme_str())
              
