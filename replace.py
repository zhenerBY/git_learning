phrase = 'Hello worlddddd 123'
old ='hhhh'
new = '11'
lenphrase = len(phrase)
lenold = len(old)
lenew = len(new)
phrase_list = list(phrase)
old_list = list(old)
new_list = list(new)
control = False
for c1 in range(lenphrase):
    print('c1=', c1)
    for c2 in range(lenold):
        print('c2=', c2)
                if lenphrase + lenold <= c1 + c2:
            if phrase_list[c1 + c2] != old_list[c2]:
                control = False
print(control)
