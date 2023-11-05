from project_euler.decorators import print_run_time


@print_run_time
def product_pythagorean_triplet_of_sum(target_sum: int) -> int:
    answer_found = False
    # guess values of m and n where m>n and one of m, n are even
    m = 2
    n = 1
    s_ = 0
    while not answer_found and s_ < target_sum / 2:
        s_ = 2 * m**2 + 2 * m * n
        if target_sum % s_ == 0:
            p = target_sum // s_
            a = p * (m**2 - n**2)
            b = p * 2 * m * n
            c = p * (m**2 + n**2)
            answer = a * b * c
            answer_found = True
            break
        if m - n > 2:  # noqa PLR2004
            n += 2  # keep one of m, n even for this m
            print(f"m={m} n={n}")
        else:
            m += 1
            n = m % 2 + 1
            print(f"m={m} n={n}")

    return answer


if __name__ == "__main__":
    s = 1000
    print(f"There exists exactly one Pythagorean triplet for which a + b + c = {s}. Find the product abc.")
    print(f"answer: {product_pythagorean_triplet_of_sum(s)}")
