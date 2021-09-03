phrase = ' Hello worlddddd 123 '
old = 'dddd'
new = '_'

lenphrase = len(phrase)
lenold = len(old)
lenew = len(new)
phrase_list = list(phrase)
old_list = list(old)
new_list = list(new)
phrase_list_new = []
continue1 = 0
for c1 in range(lenphrase):
    control = []
    if continue1 <= 0:
        for c2 in range(lenold):
            if lenphrase >= c1 + c2 + lenold:
                if phrase_list[c1 + c2] == old_list[c2]:
                    control.append(1)
            if sum(control) == lenold:
                if phrase_list_new:
                    phrase_list_new = phrase_list_new + phrase_list[c3 + lenold:c1] + new_list
                    c3 = c1
                    continue1 = lenold - 1
                else:
                    phrase_list_new = phrase_list[:c1] + new_list
                    print('false', c2, phrase_list_new)
                    c3 = c1
                    continue1 = lenold - 1
    else:
        continue1 -= 1

phrase_list_new = phrase_list_new + phrase_list[c3 + lenold:lenphrase]


print(''.join(phrase_list))
print(''.join(phrase_list_new))
