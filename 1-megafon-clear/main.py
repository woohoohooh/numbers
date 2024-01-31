db_old = []
db_clear = []

with open('numbers_old_clear.txt', 'r', encoding='utf8') as f:
    for line in f.readlines():
        db_old.append(line.strip())
already = 0
with open('numbers_new.txt', 'r', encoding='utf8') as f:
    for line in f.readlines():
        a = line.replace(' ', '').replace('-', '').strip()
        if a in db_old:
            already += 1
        else:
            db_old.append(a)

for i in db_old:
    if i not in db_clear:
        db_clear.append(i.strip())

with open('numbers_new_db_full_clear.txt', 'a', encoding='utf8') as f:
    for i in db_clear:
        f.write(i)
        f.write('\n')

print('найдено повторов:', already)