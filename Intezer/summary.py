from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor
import sys
import csv
import requests
from urllib.request import urlparse, urljoin
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

from bs4 import BeautifulSoup

urls = []
#document = "Natural language generation (NLG) is the natural language processing task of generating natural language from a machine representation system such as a knowledge base or a logical form. Psycholinguists prefer the term language production when such formal representations are interpreted as models for mental representations."   
f = open("internal_links.txt", "r")

for line in f :
    urls.append(line.strip()) 
#sys.stdout = open(f"summarized.txt", "w")
cf = open("intezer.csv",'w')
writer = csv.writer(cf)
writer.writerow(["url","summary"])
count = 0
for url in urls :
            if count < 5 :        
                    html_page = requests.get(url, headers=headers)
                    soup = BeautifulSoup(html_page.content, 'lxml')
                    count = count +1
                    document = ""
                    
                    try:
                        head = soup.findAll('div',{'class':'single-post-content'}) #.find_all("p")
                        for div in head :
                            a = div.findAll('p')
                            for i in a :
                                document = document+i.get_text()
                            b = div.findAll('li')
                            for j in b :
                                document = document+j.get_text()
                          
                        writer.writerow([url,document])
                                        
                        """
                        # Object of automatic summarization.
                        auto_abstractor = AutoAbstractor()
                            # Set tokenizer.
                        auto_abstractor.tokenizable_doc = SimpleTokenizer()
                            # Set delimiter for making a list of sentence.
                        auto_abstractor.delimiter_list = [".", "\n"]
                            # Object of abstracting and filtering document.
                        abstractable_doc = TopNRankAbstractor()
                            # Summarize document.
                        result_dict = auto_abstractor.summarize(document, abstractable_doc)

                            # Output result.
                        #with open(f"summarized.txt", "w") as f:
                        
                        for sentence in result_dict["summarize_result"]:
                                #print(url +"\t"+ sentence)
                                 
                                 
                                writer.writerow([url,sentence])
                                count = count +1
                                #print(sentence, file=nf)"""
                    except(TypeError, KeyError, AttributeError) as e:
                        pass