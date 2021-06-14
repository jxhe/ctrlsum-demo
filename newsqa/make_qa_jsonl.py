import json

data = {}

with open('dev.newsqa.source') as fs, \
    open('dev.newsqa.hypo') as fh, \
    open('dev.newsqa.target') as ft:
    for s, h, t in zip(fs, fh, ft):
        s = s.strip().split(' => ')
        question = s[0]
        article = ' => '.join(s[1:])
        key = article[:min(50, len(article))]
        
        if key in data:
            data[key]['Q'].append(question)
            data[key]['A'].append(f'{question} {h.strip()}')
            data[key]['GA'].append(t.strip())
        else:
            data[key] = {
                'article': article,
                'Q': [question],
                'A': [f'{question} {h.strip()}'],
                'GA': [t.strip()],
            }
      


with open('newsqa.jsonl', 'w') as fout:
    for d, v in data.items():
        fout.write(f'{json.dumps(v)}\n')
