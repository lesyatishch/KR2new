"""Дана последовательность целых чисел. 
Элементы последовательности могут принимать целые значения от —100 000 до 100 000 включительно.
Определите количество троек элементов последовательности, в которых хотя бы один из трёх элементов оканчивается на 3, 
а сумма элементов тройки не больше максимального элемента последовательности, являющегося пятизначным числом, 
которое оканчивается на 3.  В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности."""



def finder(arr):
    # максимальное пятизначное число, оканчивающееся на 3
    max_five_digit_ending_in_3 = None
    for num in arr:
        if 10000 <= num <= 99999 and num % 10 == 3:
            if max_five_digit_ending_in_3 is None or num > max_five_digit_ending_in_3:
                max_five_digit_ending_in_3 = num
    if max_five_digit_ending_in_3 is None:
        return 0
    
    # количество троек, удовлетворяющих условиям
    count = 0
    for i in range(len(arr) - 2):
        triple = arr[i:i+3]
        if any(num % 10 == 3 for num in triple):
            if sum(triple) <= max_five_digit_ending_in_3:
                count += 1
    return count

arr = [12345, 234, 12, 1003, 40000, 15003, 99333, 123]
result = finder(arr)
print(result)
