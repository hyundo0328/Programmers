def solution(numbers):
    numbers = sorted(numbers)
    return numbers[len(numbers)-1]*numbers[len(numbers)-2]