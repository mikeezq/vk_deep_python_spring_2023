count = 1_000_000

## point.name='Default Points class':
         

```1000005 function calls in 3.211 seconds
   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.573    0.573    1.245    1.245 08/points.py:48(<listcomp>)
        1    0.722    0.722    0.722    0.722 08/points.py:46(<listcomp>)
  1000000    0.671    0.000    0.671    0.000 08/points.py:15(__init__)
        1    0.660    0.660    0.660    0.660 08/points.py:45(<listcomp>)
        1    0.585    0.585    0.585    0.585 08/points.py:44(<listcomp>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```


## point.name='Slots Points class':

```1000005 function calls in 2.668 seconds
   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.616    0.616    0.765    0.765 08/points.py:48(<listcomp>)
        1    0.678    0.678    0.678    0.678 08/points.py:46(<listcomp>)
        1    0.638    0.638    0.638    0.638 08/points.py:45(<listcomp>)
        1    0.587    0.587    0.587    0.587 08/points.py:44(<listcomp>)
  1000000    0.149    0.000    0.149    0.000 08/points.py:25(__init__)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```


## point.name='Weakrefs Points class':

```1000005 function calls in 4.431 seconds
   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.312    0.312    2.544    2.544 08/points.py:48(<listcomp>)
  1000000    2.232    0.000    2.232    0.000 08/points.py:34(__init__)
        1    0.679    0.679    0.679    0.679 08/points.py:46(<listcomp>)
        1    0.633    0.633    0.633    0.633 08/points.py:45(<listcomp>)
        1    0.576    0.576    0.576    0.576 08/points.py:44(<listcomp>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

## Выводы
Реализация класса Points с использованием слотов оказалась наиболее эффективной в плане производительности.
Она позволяет избежать накладных расходов на словарь dict и тем самым уменьшить потребление памяти, и ускорить выполнение операций.

Реализация класса Points с использованием обычных ссылок оказалась второй по эффективности.

Реализация класса Points с использованием слабых ссылок оказалась наименее эффективной в плане производительности.
Потому что слабые ссылки создают дополнительные затраты на работу с объектами,
а также они имеют более ограниченный функционал, что приводит к более сложному коду. В данном случае это зависит от реализации и
слабые ссылки могут быть полезны в других случаях

