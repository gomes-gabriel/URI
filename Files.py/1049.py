word1 = input()
word2 = input()
word3 = input()

if word1 == 'vertebrado':
    if word2 == 'ave':
        if word3 == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    elif word3 == 'onivoro':
        print('homem')
    else:
        print('vaca')
elif word2 == 'inseto':
    if word3 == 'hematofago':
        print('pulga')
    else:
        print('lagarta')
elif word3 == 'hematofago':
    print('sanguessuga')
else:
    print('minhoca')
