num_count = int(input())
count = 0
for i in range(num_count):
  word = input()
  if len(word) > 1 :
    for j in range(0, len(word)-1):
      if word[j] == word[j+1]:
        pass
      elif word[j] in word[j+1:]:
        count += 1
        break
print(num_count - count)