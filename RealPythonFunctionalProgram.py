import collections
from pprint import pprint
import time
import os
import multiprocessing

Scientist = collections.namedtuple('Scientist',[
    'name',
    'field',
    'born',
    'nobel',
    ])
scientists = (
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
    Scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
    Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', born=1951, nobel=False),
    )

#fs = filter(lambda x: x.nobel is True, scientists)
#next(fs)

#pprint(tuple(filter(lambda x: x.nobel is True, scientists)))

#pprint(tuple(filter(lambda x: x.field == 'physics', scientists)))

#for x in scientists:
 #       if x.nobel is True:
  #          print(x)

#def nobel_filter(x):
 #   return x.nobel is True

#pprint(tuple(filter(nobel_filter, scientists)))

#[x for x in scientists if x.nobel is True]
#pprint([x for x in scientists if x.nobel is True]
#)
#print(tuple(x for x in scientists if x.nobel is True))
names_and_ages = tuple(map(
        lambda x: {'name': x.name, 'age': 2020 - x.born},
        scientists
        ))
#pprint(names_and_ages)
#pprint([{'name':x.name, 'age' : 2020- x.born}
 #for x in scientists])
from functools import reduce
total_age = reduce(
        lambda acc, val: acc + val['age'],
        names_and_ages,
        0)
#print(total_age)
def reducer(acc, val):
        acc[val.field].append(val.name)
        return acc

scientists_by_field = reduce(
            reducer,
            scientists,
            {'math': [], 'physics':[], 'chemistry':[], 'astronomy':[]})
#pprint(scientists_by_field)

dd = collections.defaultdict(list)
scientists_by_field=reduce(
        reducer,
        scientists,
        dd
        )
#pprint(scientists_by_field)
def transform(x):
        print(f'{os.getpid()} working record {x.name}')
        time.sleep(1)
        result = {'name': x.name, 'age':2020 - x.born}
        print(f'{os.getpid()} Done processing record {x.name}')
        return result

start = time.time()

pool = multiprocessing.Pool(processes = len(scientists))
result = pool.map(transform, scientists)

#result = tuple(map(
 #   transform,
  #  scientists
   # ))
end = time.time()

print(f'\nTime to complete: {end - start:.2f}s\n')
pprint(result)



