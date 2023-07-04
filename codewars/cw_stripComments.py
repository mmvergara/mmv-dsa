import re


def strip_comments(strng, markers):
    # res out
    res= []

    # split the arr in lines
    for line in strng.split("\n"):
      # for every markers
      for m in markers:

        # if a marker is present in line remove all of the string after it and also the marker it self
        if m in line:
          line = line[:line.index(m)]
      res.append(line.rstrip())
    
    # join them with \n (for each line)
    return "\n".join(res)


print(strip_comments(
    "watermelons avocados watermelons\n@ bananas ,\n@ ! cherries ! pears oranges\nstrawberries ! watermelons",
    ["#", "'", "@", "^", "-", ",", ".", "?"],
))
