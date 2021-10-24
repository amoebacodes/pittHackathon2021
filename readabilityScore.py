# %%
from readability import Readability

text = open('testFile.txt', 'r').read()
r = Readability(text)

print(r.flesch_kincaid())
