import googletrans

translator = googletrans.Translator()
read_file_path = r"eng.txt"
write_file_path = r"kor.txt"
with open(read_file_path, 'r') as f:
    readLines = f.readlines()

    for line in readLines:
        print(line)
        result = translator.translate(line, dest='ko')
        print(result.text)
        with open(write_file_path, 'a', encoding='UTF8') as f:
            f.write(result.text + '\n')