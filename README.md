# API for TV Week Magazine 《香港電視》

TV Week is a weekly periodical published by Television Broadcasts Limited (TVB) between 1967 to 1997 in Hong Kong. For more information of the periodical, visit: [https://zh.m.wikipedia.org/zh-hk/香港電視_(雜誌)]( https://zh.m.wikipedia.org/zh-hk/香港電視_(雜誌) ).

The digitized version of the periodical are avaialble on《中港電視。電影刊物資料庫》 (https://digital.lib.hkbu.edu.hk/film-tv/), Hong Kong Baptist University Library (Digital Initiative & Research Cluster). 


## Resource URL
```
https://digital.lib.hkbu.edu.hk/api/tvweek/
```

## API Outputs
 The API returns the following output (by issues)
 - issue number
 - published date
 - URL of cover page thumbnail image
 - list of keywords indexed from the contents
 - URL to digitized version on HKBU Library web server

### Example Browse Parameters:
https://digital.lib.hkbu.edu.hk/api/tvweek/?issueNumber=1028
https://digital.lib.hkbu.edu.hk/api/tvweek/?startIssueNumber=123&endIssueNumber=308
https://digital.lib.hkbu.edu.hk/api/tvweek/?startDate=1985-01-01&endDate=1990-01-01


Output limit:
Note that each API query only returns results of 20 issues. To return more:
https://digital.lib.hkbu.edu.hk/api/tvweek/?start=0&limit=300


Pages:
https://digital.lib.hkbu.edu.hk/api/tvweek/?start=0&limit=10
https://digital.lib.hkbu.edu.hk/api/tvweek/?start=11&limit=10
https://digital.lib.hkbu.edu.hk/api/tvweek/?start=21&limit=10


Examples:

Basic tallying of keywords from specific issues




Named Entity Recognition from a specific issue
```
import stanza
import requests

url = "https://digital.lib.hkbu.edu.hk/api/tvweek/api.php?issueNumber=18"
r = requests.get(url)
data = r.json()
wordlist = data['Results'][0]['keywords']

nlp = stanza.Pipeline(lang='zh', processors='tokenize,ner',tokenize_pretokenized=True)

for w in wordlist:
    doc = nlp(w)
    print(*[f'entity: {ent.text}\ttype: {ent.type}' for sent in doc.sentences for ent in sent.ents], sep='\n')
    

```



Face recognition on magazine cover thumbnail images
    
    




Note:
- The databases have these missing issues: 253, 254, 255, 257, 258, 259, 401, 402, 405, 408, 409, 410, 715

