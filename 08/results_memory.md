count = 100_000

## point.name='Default Points class':
```Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    42     16.8 MiB     16.8 MiB           1   @profile  # delete for check timings
    43                                         def create_points(point, count):
    44     30.0 MiB     13.2 MiB      100003       x_values = [Helper([i]) for i in range(count)]
    45     43.2 MiB     13.2 MiB      100003       y_values = [Helper([i + 1]) for i in range(count)]
    46     56.4 MiB     13.2 MiB      100003       z_values = [Helper([i + 2]) for i in range(count)]
    47
    48     72.6 MiB     16.2 MiB      100003       points = [point(x, y, z) for x, y, z in zip(x_values, y_values, z_values)]
    49     72.6 MiB      0.0 MiB      100001       for i in points:
    50     72.6 MiB      0.0 MiB      100000           i.x = 1
    51     72.6 MiB      0.0 MiB      100000           i.y = 2
    52     72.6 MiB      0.0 MiB      100000           i.z = 3
```

## point.name='Slots Points class':
```Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    42     16.7 MiB     16.7 MiB           1   @profile  # delete for check timings
    43                                         def create_points(point, count):
    44     29.9 MiB     13.2 MiB      100003       x_values = [Helper([i]) for i in range(count)]
    45     43.2 MiB     13.3 MiB      100003       y_values = [Helper([i + 1]) for i in range(count)]
    46     56.5 MiB     13.2 MiB      100003       z_values = [Helper([i + 2]) for i in range(count)]
    47                                         
    48     63.4 MiB      7.0 MiB      100003       points = [point(x, y, z) for x, y, z in zip(x_values, y_values, z_values)]
    49     63.4 MiB      0.0 MiB      100001       for i in points:
    50     63.4 MiB      0.0 MiB      100000           i.x = 1
    51     63.4 MiB      0.0 MiB      100000           i.y = 2
    52     63.4 MiB      0.0 MiB      100000           i.z = 3
```

## point.name='Weakrefs Points class':
```Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    42     16.8 MiB     16.8 MiB           1   @profile  # delete for check timings
    43                                         def create_points(point, count):
    44     30.0 MiB     13.2 MiB      100003       x_values = [Helper([i]) for i in range(count)]
    45     43.6 MiB     13.6 MiB      100003       y_values = [Helper([i + 1]) for i in range(count)]
    46     56.9 MiB     13.3 MiB      100003       z_values = [Helper([i + 2]) for i in range(count)]
    47                                         
    48     96.5 MiB     39.6 MiB      100003       points = [point(x, y, z) for x, y, z in zip(x_values, y_values, z_values)]
    49     96.5 MiB      0.0 MiB      100001       for i in points:
    50     96.5 MiB      0.0 MiB      100000           i.x = 1
    51     96.5 MiB      0.0 MiB      100000           i.y = 2
    52     96.5 MiB      0.0 MiB      100000           i.z = 3
```

## Выводы
Результаты показывают, что использование слотов позволяет значительно сократить объем потребляемой памяти
по сравнению с обычным классом за счет уменьшения количества атрибутов объектов.
Однако использование слабых ссылок приводит к увеличению объема потребляемой памяти,
так как создается дополнительный объект слабой ссылки.
