numbers = [1, 3, 2, 4]
MOD = 1_000_000_007

ranks = {value: index + 1 for index, value in enumerate(sorted(set(numbers)))}
size = len(ranks)
max_length = [0] * (size + 1)
ways = [0] * (size + 1)


def query(index):
    length = 0
    count = 0
    while index > 0:
        if max_length[index] > length:
            length = max_length[index]
            count = ways[index]
        elif max_length[index] == length:
            count = (count + ways[index]) % MOD
        index -= index & -index
    return length, count


def update(index, length, count):
    while index <= size:
        if length > max_length[index]:
            max_length[index] = length
            ways[index] = count
        elif length == max_length[index]:
            ways[index] = (ways[index] + count) % MOD
        index += index & -index


answer_length = 1
answer_count = 0
for number in numbers:
    rank = ranks[number]
    length, count = query(rank - 1)
    current_length = length + 1
    current_count = count if length > 0 else 1
    update(rank, current_length, current_count)
    if current_length > answer_length:
        answer_length = current_length
        answer_count = current_count
    elif current_length == answer_length:
        answer_count = (answer_count + current_count) % MOD

print(answer_length, answer_count % MOD)
