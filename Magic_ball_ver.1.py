import random
positive = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом']
hesitantly = ['Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да']
neutral = ['Пока неясно, попробуй снова', '	Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять']
negative = ['Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']
answer = positive + hesitantly + neutral + negative
print ('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input ('Как тебя зовут? Напиши свое имя: ')
print (f'Привет, {name}!!!')

def choice():
    question = input('Если есть сомнения, я смогу их развеять. Введи свой вопрос: ')
    print(random.choice(answer))

choice()

while True:
    povtor = input('Хотите задать еще один вопрос: да/нет?' )
    if povtor == "да" or povtor == "Да" or povtor == "ДА":
        choice()
    elif povtor == "нет" or povtor == "Нет" or povtor == "НЕТ":
        print('Возвращайся если возникнут вопросы!')
        break
    else:
        print('Ты подбуханный что ли, читай внимательно и пиши только "да" или "нет"')
        continue
