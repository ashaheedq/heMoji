import json
import sys

ORIG_RECORD_FILE = '../data/hebrew_tweets_wtime_3G_test.json'
TWEETS_TEXT_FILE = '../data/hebrew_tweets_3G_mini_test2.tsv'
LINES_TO_PROCESS = 100000


def getArgs():
    if len(sys.argv) == 4:
        orig_file = sys.argv[1]
        tweets_text_file = sys.argv[2]
        lines_to_process = sys.argv[3]
        if lines_to_process == "all":
            lines_to_process = sum(1 for line in open(orig_file))
    else:
        orig_file = ORIG_RECORD_FILE
        tweets_text_file = TWEETS_TEXT_FILE
        lines_to_process = LINES_TO_PROCESS

    print("""\nLoading original file: "{0}" and Parsing the {1} lines out of this file to: "{2}"\n""".format(
        orig_file, lines_to_process, tweets_text_file))

    return orig_file, tweets_text_file, lines_to_process


def extractTextFromTweets(orig_file, tweets_text_file, lines_to_process):
    # initialize (clean) file
    with open(tweets_text_file, 'w') as f_mini:
        f_mini.write("")

    # print (lines_to_process) lines from (orig_file) to (tweets_meta_file)
    with open(orig_file, 'r') as f:
        dropped_lines = 0
        for i in range(lines_to_process):
            x = f.readline()
            if i % 100000 == 0:
                print("Parsing line {} out of {} ({}%) ...".format(i, lines_to_process, i*100.0/lines_to_process))
            with open(tweets_text_file, 'a') as f_txt:
                if not x: break
                if x != '\n':
                    try:
                        js = json.loads(x)
                        if 'text' in js:
                            f_txt.write(js['text'].encode('utf-8'))
                            f_txt.write('\n')
                            # tsv_writer.writerow(js['text'].encode('utf-8'))
                    except ValueError as e:
                        print("[WARNING] line number {0} is invalid to extract: {1}".format(i, x))
                        dropped_lines += 1
        print("Done!\nLines parsed successfully: {0}\nLines dropped: {1}".format(i, dropped_lines))


if __name__ == '__main__':
    """
    Usage: python make_tweets.py [ORIG_RECORD_FILE] [TWEETS_TEXT_FILE] [LINES_TO_PROCESS]
    my Usage example: python make_tweets.py ../../../he_tweets/hebrew_tweets_wtime_500G.json ../../data/tweets_500G.txt all &> ../../data/tweets_500G.log.txt
    1. Iterate over original record file (ORIG_RECORD_FILE)
    2. and print only the text to (TWEETS_TEXT_FILE)
    """
    orig_file, tweets_text_file, lines_to_process = getArgs()
    extractTextFromTweets(orig_file, tweets_text_file, lines_to_process)