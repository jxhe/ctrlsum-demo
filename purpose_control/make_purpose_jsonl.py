import json

data = []
last_article = ""

with open('test.purpose.source') as fs, \
    open('test.purpose.hypo') as fh:
    for s, h in zip(fs, fh):
        s = s.strip().split(' => ')
        prompt = s[0]
        article = ' => '.join(s[1:])

        data.append({
            'prompt': prompt,
            'article': article,
            'hypo': h.strip(),
        })

with open('purpose.jsonl', 'w') as fout:
    for d in data:
        fout.write(f'{json.dumps(d)}\n')
