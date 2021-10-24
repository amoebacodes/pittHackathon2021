# %%
from readability import Readability

text = open('testFile.txt', 'r').read()
r = Readability(text)

print(r.flesch_kincaid())
print(type(r.flesch_kincaid().score))
save = open("readabilityScore.txt", 'w')
save.write("scores: " + str(r.flesch_kincaid().score))
save.write("\n")
save.write("grade level: "+ str(r.flesch_kincaid().grade_level))
save.close()

# r.flesch()
# r.gunning_fog()
# r.coleman_liau()
# r.dale_chall()
# r.ari()
# r.linsear_write()
# r.smog()
# r.spache()
# %%
