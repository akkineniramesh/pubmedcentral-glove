from __future__ import print_function
from glove import Glove
from glove import Corpus
def main():
    corpus_model = Corpus()
    corpus_model = Corpus.load('bioc-corpus-AZ2.model')
    glove = Glove(no_components=100, learning_rate=0.05)
    glove.fit(corpus_model.matrix, epochs=10, no_threads=16, verbose=True)
    glove.add_dictionary(corpus_model.dictionary)
    glove.save('bioc-glove-AZ2.model')
main()
