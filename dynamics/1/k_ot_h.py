import math
import matplotlib.pyplot as plt

DATA_FILE_NAME = 'M_kr.txt'

M_PR1 = 0.868  # m_pr1 kg
R_PR1 = 0.032  # R_pr1 m
OMEGA = 418.8  # rad / s

def calc_M_pr(H, alfa):
    return H * R_PR1 * OMEGA ** 2 * math.sin(2 * alfa)

def calc_new_M_kr_arr(M_kr_arr, H):
    new_M_kr_arr = []

    # alfe = index в град
    for alfa, M_kr in enumerate(M_kr_arr):
        alfa_rad = math.radians(alfa)
        new_M_kr_arr.append(M_kr + calc_M_pr(H, alfa_rad))

    return new_M_kr_arr

def print_MAX_MIN_AVG(M_kr_arr):
    print("MAX:", max(M_kr_arr))
    print("MIN:", min(M_kr_arr))
    print("AVG:", sum(M_kr_arr) / len(M_kr_arr))

def calc_K(M_kr_arr):
    max_M_kr = max(M_kr_arr)
    min_M_kr = min(M_kr_arr)
    avg_M_kr = sum(M_kr_arr) / len(M_kr_arr)

    # return max_M_kr / avg_M_kr
    return (max_M_kr - min_M_kr) / avg_M_kr


if __name__ == "__main__":
    M_kr_arr = []
    with open(DATA_FILE_NAME) as f:
        for line in f:
            M_kr_arr.append(float(line.rstrip().replace(',','.')))

    # print("avg:", sum(M_kr_arr) / len(M_kr_arr))

    max_H = 0.5
    min_H = 0
    itterations = 2000
    delta = (max_H - min_H) / itterations

    arr_of_K = []
    arr_of_H = []

    currH = min_H

    while currH <= max_H:
        new_M_kr_arr = calc_new_M_kr_arr(M_kr_arr, currH)
        arr_of_H.append(currH)
        arr_of_K.append(calc_K(new_M_kr_arr))

        currH += delta

    fig = plt.figure()
    plt.plot(arr_of_H, arr_of_K)
    plt.suptitle('K(H)', fontsize=20)
    plt.xlabel('H', fontsize=16)
    plt.ylabel('K', fontsize=16)
    plt.show()

    h = 0.412
    optimized_m_kr_arr = calc_new_M_kr_arr(M_kr_arr, h)
    degrees_arr = []
    for alfa, _ in enumerate(optimized_m_kr_arr):
        degrees_arr.append(alfa)

    print("K =", calc_K(optimized_m_kr_arr))

    fig = plt.figure()
    plt.plot(degrees_arr, optimized_m_kr_arr)
    plt.suptitle('Mкр(alfa)', fontsize=20)
    plt.xlabel('alfa', fontsize=16)
    plt.ylabel('Mкр', fontsize=16)
    plt.show()



    f = open("new_M_kr.txt", "w")
    for M_kr in optimized_m_kr_arr:
        f.write(str(M_kr) + "\n")
    f.close()

    # new_M_kr_arr = calc_new_M_kr_arr(M_kr_arr, currH)


    # print_MAX_MIN_AVG(M_kr_arr)
    # print_MAX_MIN_AVG(new_M_kr_arr)
    # print(calc_K(M_kr_arr))
    # print(calc_K(new_M_kr_arr))
    # print()
    # print()
    # print()
    # print()
    # print()
    # for alfa, M_kr in enumerate(new_M_kr_arr):
    #     print(alfa, M_kr)

