from itertools import permutations
def print_permutations(s, r):
    perms = permutations(s, r)
    for perm in sorted(perms):  
        print(''.join(perm))
if __name__ == "__main__":
    input_string, size = input().split()
    size = int(size)
    print_permutations(sorted(input_string), size)
