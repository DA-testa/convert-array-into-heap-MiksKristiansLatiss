import sys


def build_heap(n, data):
    swap_count = 0
    swap_list = []
    size = n - 1

    def sift_down(i):
        nonlocal swap_count, swap_list, data

        min_index = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left <= size and data[left] < data[min_index]:
            min_index = left

        if right <= size and data[right] < data[min_index]:
            min_index = right

        if i != min_index:
            data[i], data[min_index] = data[min_index], data[i]
            swap_count += 1
            swap_list.append((i, min_index))
            sift_down(min_index)

    for i in range(n // 2, -1, -1):
        sift_down(i)

    return swap_count, swap_list


def main():
    if len(sys.argv) < 2:
        return
    input_type = sys.argv[1]
    if input_type == "I":
        n = int(input().strip())
        data = list(map(int, input().split()))
        assert len(data) == n
    elif input_type == "F":
        filename = input().strip()
        with open(filename, "r") as f:
            n = int(f.readline().strip())
            data = list(map(int, f.readline().split()))
            assert len(data) == n
    else:
        return

    swap_count, swap_list = build_heap(n, data)
    
    print(swap_count)
    for swap in swap_list:
        print(swap[0], swap[1])


if __name__ == "__main__":
    main()
