doc = input()
search = input()
length = len(search)
count = 0
i = 0

while(1):
  if i == len(doc):
    break
  if doc[i:i+length] == search:
    count += 1
    i += length
  else: i += 1
print(count)