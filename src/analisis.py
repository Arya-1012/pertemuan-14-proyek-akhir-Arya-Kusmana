def hitung_statistik(data):
    """Menghitung jumlah, rata-rata, minimum, dan maksimum nilai."""
    if not data:
        return {
            "jumlah": 0,
            "rata_rata": 0,
            "minimum": None,
            "maksimum": None,
        }

    nilai = [item["nilai"] for item in data]
    return {
        "jumlah": len(nilai),
        "rata_rata": sum(nilai) / len(nilai),
        "minimum": min(nilai),
        "maksimum": max(nilai),
    }


def hitung_ketuntasan(data, kkm):
    """Menghitung jumlah siswa tuntas dan belum tuntas."""
    tuntas = sum(1 for item in data if item["nilai"] >= kkm)
    return {
        "tuntas": tuntas,
        "belum_tuntas": len(data) - tuntas,
    }
