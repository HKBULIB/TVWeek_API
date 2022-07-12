# API for TV Week Magazine 《香港電視》

TV Week is a weekly periodical published by Television Broadcasts Limited (TVB) between 1967 to 1997 in Hong Kong. For more information of the periodical, visit: [https://zh.m.wikipedia.org/zh-hk/香港電視_(雜誌)]( https://zh.m.wikipedia.org/zh-hk/香港電視_(雜誌) ).

The digitized version of the periodicals are avaialble on《中港電視。電影刊物資料庫》 (https://digital.lib.hkbu.edu.hk/film-tv/), Hong Kong Baptist University Library (Digital Initiative & Research Cluster). 


## Resource URL
```
https://digital.lib.hkbu.edu.hk/api/tvweek/
```

## API Outputs
 The API returns the following output (by issues):
 - issue number
 - published date
 - URL of cover page thumbnail image
 - list of keywords indexed from the contents
 - URL to digitized version on HKBU Library web server

### Example Outputs

Results returned by specific issue number (1088):

https://digital.lib.hkbu.edu.hk/api/tvweek/?issueNumber=1088
```
{
    "totalResults": 1,
    "Results": [
        {
            "issueNumber": 1088,
            "publishedDate": "1988-09-08T00:00:00Z",
            "coverThumbnail": "https:\/\/storage.lib.hkbu.edu.hk\/tvweek\/Thumbnail\/1088\/1088_001.jpg",
            "keywords": [
                "奧林匹克運動會",
                "白金巨星耀保良",
                "劉嘉玲",
                "呂方",
                ...
                ...
                "味之素",
                "和春堂",
                "哥倫比亞電影公司",
                "哥羅廸巴里"
            ],
            "url": "https:\/\/digital.lib.hkbu.edu.hk\/film-tv\/magazines\/yes\/years\/1988\/books\/1088"
        }
    ]
}
```

Results returned by specific range of issue numbers (130 - 135):

https://digital.lib.hkbu.edu.hk/api/tvweek/?startIssueNumber=130&endIssueNumber=135
```
{
    "totalResults": 6,
    "Results": [
        {
            "issueNumber": 130,
            "publishedDate": "1970-05-05T00:00:00Z",
            "coverThumbnail": "https:\/\/storage.lib.hkbu.edu.hk\/tvweek\/Thumbnail\/130\/130_001.jpg",
            "keywords": [
                "沈殿霞",
                "神偷諜影",
                ...
                "張瑛",
                "張英才"
            ],
            "url": "https:\/\/digital.lib.hkbu.edu.hk\/film-tv\/magazines\/yes\/years\/1970\/books\/130"
        },
        {
            "issueNumber": 131,
            "publishedDate": "1970-05-12T00:00:00Z",
            "coverThumbnail": "https:\/\/storage.lib.hkbu.edu.hk\/tvweek\/Thumbnail\/131\/131_001.jpg",
            "keywords": [
                "歡樂今宵",
                "張瑛",
                 ...
                "安杜披雲",
                "安東尼巴素"
            ],
            "url": "https:\/\/digital.lib.hkbu.edu.hk\/film-tv\/magazines\/yes\/years\/1970\/books\/131"
        },
        {
            "issueNumber": 132,
            "publishedDate": "1970-05-19T00:00:00Z",
            "coverThumbnail": "https:\/\/storage.lib.hkbu.edu.hk\/tvweek\/Thumbnail\/132\/132_001.jpg",
            "keywords": [
                "歡樂今宵",
                "歡樂家庭",
                 ...
                "安鐸",
                "宋惠慈"
            ],
            "url": "https:\/\/digital.lib.hkbu.edu.hk\/film-tv\/magazines\/yes\/years\/1970\/books\/132"
        },
        {
            "issueNumber": 133,
            "publishedDate": "1970-05-26T00:00:00Z",
            "coverThumbnail": "https:\/\/storage.lib.hkbu.edu.hk\/tvweek\/Thumbnail\/133\/133_001.jpg",
            "keywords": [
                "歡樂今宵",
                "兒童節目",
                 ...
                "夢會牡丹亭",
                "奇蓮伊士活"
            ],
            "url": "https:\/\/digital.lib.hkbu.edu.hk\/film-tv\/magazines\/yes\/years\/1970\/books\/133"
        },
        {
            "issueNumber": 134,
            "publishedDate": "1970-06-02T00:00:00Z",
            "coverThumbnail": "https:\/\/storage.lib.hkbu.edu.hk\/tvweek\/Thumbnail\/134\/134_001.jpg",
            "keywords": [
                "歡樂今宵",
                "羅拔韋納",
                 ...
                "大衛白賴仁",
                "大衛花拉"
            ],
            "url": "https:\/\/digital.lib.hkbu.edu.hk\/film-tv\/magazines\/yes\/years\/1970\/books\/134"
        },
        {
            "issueNumber": 135,
            "publishedDate": "1970-06-09T00:00:00Z",
            "coverThumbnail": "https:\/\/storage.lib.hkbu.edu.hk\/tvweek\/Thumbnail\/135\/135_001.jpg",
            "keywords": [
                "歡樂今宵",
                "劉家傑",
                 ...
                "喧尼斯鮑寧",
                "噢多可愛的戰爭"
            ],
            "url": "https:\/\/digital.lib.hkbu.edu.hk\/film-tv\/magazines\/yes\/years\/1970\/books\/135"
        }
    ]
}
```


Results returned by specific range of published date (01 March 1985 - 31 December 1985):

https://digital.lib.hkbu.edu.hk/api/tvweek/?startDate=1985-03-01&endDate=1985-12-31
```
{
    "totalResults": 43,
    "Results": [
        {
            "issueNumber": 905,
            "publishedDate": "1985-03-07T00:00:00Z",
            "coverThumbnail": "https:\/\/storage.lib.hkbu.edu.hk\/tvweek\/Thumbnail\/905\/905_001.jpg",
            "keywords": [
                "婦女新姿",
                "汪明荃",
                ...
                "夢幻之旋律",
                "大地旅運社"
            ],
            "url": "https:\/\/digital.lib.hkbu.edu.hk\/film-tv\/magazines\/yes\/years\/1985\/books\/905"
        },
        {
            "issueNumber": 906,
            "publishedDate": "1985-03-14T00:00:00Z",
            "coverThumbnail": "https:\/\/storage.lib.hkbu.edu.hk\/tvweek\/Thumbnail\/906\/906_001.jpg",
            "keywords": [
                "歡樂今宵",
                "張國榮",
                ...
                "奧莉花紐頓莊",
                "奪標"
            ],
            "url": "https:\/\/digital.lib.hkbu.edu.hk\/film-tv\/magazines\/yes\/years\/1985\/books\/906"
        },
        ...
        ...
        {
            "issueNumber": 923,
            "publishedDate": "1985-07-11T00:00:00Z",
            "coverThumbnail": "https:\/\/storage.lib.hkbu.edu.hk\/tvweek\/Thumbnail\/923\/923_001.jpg",
            "keywords": [
                "新秀歌唱大賽",
                "婦女新姿",
                ...
                "何文匯",
                "保治靈"
            ],
            "url": "https:\/\/digital.lib.hkbu.edu.hk\/film-tv\/magazines\/yes\/years\/1985\/books\/923"
        },
        {
            "issueNumber": 924,
            "publishedDate": "1985-07-18T00:00:00Z",
            "coverThumbnail": "https:\/\/storage.lib.hkbu.edu.hk\/tvweek\/Thumbnail\/924\/924_001.jpg",
            "keywords": [
                "歡樂今宵",
                "香港電視",
                 ...
                "周生生珠寶金行有限公司",
                "周繩武"
            ],
            "url": "https:\/\/digital.lib.hkbu.edu.hk\/film-tv\/magazines\/yes\/years\/1985\/books\/924"
        }
    ]
}
```



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

