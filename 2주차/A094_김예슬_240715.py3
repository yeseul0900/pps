word = input()
croatia = ["dz=", "d-", "c=", "c-", "lj", "nj", "s=","z="]
for i in croatia:
  if i in word:
    word = word.replace(i, "*")
print(len(word))