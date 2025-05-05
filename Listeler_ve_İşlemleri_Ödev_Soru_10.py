projeler = {
    "ProjeX": {"durum": "aktif", "süre": 3},
    "ProjeY": {"durum": "tamamlandı", "süre": 6},
    "ProjeZ": {"durum": "aktif", "süre": 2}
}

aktif_projeler = [proje for proje, bilgiler in projeler.items() if bilgiler["durum"] == "aktif"]

print("Aktif projeler:", aktif_projeler)

