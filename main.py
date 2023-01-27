def solve(N, workload):
    max_sum = 0
    current_sum = 0
    for work in workload:
        if work > 6:
            current_sum = current_sum + 1
            if current_sum > max_sum:
                max_sum = current_sum
        else:
            current_sum = 0
    return max_sum


N = int(input())
workload = list(map(int, input().split()))

out_ = solve(N, workload)
print(out_)
