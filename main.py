from linked_list.linked_list import LinkedList
from dictionary_openadressing.dictionary import Dictionary


if __name__ == "__main__":
    a = Dictionary()
    a['A'] = 'Apple'
    a['B'] = 'Banana'
    a['C'] = 'Cat'
    a['D'] = 'Dog'
    a['E'] = 'Egg'
    a['F'] = 'Frog'
    a['G'] = 'Goose'
    a['H'] = 'Hi'
    a['I'] = 'Ice'
    a['J'] = 'Juice'
    a['K'] = 'King'
    a['L'] = 'Lion'
    a['A2'] = 'Adam'
    a['B2'] = 'Bee'
    a['C2'] = 'Cow'
    a['D2'] = 'Duck'
    a['E2'] = 'Elephant'
    a['F2'] = 'Fun'
    a['G2'] = 'Girl'
    a['H2'] = 'Hello'
    a['I2'] = 'Ice-Cream'
    a['J2'] = 'Jump'
    a['K2'] = 'Kobe'
    a['L2'] = 'Lakers'
    print(a)
    tmp = 'J2'

    print(a)
    print("a[", tmp.__repr__(), "]:", a[tmp])
    del a[tmp]
    print("a[", tmp.__repr__(), "]:", a[tmp])
