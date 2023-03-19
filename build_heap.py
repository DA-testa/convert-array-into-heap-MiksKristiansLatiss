# python3


def build_heap(data):
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
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(swap_count)
    for swap in swap_list:
        print(swap[0], swap[1])


if __name__ == "__main__":
    main()
