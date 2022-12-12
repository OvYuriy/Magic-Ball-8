from random import choice
answers = ['Бесспорно', 'Мне кажется - да', 'Пока неясно, попробуй снова', 'Даже не думай', 'Предрешено', 'Вероятнее всего',
'Спроси позже', 'Мой ответ - нет', 'Никаких сомнений', 'Хорошие перспективы', 'Лучше не рассказывать', 'По моим данным - нет',
'Определённо да', 'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие', 'Можешь быть уверен в этом',
'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']


def check(stop_question):
    flag = True
    while flag:
        if stop_question == 'да':
            return True
        elif stop_question == 'нет':
            return False
        else:
            stop_question = input('Хочешь задать еще один вопрос? ').lower()


print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Как тебя зовут? ')
print('Привет,', name)

flag = True
while flag:
    question = input('Задавай свой вопрос: ')
    if question == '' or question == ' ':
        question = input('Задавай свой вопрос: ')
    else:
        print(choice(answers))
        stop_question = input('Хочешь задать еще один вопрос? ').lower()
        flag = check(stop_question)
input('Возвращайся, если возникнут вопросы! ')
            