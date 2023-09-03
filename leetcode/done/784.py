from randoms.dsa import *


def letterCasePermutation(self, s: str) -> List[str]:
    perms = [""]

    for char in s:
        if char.isalpha():
            perms = [perm + char.lower() for perm in perms] + [
                perm + char.upper() for perm in perms
            ]
            print(perms)
        else:
            perms = [perm + char for perm in perms]
            print(perms)

    return perms


print(letterCasePermutation("", "rmrqweqwe"))


# def letterCasePermutation(self, s: str) -> List[str]:
#     perms = ['']

#     for char in s:
#         if char.isalpha():
#             perms = [perm + char.lower() for perm in perms] + [perm + char.upper() for perm in perms]
#         else:
#             perms = [perm + char for perm in perms]

#     return perms
