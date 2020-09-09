# -*- coding: utf8 -*-

def fn_cmp(a, b):
    if a[0] > b[0]: return 1
    if a[0] < b[0]: return -1
    return 0

#-- создать дерево хаффмана по тексту -
def make_tree(text):

    se = set(text)
    ls = [(text.count(ch), ch) for ch in se]
    ls.sort()

    #-- построить двоичное дерево по этому списку
    while len(ls) >= 2:
        d = (ls[0] [0] + ls [1] [0], (ls[0] [1], ls[1] [1]))

        if ls[-1] [0]< d[0]:
            ls.append(d)
        else:
            for num in range(2, len (ls)) :
                if ls [num] [0]>= d[0]:
                    break
            ls.insert(num, d)
        ls.pop(0)
        ls.pop(0)
    return ls [0] [1]


#-- рекурсивно создать бинарный код листов элемента
def fn_cod(st, el):
    global ls_haf
    if type (el) == str:
        ls_haf.append((el, st))
        return
    fn_cod(st+"0", el[0])
    fn_cod(st+'1', el[1])
    return

#-- создать словарь хаффмана по тексту -
def make_dict(text):
    global ls_haf
    ls = make_tree(text)
    ls_haf=[]
    fn_cod('',ls)
    dc_haf= dict(ls_haf)
    return dc_haf

#-- сжать по хаффману
def compress(text, dc_haf):
    st_res = ''
    for ch in text:
        st_res = st_res + dc_haf[ch]
    return st_res

#-- decompress
def decompress(text_decompress, key_decompress):
    dc_decod = {key_decompress[key]:key for key in key_decompress}
    st_res = ''
    while len(text_decompress) > 0:
        num = 1
        while text_decompress[:num] not in dc_decod:
            num+=1
        st_res += dc_decod[text_decompress[:num]]
        text_decompress = text_decompress[num:]
    return st_res


#Функции зашифровки текста и создание ключа
def encryption_text(text):
    dc_haf = make_dict(text)
    compressed_text = compress(text, dc_haf)
    ass = int(compressed_text[0])
    if ass == 0:
        t = str(compressed_text)
        count = 0
        for i in t:
            count += 1
            if i == "1":
                break
        count = count - 1
        compressed_text2 = hex(int(compressed_text, 2))
        compressed_text2 = (f'{count}q{compressed_text2}')
    else:
        compressed_text2 = hex(int(compressed_text, 2))
    return compressed_text2
def encryption_key(text):
    dc_haf = make_dict(text)
    compressed_text = compress(text, dc_haf)
    return dc_haf

#Функция расшифровки текста
def huff_decompress(contents, key_decompress):
    wwe = int(contents[0])
    if wwe > 0:
        for y in range(wwe):
            contents = contents.replace(f'{wwe}q', '')
            print(contents)
            text_decompress = bin(int(contents, 16)).replace('0b', '')
            text_decompress = (f'0{text_decompress}')
    else:
        text_decompress = bin(int(contents, 16)).replace('0b', '')
    text_decompress = str(text_decompress)
    decompress_text = decompress(text_decompress, key_decompress)
    return decompress_text
