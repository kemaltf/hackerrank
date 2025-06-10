# Cara tradisional dengan loop
angka = [1, 2, 3, 4, 5]
kuadrat_loop = []
for x in angka:
    kuadrat_loop.append(x**2)

# Dengan list comprehension (lebih singkat)
kuadrat_comp = [x**2 for x in angka]
#                    ^^^^^^^^^^^^^ 
#                      Mulai dari sini: "untuk setiap x di dalam angka"
#               ^^^^
#               "ambil x, lalu pangkatkan 2"

# Hasilnya sama
print(kuadrat_loop)  # Output: [1, 4, 9, 16, 25]
print(kuadrat_comp)  # Output: [1, 4, 9, 16, 25]