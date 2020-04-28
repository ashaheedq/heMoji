import emoji

# specific emojis were taken from from https://github.com/bfelbo/DeepMoji/blob/master/emoji_unicode.csv
deepe2l = {
    u'\U0001f602': 0,
    u'\U0001f612': 1,
    u'\U0001f629': 2,
    u'\U0001f62d': 3,
    u'\U0001f60d': 4,
    u'\U0001f614': 5,
    u'\U0001f44c': 6,
    u'\U0001f60a': 7,
    u'\U0001f60f': 8,
    u'\U0001f601': 9,
    u'\U0001f3b6': 10,
    u'\U0001f633': 11,
    u'\U0001f4af': 12,
    u'\U0001f634': 13,
    u'\U0001f60c': 14,
    u'\U0001f64c': 15,
    u'\U0001f495': 16,
    u'\U0001f611': 17,
    u'\U0001f605': 18,
    u'\U0001f64f': 19,
    u'\U0001f615': 20,
    u'\U0001f618': 21,
    u'\U0001f610': 22,
    u'\U0001f481': 23,
    u'\U0001f61e': 24,
    u'\U0001f648': 25,
    u'\U0001f62b': 26,
    u'\U0001f60e': 27,
    u'\U0001f621': 28,
    u'\U0001f44d': 29,
    u'\U0001f622': 30,
    u'\U0001f62a': 31,
    u'\U0001f60b': 32,
    u'\U0001f624': 33,
    u'\U0001f637': 34,
    u'\U0001f44f': 35,
    u'\U0001f440': 36,
    u'\U0001f52b': 37,
    u'\U0001f623': 38,
    u'\U0001f608': 39,
    u'\U0001f613': 40,
    u'\U0001f494': 41,
    u'\U0001f3a7': 42,
    u'\U0001f64a': 43,
    u'\U0001f609': 44,
    u'\U0001f480': 45,
    u'\U0001f616': 46,
    u'\U0001f604': 47,
    u'\U0001f61c': 48,
    u'\U0001f620': 49,
    u'\U0001f645': 50,
    u'\U0001f4aa': 51,
    u'\U0001f44a': 52,
    u'\U0001f49c': 53,
    u'\U0001f496': 54,
    u'\U0001f499': 55,
    u'\U0001f62c': 56,
    u'\u2764': 57,
    u'\u263a': 58,
    u'\u2665': 59,
    u'\u270c': 60,
    u'\u270b': 61,
    u'\u2661': 62,
    u'\u2728': 63
}
l2edeep = {v: k for k, v in deepe2l.items()}

alle2l = {v: i for i, (k, v) in enumerate(emoji.EMOJI_UNICODE.items())}
l2eall = {v: k for k, v in alle2l.items()}

# emojis were picked based on the original (deepe2l) set and the current data freq
# https://docs.google.com/spreadsheets/d/1E0ZzRJ5Q2iACvitC6zJgHBCf_uUTED-5WIoX5trcrm4/edit#gid=1034682859
data01e2l = {
    u'\U0001f602': 0,
    u'\U0001f60d': 1,
    u'\u2764': 2,
    u'\U0001f609': 3,
    u'\U0001f629': 4,
    u'\U0001f44c': 5,
    u'\U0001f62d': 6,
    u'\U0001f618': 7,
    u'\U0001f60a': 8,
    u'\U0001f64f': 9,
    u'\U0001f44d': 10,
    u'\U0001f61c': 11,
    u'\U0001f44f': 12,
    u'\U0001f634': 13,
    u'\U0001f601': 14,
    u'\U0001f633': 15,
    u'\U0001f60f': 16,
    u'\U0001f605': 17,
    u'\U0001f60c': 18,
    u'\u263a': 19,
    u'\U0001f62b': 20,
    u'\U0001f64c': 21,
    u'\U0001f60e': 22,
    u'\U0001f49c': 23,
    u'\U0001f499': 24,
    u'\U0001f60b': 25,
    u'\U0001f62a': 26,
    u'\U0001f612': 27,
    u'\U0001f4aa': 28,
    u'\U0001f621': 29,
    u'\U0001f614': 30,
    u'\U0001f622': 31,
    u'\U0001f3b6': 32,
    u'\u2665': 33,
    u'\U0001f495': 34,
    u'\u270b': 35,
    u'\U0001f604': 36,
    u'\U0001f494': 37,
    u'\U0001f613': 38,
    u'\U0001f3a7': 39,
    u'\U0001f648': 40,
    u'\U0001f615': 41,
    u'\U0001f624': 42,
    u'\U0001f616': 43,
    u'\U0001f608': 44,
    u'\U0001f61e': 45,
    u'\U0001f623': 46,
    u'\U0001f611': 47,
    u'\U0001f64a': 48,
    u'\U0001f631': 49,
    u'\U0001F625': 50,
    u'\U0001f389': 51,
    u'\U0001f61D': 52,
    u'\U0001f48B': 53,
    u'\U0001F610': 54,
    u'\U0001f44E': 55,
    u'\U0001f497': 56,
    u'\U0001f44B': 57,
    u'\U0001F637': 58,
    u'\U0001f525': 59,
    u'\U0001f607': 60,
    u'\U0001f44A': 61,
    u'\U0000270C': 62,
    u'\U0001f630': 63
}
l2edata01 = {v: k for k, v in data01e2l.items()}

if __name__ == '__main__':
    print(data01e2l.keys())