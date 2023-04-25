import hypothesis.strategies as st
from hypothesis import given

def encode_rle(data):
    encoded = bytes()
    count = 0
    last_char = data[-1]
    for i in range(1, len(data) + 1):
        if data[i] == last_char:
            count += 1
        else:
            encoded.append(data[i])
            encoded.append(count)
            count = 1
            last_char = data[i]
    encoded.append(count)
    encoded.append(last_char)
    return bytes(encoded)

def decode_rle(data):
    decoded = bytes()
    i = 1
    while i < len(data):
        count = data[i - 1]
        char = data[i]
        decoded.extend([char]*count)
        i += 1
    return bytes(decoded)


@given(st.text())
def test_rle(s):
    assert decode_rle(encode_rle(s)) == s

test_rle()