import numpy as np


def game_core_v3(number):

    '''using trivial diсhotomy search in a loop'''
    
    # just in case we might change the range of possible guesses
    lo = 1
    hi = 100
    
    count = 1
    
    step = ((hi-lo) + (hi-lo)%2) // 2  # initally it is half length of the range
    predict = lo+step  # and we start checking right from the middle of the range
    
    while number != predict:
        
        #with each iteration step is diminished in half
        
        step = (step + step % 2) // 2
        if number > predict: 
            predict += step

        elif number < predict: 
            predict -= step
         
        count+=1

    return(count)





 #the recursive version
 #looks much better, but is 20% slower
 #and we have to hard preset the predict and step values
 #so it could be called by the testing function seamlessly
 #but I've wrote this just to check if it will be significantly slower    


def game_core_v4(number, predict=50, step=50):

     '''using trivial diсhotomy search recursively'''
        
    step = (step + step % 2) // 2
  
    if number > predict: 
        return 1 + game_core_v4(number, predict+step, step)
     

    if number < predict: 
        return 1 + game_core_v4(number, predict-step, step)
   
    return 1



        

def score_game(game_core):

    '''Запускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число'''

    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,100, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")

    return(score)



score_game(game_core_v3)
score_game(game_core_v4)


