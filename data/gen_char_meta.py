
f1 = open('ids.txt', 'r', encoding='utf-8')
f2 = open('Unihan_Readings.txt', 'r', encoding='utf-8')
f3 = open('char_meta.txt', 'w', encoding='utf-8')

strokes = f1.readlines()
spells = f2.readlines()

new_strokes = {}
new_spells = {}

tone_dict = {
    'ā': ['a', '1'],
    'á': ['a', '2'],
    'ǎ': ['a', '3'],
    'à': ['a', '4'],

    'ō': ['o', '1'],
    'ó': ['o', '2'],
    'ǒ': ['o', '3'],
    'ò': ['o', '4'],

    'ē': ['e', '1'],
    'é': ['e', '2'],
    'ě': ['e', '3'],
    'è': ['e', '4'],

    'ī': ['i', '1'],
    'í': ['i', '2'],
    'ǐ': ['i', '3'],
    'ì': ['i', '4'],

    'ū': ['u', '1'],
    'ú': ['u', '2'],
    'ǔ': ['u', '3'],
    'ù': ['u', '4'],
}

for i, st in enumerate(strokes):
    st1 = st.strip().split('	')

    if st1[0] == 'U+29343':
        print(ord(st1[1]))

    if st1[1] in ['𡱺', '鼖']:
        continue
    if ord(st1[1]) in [194823, 168771]:
        continue
    new_strokes[st1[0]] = st1[1]

for i, sp in enumerate(spells):
    sp1 = sp.strip().split('	')
    if not sp1:
        continue
    if sp1[0] not in new_spells:
        new_spells[sp1[0]] = {
            'kHanyuPinyin': '',
            'kCantonese': '',
            'kKorean': '',
            'kJapaneseOn': '',
            'kVietnamese': ''
        }
        if sp1[1] == 'kHanyuPinlu':
            sp1[1] = 'kHanyuPinyin'
        if sp1[1] in new_spells[sp1[0]].keys():
            new_spells[sp1[0]][sp1[1]] = sp1[2].split(':')[-1].split('(')[0]
    else:
        if sp1[1] == 'kHanyuPinlu':
            sp1[1] = 'kHanyuPinyin'
        if sp1[1] in new_spells[sp1[0]].keys():
            new_spells[sp1[0]][sp1[1]] = sp1[2].split(':')[-1].split('(')[0]

# new_new_spells = {}
# for i in new_spells:
#     flag = 1
#     for j in new_spells[i]:
#         if not new_spells[i][j]:
#             flag = 0
#     if flag:
#         new_new_spells[i] = new_spells[i]
#     else:
#         continue

for i in new_strokes:
    if i in new_spells:
        # j = ';'.join(new_spells[i].values())
        j = new_spells[i].get('kHanyuPinyin')
        j1 = j.split(',')
        j2 = []
        for sub_j in j1:
            for k in sub_j:
                if k in tone_dict:
                    sub_j = sub_j.replace(k, tone_dict[k][0])
                    sub_j += tone_dict[k][1]
                    j2.append(sub_j)
                    break
        j = ','.join(j2)
        f3.write(i + '	' + new_strokes[i] + '	' +
                 j + '	' + new_strokes[i] + '\n')

f1.close()
f2.close()
f3.close()
