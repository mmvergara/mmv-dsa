import re


def strip_comments(strng, markers):
    res= []

    for line in strng.split("\n"):
      for m in markers:
        if m in line:
          line = line[:line.index(m)]
      res.append(line.rstrip())
    
    return "\n".join(res)


print(strip_comments(
    "watermelons avocados watermelons\n@ bananas ,\n@ ! cherries ! pears oranges\nstrawberries ! watermelons",
    ["#", "'", "@", "^", "-", ",", ".", "?"],
))
