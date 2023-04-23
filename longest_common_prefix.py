def longestCommonPrefix(strs: list[str]) -> str:
    for length in range(len(strs[0]), 0, -1):
        str_to_compare = strs[0][:length]
        all_fine = True
        for string in strs:
            if not string.startswith(str_to_compare):
                all_fine = False
        if all_fine:
            return str_to_compare

print(longestCommonPrefix(["flower", "flow", "flight"]))
