def enkripsi(teks):
    teks_terenkripsi = ""
    for karakter in teks:
        if karakter in 'aeiou':
            if karakter == 'a':
                teks_terenkripsi += '1'
            elif karakter == 'e':
                teks_terenkripsi += '4'
            elif karakter == 'i':
                teks_terenkripsi += '2'
            elif karakter == 'o':
                teks_terenkripsi += '5'
            elif karakter == 'u':
                teks_terenkripsi += '3'
        elif karakter.isalpha():
            if karakter == 'z':
                teks_terenkripsi += 'a'
            else:
                teks_terenkripsi += chr(ord(karakter) + 1)
        else:
            teks_terenkripsi += karakter
    return teks_terenkripsi

def dekripsi(teks):
    teks_terdekripsi = ""
    for karakter in teks:
        if karakter.isdigit():
            if karakter == '1':
                teks_terdekripsi += 'a'
            elif karakter == '2':
                teks_terdekripsi += 'i'
            elif karakter == '3':
                teks_terdekripsi += 'u'
            elif karakter == '4':
                teks_terdekripsi += 'e'
            elif karakter == '5':
                teks_terdekripsi += 'o'
        elif karakter.isalpha():
            if karakter == 'a':
                teks_terdekripsi += 'z'
            else:
                teks_terdekripsi += chr(ord(karakter) - 1)
        else:
            teks_terdekripsi += karakter
    return teks_terdekripsi

teks_yang_ingin_dienkripsi = input("Masukkan string yang ingin dienkripsi: ")
teks_terenkripsi = enkripsi(teks_yang_ingin_dienkripsi)
print(f"String terenkripsi: {teks_terenkripsi}")

teks_yang_ingin_didekripsi = input("Masukkan string yang ingin didekripsi: ")
teks_terdekripsi = dekripsi(teks_yang_ingin_didekripsi)
print(f"String terdekripsi: {teks_terdekripsi}")