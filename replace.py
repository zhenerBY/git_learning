phrase = ' Hello worlddddd 123 '
old = ' '
new = '!'
lenphrase = len(phrase)
lenold = len(old)
lenew = len(new)
phrase_list = list(phrase)
old_list = list(old)
new_list = list(new)
for c1 in range(lenphrase):
    control = []
    # print('c1=', c1)
    for c2 in range(lenold):
        if lenphrase >= c1 + c2 + lenold:
            if phrase_list[c1 + c2] == old_list[c2]:
                control.append(1)
                print(control)
        if sum(control) == lenold:
            print('Foun in: ', c1)
            phrase_list = phrase_list[:c1] + new_list + phrase_list[c1+lenold:]

print(phrase_list)

