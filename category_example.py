import json
import os


HYPERLINKS_TO_PRINT = 20
DIRECTORY_NAME = 'category_data'
FILENAMES = [
    'test_set.jsonl', 'train_set1.jsonl', 'train_set2.jsonl', 'train_set3.jsonl'
]


def main():
    for filename in FILENAMES:
        print('==', filename, '==')
        print()

        with open(os.path.join(DIRECTORY_NAME, filename)) as json_file:
            for i in range(HYPERLINKS_TO_PRINT):
                line = json_file.readline()
                json_content = json.loads(line)

                print('Policy Url:', json_content.get('Policy Url'))
                print('Opt Out Url:', json_content.get('Opt Out Url'))
                print('Sentence Text:', json_content.get('Sentence Text'))
                print('Hyperlink Text:', json_content.get('Hyperlink Text'))
                print('Labels', json_content.get('Labels'))

                print()


if __name__ == '__main__':
    main()
