import numpy as np

def game_core_v3(number):
     
    # Идем путём банальной дихотомии
    count = 0
    predict = 50 # Начинаем с середины диапазона
    step = 25 # Первый шаг равен четверти диапазона
   

    while number != predict:
        
        count+=1
        if number > predict: 
            predict += step
        elif number < predict: 
            predict -= step
        
        #делим шаг пополам, с защитой от промахов
        step = (step + step % 2) // 2
    
    return(count)


'''  то же самое в рекурсивном варианте
     для единообразия вызова функции функцией-прогонщиком задаем дефолтные значения 
     стартовой версии и шага
     Правда, оно работает на 20% медленнее чем предыдущий вариант'''
def game_core_v4(number, predict=50, step=50):
    
    
    step = (step + step % 2) // 2
    
    if number > predict: 
        return 1 + game_core_v4(number, predict+step, step)
        
    if number < predict: 
        return 1 + game_core_v4(number, predict-step, step)
    
    return 0
        
        

        
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core_v3)
score_game(game_core_v4)
