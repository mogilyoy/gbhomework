# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
def int_func(*args):
   return args.title()

text = input('Введите текст: ')
print(int_func(text))