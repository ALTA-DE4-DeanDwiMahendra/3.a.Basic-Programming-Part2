# Input harga awal dari pengguna
harga_awal = 370000
# Input persentase diskon dari pengguna
persentase_diskon = 15    
# Menghitung harga diskon
harga_diskon = (persentase_diskon / 100) * harga_awal   
# Menghitung harga akhir setelah diskon
harga_akhir = harga_awal - harga_diskon    
# Mencetak hasil perhitungan harga akhir
print(f"Harga awal: Rp{harga_awal:.2f}")
print(f"Diskon: {persentase_diskon}%")
print(f"Harga diskon: Rp{harga_diskon:.2f}")
print(f"Harga akhir setelah diskon: Rp{harga_akhir:.2f}")