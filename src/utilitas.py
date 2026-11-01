def format_nilai(nilai):
    """Membuat nilai tampil rapi tanpa .0 jika berupa bilangan bulat."""
    if nilai is None:
        return "-"
    if float(nilai).is_integer():
        return str(int(nilai))
    return f"{nilai:.2f}"
