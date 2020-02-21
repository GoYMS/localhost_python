import collections

s='I love you'
print(isinstance(s,collections.Iterable))
print(isinstance(s,collections.Iterator))

s_iter=iter(s)
print(isinstance(s_iter,collections.Iterable))
print(isinstance(s_iter,collections.Iterator))
