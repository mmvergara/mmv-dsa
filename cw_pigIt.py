import string


def pig_it(text):
    arr = text.split()

    for i in range(len(arr)):
        arr[i] = f"{arr[i][1:]+arr[i][:1]}ay"

    return " ".join(arr)


pig_it("Pig latin is cool")
