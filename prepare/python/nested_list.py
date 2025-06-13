if __name__ == '__main__':
    students = {}  # Buat dictionary kosong
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students[name] = score
    
    # Temukan nilai unik dan urutkan
    scores = sorted(set(students.values()))
    
    # Ambil nilai kedua terendah
    second_lowest = scores[1]
    
    # Temukan semua siswa dengan nilai kedua terendah
    result = [name for name, score in students.items() if score == second_lowest]
    
    # Urutkan nama secara alfabetis
    result.sort()
    
    # Cetak setiap nama pada baris baru
    for name in result:
        print(name)