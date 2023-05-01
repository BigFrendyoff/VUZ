import re


def main(s):
    pattern = r"{{\s*set\s+@'(\w+)'\s*:=\s*\[([\w\s,\\, \\n]+)\];\s*}}\s*;"
    matches = re.findall(pattern, s)
    return [(name, [value.strip()
                    for value in values.split(',')])
            for name, values in matches]
