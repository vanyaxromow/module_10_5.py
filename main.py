import multiprocessing
import time


def read_info(name):
    all_data = []
    # st = time.time()
    with open(name) as file:
        for _ in file:
            str_ = file.readline()
            all_data.append(str_)
    # ft = time.time()
    # print(ft - st)


# read_info('file 4.txt')


if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        st = time.time()
        filenames = [f'./file {number}.txt' for number in range(1, 5)]
        pool.map(read_info, filenames)
        et = time.time()
        print(et - st)

# Линейный вызов
# 5.121822357177734 для 'file 1.txt'
# 6.0292580127716064 для 'file 2.txt'
# 5.222768068313599 для 'file 3.txt'
# 1.0703368186950684 для 'file 4.txt'

# # Многопроцессный
# 4.792028903961182 для 'file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt'
