# sf_module_0
## Проект RDS_0 SkillFactory

***Постановка задачи***

Компьютер загадывает целое число от 1 до 100, и нам его нужно угадать. 

По условиям задачи нам недоступна никакая информация об исходном числе, кроме его принадлежности к заданному диапазону.
Все, что мы можем - сделать по какому-то принципу догадку и сравнить ее (больше, меньше, равно) с загаданным числом.

Требуется написать функцию, которая принимает на вход загаданное число, делает попытки угадать его, и, угадав, возвращает число сделанных попыток. Функция-отгадчик вызывается написанной заранее функцией-тестировщиком, которая запускает ее 1000 раз на случайных числах заданного диапазона и подсчитывает среднее количество попыток.

В функции-отгадчике должен быть реализован алгоритм, которому требуется в среднем минимальное количество попыток.

***Решение***

При данных ограничениях единственный способ угадывания - на основе сравнения догадки с истинным значением увеличить или уменьшить значение догадки на некоторый шаг.
В решении применен дихотомический поиск. В качестве отправной точки берем середину диапазона. 
В качестве первого шага приближения - четверть длины диапазона. На каждой очередной итерации шаг уменьшается вдвое. 

***Результат***

Примененный метод сходится в среднем за 5 попыток (считая стартовое значение за попытку, а собственно итераций цикла соответственно 4).
