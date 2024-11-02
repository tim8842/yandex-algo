from typing import List


def get_data(filename: str = "input.txt") -> List[str]:
    with open(filename, "r") as file:
        res = file.readlines()
    return res


def write_data(res: str, filename: str = "output.txt") -> None:
    with open(filename, "w") as file:
        res = file.write(res)


def count_occurrences(arr):
    occurrences = {}
    for num in arr:
        occurrences[num] = occurrences.get(num, 0) + 1
    return occurrences


def logic(n, k, a, count_occurrences, reversed=False):
    a = sorted(a, reverse=reversed)
    keys = list(count_occurrences.keys())
    if len(keys) > 1:
        count = 0
        max_count = 0
        start = [a[0], a[0], 0, 0]
        end = [a[1], a[1], 1, 1]
        i = 1
        if n > 2:
            while i < n - 1:
                if abs(a[i + 1] - start[0]) > k:
                    if abs(a[i] - start[0]) <= k:
                        count = 1
                    else:
                        count = 0
                    if max_count < i - start[2] + count:
                        max_count = i - start[2] + count
                    start[1], start[3] = start[0], start[2]
                    start[0], start[2] = a[start[2] + 1], start[2] + 1
                i += 1
            if abs(a[i] - start[0]) <= k:
                count = 1
            else:
                count = 0
            if max_count < i - start[2] + count:
                max_count = i - start[2] + count
            return max_count
        else:
            if abs(a[1] - a[0]) <= k:
                return 2
            else:
                return 1
            # if count <= max_count:
            #     count += 1
            #     end[1] = end[0]
            #     end[0] = a[i]
            # else:
            #     if abs(end[0] - start[0]) <= k:
            #         max_count = count + 1
            #         # count += 1
            #         # end[1] = end[0]
            #         # end[0] = a[i + 1]
            #     else:
            #         max_count = count
            #         while start[0] == start[1]:
            #             start[1] = start[0]
            #             start[2] += 1
            #             start[0] = a[start[2]]
            #             count -= 1

            # else:
            #     start = a[i]
            #     if count > max_count:
            #         max_count = count
            #     count = 1
            #     start_ptr = i
            # i += 1
        # if count > max_count:
        #     max_count = count
        # return max_count
    else:
        return list(count_occurrences.values())[0]


def main():
    data = get_data()
    n_k = data[0].split(" ")
    n, k, a = int(n_k[0]), int(n_k[1]), [int(i) for i in data[1].split(" ")]
    # occurrences = dict(sorted(count_occurrences(a).items(), reverse=True))
    # res1 = logic(n, k, a, occurrences, reversed=True)
    occurrences = dict(sorted(count_occurrences(a).items()))
    res2 = logic(n, k, a, occurrences)
    write_data(str(res2))


if __name__ == "__main__":
    main()
