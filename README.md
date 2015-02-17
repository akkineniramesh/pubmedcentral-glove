# pubmedcentral-glove
Glove applied to Pubmed Central BioC Corpus

We all want to read a lot of research papers but do not have enough time. It is now possible to consider all the evidence in a lot of research papers in Pubmed Central without much effort. You can confirm your hunch faster and proceed to invest more of your time on promising ideas.

This small Ipython notebook shows how to use Glove Algorithm http://nlp.stanford.edu/projects/glove/ to analyze PubmedCentral BioC Corpus with almost no effort.
Steps:
1. If you do not have python installed, download and install Anaconda to save time.
2. download and install glove-python from https://github.com/maciejkula/glove-python
3. download ascii.A-B.tar.gz and BioC.dtd from ftp://ftp.ncbi.nlm.nih.gov/pub/wilbur/BioC-PMC/
4. use command 'ipython notebook' to run the notebook

Use the python3.4 files for applying Glove to whole of BioC Corpus at once. Needs lots of RAM, I used n1-highmem-16 instance of Google compute and Anaconda python3.4 distribution. To run in background, I used the command:


nohup python pubmedcentral-corpus-py34.py > /dev/null 2>&1 &



License : Apache 2.0 License
Most of code in the IPython notebook taken from example.py of Maciejkula's glove-python -- Apache 2.0 License
