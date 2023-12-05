def weight_conversion():
    berat = int(input("Massukan berat anda > "))
    satuan = input("Dalam satuan aoa beray yang anda masukkan? (K untuk KG, L untuk LBS) > ")
    
    if satuan.lower() == 'l':
        print(f"berat anda dikonversi menjadi kilogram adalah {round(berat*0.453592)} kg")
    elif satuan.lower() == 'k':
        print(f"berat anda dikonversi menjadi pons adalah {round(berat*2.20462)} lbs")