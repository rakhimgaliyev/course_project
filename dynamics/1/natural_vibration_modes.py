import math
import matplotlib.pyplot as plt


def get_arr_of_L_pr():
    return [
        0.171, # 1
        0.171, # 2
        0.171, # 3
        0.025, # 4
        1.157, # 5
        2.087, # 6
        10.993, # 7
        0.039, # 8
        0.113, # 9
        0.676, # 10
        0.844, # 11
        12.5, # 12
        3.918, # 13
        3.364, # 14
        3.918, # 15
        482, # 16
        3.364, # 17
        482, # 18
    ]

# в метрах
def get_x_axis_data_arr():
    array_of_L_pr = get_arr_of_L_pr()

    res = []
    for l_pr in array_of_L_pr:
        if len(res) > 0:
            res.append(l_pr + res[-1])
        else:
            res.append(l_pr)

    return res

def generate_x_axis(array_of_L_pr):
    res = []
    for l_pr in array_of_L_pr:
        if len(res) > 0:
            res.append(l_pr + res[-1])
        else:
            res.append(l_pr)

    return res


# главная ветка
def get_first_arr_of_L_pr():
    array_of_L_pr = get_arr_of_L_pr()
    return generate_x_axis(array_of_L_pr[:8] + array_of_L_pr[11:])

# побочная ветка
def get_second_arr_of_L_pr():
    array_of_L_pr = get_arr_of_L_pr()
    return generate_x_axis(array_of_L_pr[:7] + array_of_L_pr[8:11])


# главная ветка
def get_first_arr_of_data(data):
    return data[:8] + data[11:]

# побочная ветка
def get_second_arr_of_data(data):
    return data[:7] + data[8:11]


if __name__ == "__main__":
    x_axis_data = get_x_axis_data_arr()

    i_2_data = [
        1, # 1
        0.9965, # 2
        0.9896, # 3
        0.9792, # 4
        -0.1629, # 5
        -0.1754, # 6
        -0.1982, # 7
        -0.3145, # 8
        -0.3147, # 9
        -0.3151, # 10
        -0.3155, # 11
        -0.3149, # 12
        -0.4242, # 13
        -0.4215, # 14
        -0.4578, # 15
        -0.4189, # 16
        -0.4708, # 17
        -0.0007445, # 18
    ]

    i_3_data = [
        1, # 1
        0.9944, # 2
        0.9834, # 3
        0.9669, # 4
        -0.8451, # 5
        -0.3318, # 6
        0.6059, # 7
        5.510, # 8
        5.514, # 9
        5.526, # 10
        5.535, # 11
        5.525, # 12
        10.45, # 13
        10.40, # 14
        11.92, # 15
        10.34, # 16
        12.53, # 17
        -0.01199, # 18
    ]

    i_4_data = [
        1, # 1
        0.9237, # 2
        0.7775, # 3
        0.5724, # 4
        -20.06, # 5
        192.9, # 6
        579.4, # 7
        2406, # 8
        2432, # 9
        2510, # 10
        2568, # 11
        2402, # 12
        535.1, # 13
        552.7, # 14
        -158.9, # 15
        558.3, # 16
        -634.6, # 17
        0.002913, # 18
    ]

    i_5_data = [
        1, # 1
        0.8033, # 2
        0.4499, # 3
        0.00864, # 4
        -36.77, # 5
        974.9, # 6
        2790, # 7
        9817, # 8
        10110, # 9
        11000, # 10
        11680, # 11
        9725, # 12
        -25520, # 13
        -28230, # 14
        -22630, # 15
        -29320, # 16
        23990, # 17
        0.07898, # 18
    ]

    i_6_data = [
        1, # 1
        0.4637, # 2
        -0.3192, # 3
        -0.9324, # 4
        -10.66, # 5
        790.9, # 6
        2183, # 7
        4165, # 8
        4583, # 9
        6014, # 10
        7152, # 11
        4009, # 12
        -51230, # 13
        -73260, # 14
        13870, # 15
        -82600, # 16
        -3129, # 17
        0.4665, # 18
    ]

    i_7_data = [
        1, # 1
        0.4063, # 2
        -0.4267, # 3
        -1.008, # 4
        0.0009740, # 5
        0.001386, # 6
        0.002, # 7
        -0.0001773, # 8
        -0.000198, # 9
        -0.00027, # 10
        -0.0003278, # 11
        -0.0001771, # 12
        0.0002093, # 13
        0.0003091, # 14
        -0.00004701, # 15
        0.0003536, # 16
        0.000009634, # 17
        -0.000000001783, # 18
    ]

    i_8_data = [
        1, # 1
        0.0492, # 2
        -0.0948, # 3
        -1.051, # 4
        72.71, # 5
        -9618, # 6
        -25770, # 7
        874.7, # 8
        1116, # 9
        2097, # 10
        2922, # 11
        879.2, # 12
        -143.7, # 13
        -319.3, # 14
        16.56, # 15
        -402, # 16
        -1.967, # 17
        0.001238, # 18
    ]

    i_9_data = [
        1, # 1
        -1.015, # 2
        -1.001, # 3
        1.014, # 4
        -0.0002904, # 5
        -0.0001254, # 6
        0.0002188, # 7
        0.00002026, # 8
        0.00001508, # 9
        -0.00002921, # 10
        -0.00007267, # 11
        0.00002103, # 12
        0.0001383, # 13
        -0.0003029, # 14
        -0.00000657, # 15
        -0.0005451, # 16
        0.0000003462, # 17
        0.000000000788, # 18
    ]

    i_10_data = [
        1, # 1
        -1.019, # 2
        -0.9971, # 3
        1.022, # 4
        -1.311, # 5
        370, # 6
        921.5, # 7
        -4643, # 8
        3467, # 9
        6632, # 10
        16550, # 11
        -4996, # 12
        -87520, # 13
        189900, # 14
        4150, # 15
        342300, # 16
        -218.2, # 17
        -0.4938, # 18
    ]

    i_11_data = [
        1, # 1
        -1.411, # 2
        -0.4477, # 3
        1.586, # 4
        -144.5, # 5
        48720, # 6
        118000, # 7
        -812100, # 8
        -731500, # 9
        521600, # 10
        1833000, # 11
        -827600, # 12
        130300, # 13
        -136200, # 14
        -5085, # 15
        -291500, # 16
        222.1, # 17
        0.3522, # 18
    ]

    i_12_data = [
        1, # 1
        -2.441, # 2
        2.449, # 3
        -1.020, # 4
        0.0001709, # 5
        0.0001112, # 6
        -0.0000624, # 7
        0.00000255, # 8
        0.000002798, # 9
        0.00000007114, # 10
        -0.00000338, # 11
        0.000002626, # 12
        -0.0000001621, # 13
        0.00000004434, # 14
        0.000000004319, # 15
        0.0000001875, # 16
        -0.0000000001304, # 17
        -0.0000000000001587, # 18
    ]

    plt.plot(get_second_arr_of_L_pr(), get_second_arr_of_data(i_2_data))
    plt.plot(get_first_arr_of_L_pr(), get_first_arr_of_data(i_2_data), label='i=2')

    plt.plot(get_second_arr_of_L_pr(), get_second_arr_of_data(i_3_data))
    plt.plot(get_first_arr_of_L_pr(), get_first_arr_of_data(i_3_data), label='i=3')

    plt.plot(get_second_arr_of_L_pr(), get_second_arr_of_data(i_4_data))
    plt.plot(get_first_arr_of_L_pr(), get_first_arr_of_data(i_4_data), label='i=4')

    plt.plot(get_second_arr_of_L_pr(), get_second_arr_of_data(i_5_data))
    plt.plot(get_first_arr_of_L_pr(), get_first_arr_of_data(i_5_data), label='i=5')

    plt.plot(get_second_arr_of_L_pr(), get_second_arr_of_data(i_6_data))
    plt.plot(get_first_arr_of_L_pr(), get_first_arr_of_data(i_6_data), label='i=6')

    plt.plot(get_second_arr_of_L_pr(), get_second_arr_of_data(i_7_data))
    plt.plot(get_first_arr_of_L_pr(), get_first_arr_of_data(i_7_data), label='i=7')

    plt.plot(get_second_arr_of_L_pr(), get_second_arr_of_data(i_8_data))
    plt.plot(get_first_arr_of_L_pr(), get_first_arr_of_data(i_8_data), label='i=8')

    plt.plot(get_second_arr_of_L_pr(), get_second_arr_of_data(i_9_data))
    plt.plot(get_first_arr_of_L_pr(), get_first_arr_of_data(i_9_data), label='i=9')

    plt.plot(get_second_arr_of_L_pr(), get_second_arr_of_data(i_10_data))
    plt.plot(get_first_arr_of_L_pr(), get_first_arr_of_data(i_10_data), label='i=10')

    plt.plot(get_second_arr_of_L_pr(), get_second_arr_of_data(i_11_data))
    plt.plot(get_first_arr_of_L_pr(), get_first_arr_of_data(i_11_data), label='i=11')

    plt.plot(get_second_arr_of_L_pr(), get_second_arr_of_data(i_12_data))
    plt.plot(get_first_arr_of_L_pr(), get_first_arr_of_data(i_12_data), label='i=12')

    plt.legend(loc="upper right")

    plt.show()