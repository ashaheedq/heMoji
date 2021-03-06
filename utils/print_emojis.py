"""
PRINTING EMOJIS FROM THE DESIRED DATA_TYPE TO FILE (emojis/DATA_TYPE.txt)
"""
DATA_TYPE = 'deep'


l2e_str = 'l2e' + DATA_TYPE
# exec "from src.emoji2label import %s as e2l" % e2l_str
exec "from src.emoji2label import %s as l2e" % l2e_str


file_path = 'emojis/{0}.txt'.format(DATA_TYPE)
with open(file_path, 'w') as f:
    for l in l2e:
        e_unicode = l2e[l]
        # label_index | unicode_emoji | unicode_str
        line = str(l) + '\t' + e_unicode.encode('utf-8') + '\t' + e_unicode.encode('unicode-escape')
        f.writelines(line)
        f.writelines('\n')
