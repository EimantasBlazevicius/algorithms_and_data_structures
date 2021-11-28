from collections import namedtuple, deque, ChainMap, Counter, OrderedDict

#namedtuple example
Kintamasis = namedtuple('kursai', 'kurso_pavadinimas,kalba')
kursas = Kintamasis('Algorithms', 'Python')
# print(kursas)


#deque example
pvz_listas = deque()
pvz_listas.append(1)
pvz_listas.append(2)
pvz_listas.appendleft(3)
pvz_listas.popleft()
# print(list(pvz_listas))

#chainmap example
b = {'music': 'bach', 'art': 'rembrandt'}
a = {'art': 'van gogh', 'opera': 'carmen'}
# print(list(ChainMap(a, b)))

#Counter example
c= Counter("aaabbbgikkktjjfhvkhebhlsrgbh")
print(c)
l = Counter([1,2,3,1,2,3,5,9,9,5,1,5])
print(l)
k = Counter(red=5, blue=2, yellow=1)
k2 = Counter(red=4, blue=1, yellow=1, orange=5)
print(list(k.elements()))
print(k.most_common(1))
k.update(k2)
print(k)

#Ordered dict
ordered_dictionary = OrderedDict

