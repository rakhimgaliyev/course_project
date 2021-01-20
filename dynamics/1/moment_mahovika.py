delta = 0.02
delta_alfa = 1
omega = 4000 / 60
DATA_FILE_NAME = 'new_M_kr.txt'

if __name__ == "__main__":
    M_kr_arr = []
    with open(DATA_FILE_NAME) as f:
        for line in f:
            M_kr_arr.append(float(line.rstrip().replace(',','.')))

    M_sr = sum(M_kr_arr) / len(M_kr_arr)

    F = 0

    for M_kr in M_kr_arr:
        F = (M_kr - M_sr) * delta_alfa

    J_mah = abs(F / (delta * omega**2))
    D = 0.366 * J_mah ** (1/5)
    b = 0.2 * D
    m = 1230 * D**3
    print("момент маховика, кг*м^2:", J_mah)
    print("диаметр маховика, м:", D)
    print("ширина маховика, м:", b)
    print("масса маховика, кг:", m)