import stanza
import requests
import re   

url = "https://digital.lib.hkbu.edu.hk/api/tvweek/?issueNumber=118"
r = requests.get(url)
data = r.json()
wordlist = data['Results'][0]['keywords']


nlp = stanza.Pipeline(lang='zh', processors='tokenize,ner',tokenize_pretokenized=True)
english_check = re.compile(r'[a-z]')

for w in wordlist:
    if not(english_check.match(w)):
        doc = nlp(w)
        #print(*[f'entity: {ent.text}\ttype: {ent.type}' for sent in doc.sentences for ent in sent.ents], sep='\n')        
        if(len(doc.sentences[0].ents))>0:
            print("Text: " + doc.sentences[0].ents[0].text + "\t\t Entity: " + doc.sentences[0].ents[0].type)
