from translate import Translator

with open('text_4.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
    text_line = []
    local_str = str

translator = Translator(from_lang='English', to_lang='Russian')
for line in content:
    new = line.split()
    translation = translator.translate(new[0])
    new[0] = translation
    local_str = '{} - {}'.format(new[0], new[2])
    text_line.append(local_str)

with open('text_4_ru.txt', 'w', encoding='utf-8') as f:
    for line in text_line:
        f.writelines(f'{line}\n')
