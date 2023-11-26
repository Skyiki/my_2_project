def solid_text(text):
    words = text.split(' ')
    words = [word.capitalize() for word in words]
    return ''.join(words)


def jumping_text(text):
    result = ""
    for i in range(len(text)):
        if i % 2 == 0:
            result += text[i].lower()
        else:
            result += text[i].upper()
    return result

def emoji_text(text):
    return text.replace(' ', '𓃱𓅢')
def reverse_text(text):
    return text[::-1]


filters = ['Сплошной текст', "Прыгающий текст", "Перевёрнутый текст", "Жираф и цапли"]
filters_description = {
    "Сплошной текст": 'Делает текст сплошным, убирая все пробелы.',
    'Прыгающий текст': 'Делает буквы по порядку: заглавными, строчными.',
    'Перевёрнутый текст': 'Переворачивает заданный текст задом наперёд.',
    'Жираф и цапли': 'Вместо пробелов ставит 𓃱𓅢'}
while True:
    print("Выберите фильтр для обработки текста:")
    for i in range(len(filters)):
        print(i + 1, '-', filters[i])
    number = str(input())
    if number != '1' and number != '2' and number != '3' and number != '4':
        print('Команда введена некорректно, попробуйте ввести заново.')
    else:
        number = int(number)
        filter = filters[number - 1]
        print(f'Вы выбрали фильтр - {filter.lower()}')

        print(f'Вы уверены, что хотите применить именно этот фильтр? (Да/Нет)')
        question = str(input())
        if question.lower() != 'да' and question.lower() != 'нет':
            print('Команда введена некорректно, попробуйте ввести заново.')
        elif question.lower() == "да":
            break

while True:
    print('Введите дальнейшее действие:\n'
          '1 - Описание фильтра\n'
          '2 - Изменение название фильтра\n'
          '3 - Применение фильтра\n'
          )
    action = str(input())

    if action == '1':
        print(filters_description[filters[number - 1]])
    elif action == '2':
        print("Введите новое название фильтра")
        new_name = input()
        filters[number - 1] = new_name
        filters_description[new_name] = filters_description[filter]
        filters_description.pop(filter)
        print(f'Название фильтра {filter.lower} успешно изменено на {new_name}')
    elif action == '3':
        break
    else:
        print('Команда введена некорректно, попробуйте ввести заново.')

print('Введите текст для обработки...')
text = str(input())
if filter == 'Сплошной текст':
    print(f"Результат: {solid_text(text)}")
elif filter == 'Прыгающий текст':
    print(f"Результат: {jumping_text(text)}")
elif filter == 'Перевёрнутый текст':
    print(f"Результат: {reverse_text(text)}")
elif filter == 'Жираф и цапли':
    print(f"Результат: {emoji_text(text)}")
