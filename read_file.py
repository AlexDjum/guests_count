# file = open('guests.txt', 'rt') # read, text
#
# content = file.read()
# print(content)
#
# for line in file:
#    print(line)
#
# file.close()

guests_count = 0

with open('guests.txt', 'rt', encoding='utf-8') as file:
    for line in file:
        print(line)
        guests_count += 1
print(f'Количество гостей = {guests_count}')