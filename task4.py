st = set('it is set 1'.split())
print(st)
frozen_st = frozenset('it is frozen set 2'.split())
print(frozen_st)
union = st | frozen_st
print(union)
un = st.union(frozen_st)
print(un)
intersection = st & frozen_st
print(intersection)
#
d = st - frozen_st
print(d)
un.discard('set')
print(un)