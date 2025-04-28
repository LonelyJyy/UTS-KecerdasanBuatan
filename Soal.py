# soal1.py

def diagnose(gejala):
    diagnosis = []
    
    if "daun menguning" in gejala:
        diagnosis.append("Kemungkinan ada Kutu Daun")
    if "bercak hitam" in gejala:
        diagnosis.append("Kemungkinan ada Jamur Daun")
    if "daun berlubang" in gejala:
        diagnosis.append("Kemungkinan ada Ulat Daun")
    if "tanaman layu" in gejala:
        diagnosis.append("Kemungkinan ada Nematoda Akar")
    if "daun menguning" in gejala and "daun berlubang" in gejala:
        diagnosis.append("Serangan parah oleh Ulat Daun")

    if not diagnosis:
        diagnosis.append("Tidak dapat menentukan hama berdasarkan gejala yang diberikan.")
    
    return diagnosis

# Contoh penggunaan
if __name__ == "__main__":
    print("Masukkan gejala tanaman (pisahkan dengan koma):")
    input_gejala = input().lower().split(",")
    input_gejala = [gejala.strip() for gejala in input_gejala]
    
    hasil = diagnose(input_gejala)
    print("\nDiagnosis:")
    for h in hasil:
        print(f"- {h}")

