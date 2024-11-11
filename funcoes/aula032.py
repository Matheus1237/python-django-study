from itertools import count

# count é um iterador sem fim
# similar ao range, mas não é declarado onde acaba

c1 = count()
print(next(c1))
print(next(c1))
print(next(c1))
