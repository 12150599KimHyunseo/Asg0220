import random

num = 10
data_ary = ['코카콜라', '츄파춥스', '도시락', '삼각김밥', '레쓰비캔커피', '바나나맛우유']
product_ary = [random.choice(data_ary) for _ in range(num)]


def binary_search(ary, find_data):
    start = 0
    end = len(ary) - 1

    while start <= end:
        mid = (start + end) // 2
        if find_data == ary[mid]:
            return mid
        elif find_data > ary[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1


if __name__ == "__main__":
    print("#오늘 판매된 전체 물건(중복O, 정렬X) --> ", product_ary)

    product_ary.sort()
    print("#오늘 판매된 전체 물건(중복O, 정렬O) --> ", product_ary)

    sold_product = list(set(product_ary))
    print("#오늘 판매된 물품 종류(중복x) --> ", sold_product)

    count_list = []
    for product in sold_product:
        count = 0
        pos = 0
        while pos != -1:
            pos = binary_search(product_ary, product)
            if pos != -1:
                count = count + 1
                del(product_ary[pos])
        count_list.append((product, count))

    print("\n결산 결과 ==> ", count_list)
