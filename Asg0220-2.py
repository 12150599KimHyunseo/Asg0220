import random


def sequence_search(ary, find_data):
    pos = -1
    global count
    for i in range(len(ary)):
        count = count + 1
        if ary[i] == find_data:
            pos = i
            break
    return pos


def binary_search(ary, find_data):
    start = 0
    end = len(ary) - 1
    global count
    while start <= end:
        count = count + 1
        mid = (start + end) // 2
        if find_data == ary[mid]:
            return mid
        elif find_data > ary[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1


count = 0
data_ary = []
sorted_ary = []
find_data = 6951

if __name__ == "__main__":
    data_ary = [random.randint(0, 999999) for _ in range(1000000)]
    find_ary = data_ary.append(find_data)
    sorted_ary = sorted(data_ary)
    print("비정렬 배열(100만개) --> ", data_ary[0:2], "~~", data_ary[-3:-1])
    print("정렬 배열(100만개) --> ", sorted_ary[0:2], "~~", sorted_ary[-3:-1])

    count = 0
    sequence_search(data_ary, find_data)
    print("순차 검색(비정렬 데이터) --> ", count, "회")

    count = 0
    binary_search(data_ary, find_data)
    print("이진 검색(정렬 데이터) --> ", count, "회")
