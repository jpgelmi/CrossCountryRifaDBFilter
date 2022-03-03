f_in = open("./assets/IN/data.csv", "r")
f_out = open("./assets/OUT/rifa_limpia", "a")

for i in f_in:
    nombre = f'{i.split(",")[2].strip()} {i.split(",")[3].strip()}'
    numero_rifas = int(i.split(",")[5].strip())
    for i in range(numero_rifas): f_out.write(f"{nombre} \n")

