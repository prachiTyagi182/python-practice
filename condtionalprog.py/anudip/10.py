def stats(*args):
    # Sum, Average aur Max calculate karein
    total_sum = sum(args)
    avg = total_sum / len(args)
    max_val = max(args)

    return {
        'sum': total_sum,
        'average': avg,
        'maximum': max_val
    }


result = stats(10, 20, 30, 40, 50)
print(result)