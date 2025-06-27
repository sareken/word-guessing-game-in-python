import random

while True:
    kelime_listesi = ["system", "data", "algorithm", "such", "base", "node", "model", "case", "program", "information",
                      "set", "code", "function", "process", "application", "software", "class", "point", "type",
                      "network",
                      "tree", "object", "element", "input", "operation", "level", "memory", "table", "order", "file",
                      "variable", "language", "write", "list", "structure", "compute", "sequence", "computer", "bit",
                      "probability", "machine", "array", "page", "error", "step", "search", "most", "path", "graph",
                      "web",
                      "length", "several", "security", "proof", "access", "obtain", "matrix", "task", "image", "form",
                      "return", "interface", "resource", "address", "implementation", "loop", "first", "read",
                      "location",
                      "hardware", "behavior", "programming", "field", "key", "parameter", "distribution", "definition",
                      "instance", "interaction", "internet", "representation", "edge", "stack", "return", "procedure",
                      "link", "output", "block", "domain", "store", "call", "device", "server", "static", "dataset",
                      "detection", "write", "execute", "least", "key"]
    kelime = random.choice(kelime_listesi)
    print(kelime)
    uzunluk = len(kelime)
    turkce_karakter = 'öçşığü'
    sesli_harf = 'aeiou'
    sessiz_harf = 'bcdgfhjklmnprstvyzwq'
    toplam_puan = 0
    arananKelime = []
    for i in range(uzunluk):
        arananKelime += ['_']
    print("Secilen kelime {} harften olusmaktadir ->".format(uzunluk) ,uzunluk*' _')
    if uzunluk % 2 == 1:
        yanlis_tahmin = (uzunluk + 1) / 2
    else:
        yanlis_tahmin = uzunluk / 2
    while yanlis_tahmin > 0:
        kontrol = 0
        sonuc = ''
        tahmin = input("lutfen bir harf giriniz : ").lower()
        for i in range(uzunluk):
            while tahmin in turkce_karakter:
                tahmin = input("Lutfen tekrar harf giriniz : ").lower()
            if kelime[i] == tahmin:
                kontrol = 1
                arananKelime[i] = tahmin
                if tahmin in sesli_harf:
                    toplam_puan += 3
                elif tahmin in sessiz_harf:
                    toplam_puan += 2
        if kontrol == 0:
            toplam_puan -= 4
            yanlis_tahmin -= 1
        for i in arananKelime:
            sonuc += i + ''
        print("--------------------------------")
        print("Kalan hak:{}".format(yanlis_tahmin), "Puan:{}".format(toplam_puan))
        print("Kelimeniz: {}".format(sonuc))
        print("--------------------------------")
        if sonuc == kelime:
            secim = int(input("TEBRİKLER. KAZANDİNİZ LUTFEN YAPMAK İSTEDİGİNİZ İSLEMİ SECİN ( 1 , 2 ): \n"
                              "[1] - YENİ KELİMEYE GECME \n"
                              "[2] - CIKIS \n"))
            if secim == 1:
                break
            else :
                yanlis_tahmin=-1
    if yanlis_tahmin==-1:
        print("CİKİS YAPTİNİZ!")
        break
    if yanlis_tahmin == 0:
        print("OYUNU KAYBETTİNİZ!")
        break
