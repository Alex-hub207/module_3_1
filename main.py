calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string_):
    count_calls()
    up = string_.upper()
    low = string_.lower()
    return (len(string_), up, low)


def is_contains(string_, list_to_search):
    count_calls()
    is_included_ = False
    for i in list_to_search:
        if string_.upper() == i.upper():
            is_included_ = True
    return (is_included_)


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)

# Мне не очеь нравится моя пеализация is_contains.
# Можете что-то посоветовать?