import json

data = []
last_article = ""

with open('test.entity.source') as fs, \
    open('test.entity.hypo') as fh:
    for s, h in zip(fs, fh):
        s = s.strip().split(' => ')
        entity = s[0]
        article = ' => '.join(s[1:])
        if article[:min(50, len(article))] == last_article:
            new = False
        else:
            new = True

        if new:
            data.append({
                'entity': [entity],
                'article': article,
                'hypo': [h.strip()],
            })
        else:
            data[-1]['entity'].append(entity)
            data[-1]['hypo'].append(h.strip())

        last_article = article[:min(50, len(article))]

with open('entity.jsonl', 'w') as fout:
    for d in data:
        fout.write(f'{json.dumps(d)}\n')
