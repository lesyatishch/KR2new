"""Возрастающей подпоследовательностью будем называть последовательность символов, расположенных в 
порядке увеличения их номера в кодовой таблице символов ASCII. 
Во веденной строке определите длину наибольшей возрастающей подпоследовательности, содержащейся в ней."""

def longest_asc(s):
    max_l = 0
    curr_l = 1
    max_seq = ""
    curr_seq = s[0] if s else ""

    for i in range(1, len(s)):
        if ord(s[i]) > ord(s[i - 1]): 
            curr_l += 1
            curr_seq += s[i]
        else:
            if curr_l > max_l:
                max_l = curr_l
                max_seq = curr_seq
            curr_l = 1
            curr_seq = s[i]

    if curr_l > max_l:
        max_l = curr_l
        max_seq = curr_seq
    return max_l, max_seq

s = "fhsYHQWERbsnju"
length, sequence = longest_asc(s)
print(f"Длина: {length}, последовательность: {sequence}")
