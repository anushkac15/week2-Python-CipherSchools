# list vs strings

# strings are immutable
s = 'string'
s.title()
print(s)

s = 'string'
t = s.title()
print(t)

# lists are mutable
l = ['word1', 'word2', 'word3']
l.pop()
print(l)

l = ['word1', 'word2', 'word3']
l.append('word3')
print(l)