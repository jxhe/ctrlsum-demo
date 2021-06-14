import json

data = []
last_article = ""

sources = open('test.length.source').readlines()
hypos = open('test.length.hypo').readlines()

vary_num = 5
total_len = len(sources)

for i in range(total_len // vary_num):
    article = ' => '.join(sources[i * vary_num].strip().split(' => ')[1:])
    data.append({
        'keyword': [],
        'article': article,
        'hypo': [],
        })
    for j in range(vary_num):
        id_ = i * vary_num + j
        s, h = sources[id_], hypos[id_]
        s = s.strip().split(' => ')
        keyword = s[0]

            
        data[-1]['keyword'].append(keyword)
        data[-1]['hypo'].append(h.strip())

with open('length.jsonl', 'w') as fout:
    for d in data:
        fout.write(f'{json.dumps(d)}\n')
