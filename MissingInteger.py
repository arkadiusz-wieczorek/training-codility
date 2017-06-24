# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(arr):
    if len(arr) == 0 : return 1

    # zwroc liste unikatowych posortowanych elementow
    sorted_arr = sorted(list(set(arr)), key=int)
    # usuwamy minusowe wartosci
    sorted_arr = filter (lambda el: el > 0, sorted_arr)

    if len(sorted_arr) == 0 : return 1
    # tworzymy tablice wartosci prawidlowych od 1..len(sorted_arr)+1
    correct_arr = range(1, len(sorted_arr)+1)

    if sorted_arr == correct_arr: return correct_arr[-1]+1

    for i in range(0,len(sorted_arr)):
        try:
            if sorted_arr[i] != correct_arr[i]:
                return correct_arr[i]
            else: continue
        except IndexError:
            return correct_arr[-1] + 1

    pass
