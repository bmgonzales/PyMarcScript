from pymarc import *

with open('MarcExport.mrc', 'rb') as fh:
  reader = MARCReader(fh)
  tag035 = open('tag035.mrc', 'wb')  
  for record in reader:
    for f in record.get_fields('035'):
      for s in f.get_subfields('a'):
        if 'Sirsi' not in s:
          tag035.write(record.as_marc())
tag035.close()
