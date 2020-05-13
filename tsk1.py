import json
import csv
topic_list = {}


with open('dialogs_2019-08-30.json', 'r', encoding='utf-8') as file:
    dialogs = json.load(file)

with open('dialogs.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['dialog_id', 'sender', 'text'])
    writer.writeheader()
    for dialog in dialogs:
        for line in dialog['dialog']:
            writer.writerow({'dialog_id':dialog['dialog_id'], 'sender':line['sender'], 'text':line['text']})

with open('topic_ids.tsv', 'w', encoding='utf-8') as file:
    c = 0
    for dialog in dialogs:
        for line in dialog['users'][0]['topics']:
            c += 1
            topic_list[c] = line.split('\"')[1]
            # print(line.split('\"')[1])
    for i in range(1, len(topic_list)):
        file.write('{}  {}\n'.format(i, topic_list[i]))


with open('dialogs.csv', 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['dialog_id', 'sender', 'text']
    for i in range(1, len(topic_list)):
        fieldnames.append('topic_{}_relevant'.format(i))
    writer = csv.writer(file)
    for dialog in dialogs:
        for line in dialog['dialog']:
            lc = {'dialog_id': dialog['dialog_id'], 'sender': line['sender'], 'text': line['text']}
            for i in range(1, len(topic_list)):
                if topic_list[i] in line['text']:
                    lc[i] = True
                else:
                    lc[i] = False
            writer.writerow(lc)