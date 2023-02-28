# E211 whitespace before '('
print ()

# E225 missing whitespace around operator
a=1+2

# E231 missing whitespace after ','
print("a","b")

# E251 unexpected spaces around keyword / parameter equals
# E302 expected 2 blank lines, found 1
def f(k = "1"):
    return 0

# E701 multiple statements on one line (colon)
if a > 5: y = 1

# E702 multiple statements on one line (semicolon)
a = 1; b = 3

# E711 comparison to None should be 'if cond is None:'
if a == None:
    a = 1

# E712 comparison to True should be 'if cond is True:' or 'if cond:'
if a == True:
    a = 1
