import json

data = []
last_article = ""

with open('test.contribution.source') as fs, \
    open('test.contribution.hypo') as fh:
    for s, h in zip(fs, fh):
        s = s.strip().split(' => ')
        prompt = s[0]
        article = ' => '.join(s[1:])

        data.append({
            'prompt': prompt,
            'article': article,
            'hypo': f'{prompt[:-6]} {h.strip()}',
        })

with open('contribution.jsonl', 'w') as fout:
    for d in data:
        fout.write(f'{json.dumps(d)}\n')
