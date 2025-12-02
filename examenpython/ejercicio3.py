r = float(input("Renta: "))

irpf = 0

if r <= 12450:
    irpf = r * 0.19
else:
    irpf = 12450 * 0.19

if r > 12450:
    if r <= 20200:
        irpf += (r - 12450) * 0.24
    else:
        irpf += (20200 - 12450) * 0.24

if r > 20200:
    if r <= 35200:
        irpf += (r - 20200) * 0.30
    else:
        irpf += (35200 - 20200) * 0.30

if r > 35200:
    irpf += (r - 35200) * 0.37

print("IRPF:", irpf)
