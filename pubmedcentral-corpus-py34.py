from __future__ import print_function
from glove import Corpus

import glob
from lxml import etree

#using glob to add series of files to process
#using etree from lxml
dtd_valid_file = '/home/ramesh/bioc/BioC.dtd'
def itertexts():
    chars = ''
    for c in range(256):
        chars +=chr(c)
    delchars = ''
    for c in range(256):
        if chr(c).isalnum():
            delchars +=chr(c)
        else:
            delchars +=' '
    for xmlf in glob.iglob('/home/ramesh/bioc/ascii/*.xml'):
        xml_tree = etree.parse(xmlf)    
        if dtd_valid_file is not None:
            dtd = etree.DTD(dtd_valid_file)
            if dtd.validate(xml_tree) is False:
                raise(Exception(dtd.error_log.filter_from_errors()[0]))
#for each doc write a file containing text from each passage of doc
        for texts in xml_tree.iterfind('document/passage/text'):
            yield texts.text.translate(str.maketrans(chars,delchars)).lower().split(' ')
def main():
    corpus_model = Corpus()
    corpus_model.fit(itertexts(), window=10, max_map_size=1000000)
    corpus_model.save('bioc-corpus-AZ2.model')
main()
