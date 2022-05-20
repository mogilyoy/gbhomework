# Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.


with open('file2.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
print(f'В файле {len(lines)} строки')
i = 1

for line in lines:
    word = line.strip().replace(' -', '').count(' ')
    print(f'в {i} строке {word + 1} слов(a)')
    i+=1



