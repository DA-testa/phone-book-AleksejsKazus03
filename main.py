# python3
# Aleksejs_Kazus_221RDB105
n = int(input().strip())
phone_book = {}

for i in range(n):
    query = input().strip().split()
    if query[0] == 'add':
        phone_book[query[1]] = query[2]
    elif query[0] == 'del':
        if query[1] in phone_book:
            del phone_book[query[1]]
    elif query[0] == 'find':
        if query[1] in phone_book:
            print(phone_book[query[1]])
        else:
            print('not found')

