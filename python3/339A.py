from collections import Counter


s = input()
cnt = Counter(s)
ans = ([] if cnt["1"] == 0 else ["1"] * cnt["1"]) + ([] if cnt["2"] == 0 else ["2"] * cnt["2"]) + ([] if cnt["3"] == 0 else ["3"] * cnt["3"])

print("+".join(ans))
