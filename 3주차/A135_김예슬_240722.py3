input_num = int(input())
book_list = []
book_count = []
for i in range(input_num):
  book = input()
  if book in book_list:
    book_count[book_list.index(book)] += 1
  else:
    book_list.append(book)
    book_count.append(1)
max_book = max(book_count)
max_book_list = []
for i in range(len(book_list)):
  if book_count[i] == max_book:
    max_book_list.append(book_list[i])
max_book_list = sorted(max_book_list)
print(max_book_list[0])
