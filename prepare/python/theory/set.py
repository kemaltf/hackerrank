if __name__ == '__main__':
    students = {}  # Buat dictionary kosong
    students = {'Alice': 85.5, 'Bob': 85.5, 'Fufufafa': 78.5,'Charlie': 78.5, 'David': 85.5}

    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     students[name] = score
    
    # Temukan nilai unik dan urutkan
    # set(students.values()) - Mengkonversi nilai-nilai tersebut menjadi set, yang secara otomatis menghilangkan duplikat. Hasilnya menjadi: {37.2, 37.21, 39, 41}

    print(sorted(set(students.values()),))
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