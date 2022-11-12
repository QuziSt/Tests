geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]


def get_only_unique_ids() -> list:
    nums = []
    for user_id, numbers in ids.items():
        for number in numbers:
            nums.append(number)
    nums_new = list(dict.fromkeys(nums))
    return nums_new


def get_rus_visits_only() -> list:
    all_russian_visits = []
    for visit in geo_logs:
        for visit_country in visit.values():
            if 'Россия' in visit_country:
                for keys, values in visit.items():
                    result = f'{keys} : {values[0]}, {values[1]}'
                    all_russian_visits.append(result)

    return all_russian_visits


def get_queries_amount() -> str:
    words_amount = {}

    for query in queries:
        words_amount.setdefault(len(query.split()), 1)
        words_amount[len(query.split())] += 1

    res_amount = sum(words_amount.values())
    result = ''
    for word, count in words_amount.items():
        percent = count / res_amount * 100
        result += f'Запросы с кол-вом слов {word} встречаются в {round(percent, 2)}% запросов.\n'
    return result


if '__main__' == __name__:
    for visit_ in get_rus_visits_only():
        print(visit_)
    print(get_only_unique_ids())
