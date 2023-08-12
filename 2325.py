def decodeMessage(self, key: str, message: str) -> str:
    mp = {}
    alp = "abcdefghijklmnopqrstuvwxyz"
    keys = "".join(key.split(" "))
    offset = 0
    for i in range(len(keys)):
        if keys[i] in mp:
            offset += 1
            continue
        mp[keys[i]] = alp[i - offset]

    ans = [""] * len(message)

    for i in range(len(message)):
        if message[i] == " ":
            ans[i] = " "
            continue
        ans[i] = mp[message[i]]
    return "".join(ans)


decodeMessage(
    "", key="the quick brown fox jumps over the lazy dog", message="vkbs bs t suepuv"
)

x = {
    "t": "a",
    "h": "b",
    "e": "c",
    "q": "d",
    "u": "e",
    "i": "f",
    "c": "g",
    "k": "h",
    "b": "i",
    "r": "j",
    "o": "k",
    "w": "l",
    "n": "m",
    "f": "n",
    "x": "p",
    "j": "q",
    "m": "s",
    "p": "t",
    "s": "u",
    "v": "w",
}
