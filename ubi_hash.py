def add64(a, b):
    _0x5bb021 = [a[0] >> 16, a[0] & 0xffff, a[1] >> 16, a[1] & 0xffff]
    _0x93d03c = [b[0] >> 16, b[0] & 0xffff, b[1] >> 16, b[1] & 0xffff]
    
    _0x125a69 = [0, 0, 0, 0]
    
    _0x125a69[3] += _0x5bb021[3] + _0x93d03c[3];  _0x125a69[2] += _0x125a69[3] >> 16;  _0x125a69[3] &= 0xffff
    _0x125a69[2] += _0x5bb021[2] + _0x93d03c[2];  _0x125a69[1] += _0x125a69[2] >> 16;  _0x125a69[2] &= 0xffff
    _0x125a69[1] += _0x5bb021[1] + _0x93d03c[1];  _0x125a69[0] += _0x125a69[1] >> 16;  _0x125a69[1] &= 0xffff
    _0x125a69[0] += _0x5bb021[0] + _0x93d03c[0];  _0x125a69[0] &= 0xffff
    return [_0x125a69[0] << 16 | _0x125a69[1], _0x125a69[2] << 16 | _0x125a69[3]]

def multiply64(a, b):
    _0x265400 = [a[0] >> 16, a[0] & 0xffff, a[1] >> 16, a[1] & 0xffff]
    _0x3d5dec = [b[0] >> 16, b[0] & 0xffff, b[1] >> 16, b[1] & 0xffff]

    _0x1e6311 = [0, 0, 0, 0]
    
    _0x1e6311[3] += _0x265400[3] * _0x3d5dec[3];  _0x1e6311[2] += _0x1e6311[3] >> 16;  _0x1e6311[3] &= 0xffff
    _0x1e6311[2] += _0x265400[2] * _0x3d5dec[3];  _0x1e6311[1] += _0x1e6311[2] >> 16;  _0x1e6311[2] &= 0xffff
    _0x1e6311[2] += _0x265400[3] * _0x3d5dec[2];  _0x1e6311[1] += _0x1e6311[2] >> 16;  _0x1e6311[2] &= 0xffff
    _0x1e6311[1] += _0x265400[1] * _0x3d5dec[3];  _0x1e6311[0] += _0x1e6311[1] >> 16;  _0x1e6311[1] &= 0xffff
    _0x1e6311[1] += _0x265400[2] * _0x3d5dec[2];  _0x1e6311[0] += _0x1e6311[1] >> 16;  _0x1e6311[1] &= 0xffff
    _0x1e6311[1] += _0x265400[3] * _0x3d5dec[1];  _0x1e6311[0] += _0x1e6311[1] >> 16;  _0x1e6311[1] &= 0xffff
    _0x1e6311[0] += _0x265400[0] * _0x3d5dec[3] + _0x265400[1] * _0x3d5dec[2] + _0x265400[2] * _0x3d5dec[1] + _0x265400[3] * _0x3d5dec[0]
    _0x1e6311[0] &= 0xffff
    return [_0x1e6311[0] << 16 | _0x1e6311[1], _0x1e6311[2] << 16 | _0x1e6311[3]]

def rot_l_64(a, b):
    b %= 64
    if b == 32:
        return [a[1], a[0]]
    if b < 32:
        return [
            (a[0] << b | a[1] >> (32 - b)) & 0xffffffff,
            (a[1] << b | a[0] >> (32 - b)) & 0xffffffff,
        ]
    b -= 32
    return [
        (a[1] << b | a[0] >> (32 - b)) & 0xffffffff,
        (a[0] << b | a[1] >> (32 - b)) & 0xffffffff,
    ]

def shift_l_64(a, b):
    b %= 64
    if b == 0:
        return a
    if b < 32:
        return [(a[0] << b | a[1] >> (32 - b)) & 0xffffffff, (a[1] << b) & 0xffffffff]
    return [(a[1] << (b - 32)) & 0xffffffff, 0]

def mix64(_0x275b26):
    # purposefully retains ?potentially purposeful bug? in original script
    _0x275b26 = [_0x275b26[0] ^ [0, _0x275b26[0] >> 1][0], _0x275b26[1] ^ [0, _0x275b26[0] >> 1][1]]
    _0x275b26 = multiply64(_0x275b26, [0xff51afd7, 0xed558ccd])
    _0x275b26 = [_0x275b26[0] ^ [0, _0x275b26[0] >> 1][0], _0x275b26[1] ^ [0, _0x275b26[0] >> 1][1]]
    _0x275b26 = multiply64(_0x275b26, [0xc4ceb9fe, 0x1a85ec53])
    _0x275b26 = [_0x275b26[0] ^ [0, _0x275b26[0] >> 1][0], _0x275b26[1] ^ [0, _0x275b26[0] >> 1][1]]
    return _0x275b26

def murmurhash3(key):
    _0x3feee0 = [0x87c37b91, 0x114253d5]
    _0x585386 = [0x4cf5ad43, 0x2745937f]

    key_len = len(key)
    _0x1124dd = key_len % 16
    _0x5611a9 = key_len - _0x1124dd

    _0x23efda = [0, 0]
    _0x3b4772 = [0, 0]
    _0x5d1478 = [0, 0]
    _0x589ae5 = [0, 0]

    i = 0
    while i < _0x5611a9:
        def get_byte(o): 
            return ord(key[i + o]) & 0xff

        _0x5d1478 = [
            get_byte(4) | get_byte(5) << 8 | get_byte(6) << 16 | get_byte(7) << 24,
            get_byte(0) | get_byte(1) << 8 | get_byte(2) << 16 | get_byte(3) << 24,
        ]
        _0x589ae5 = [
            get_byte(12) | get_byte(13) << 8 | get_byte(14) << 16 | get_byte(15) << 24,
            get_byte(8)  | get_byte(9)  << 8 | get_byte(10) << 16 | get_byte(11) << 24,
        ]

        _0x5d1478 = multiply64(_0x5d1478, _0x3feee0); _0x5d1478 = rot_l_64(_0x5d1478, 31); _0x5d1478 = multiply64(_0x5d1478, _0x585386)
        _0x23efda = [_0x23efda[0] ^ _0x5d1478[0], _0x23efda[1] ^ _0x5d1478[1]]
        _0x23efda = rot_l_64(_0x23efda, 27)
        _0x23efda = add64(_0x23efda, _0x3b4772)
        _0x23efda = add64(multiply64(_0x23efda, [0, 5]), [0, 0x52dce729])

        _0x589ae5 = multiply64(_0x589ae5, _0x585386); _0x589ae5 = rot_l_64(_0x589ae5, 33); _0x589ae5 = multiply64(_0x589ae5, _0x3feee0)
        _0x3b4772 = [_0x3b4772[0] ^ _0x589ae5[0], _0x3b4772[1] ^ _0x589ae5[1]]
        _0x3b4772 = rot_l_64(_0x3b4772, 31)
        _0x3b4772 = add64(_0x3b4772, _0x23efda)
        _0x3b4772 = add64(multiply64(_0x3b4772, [0, 5]), [0, 0x38495ab5])

        i += 16

    def get_tail_byte(o): 
        return ord(key[i + o]) if i + o < key_len else 0

    if _0x1124dd >= 15: _0x589ae5 = [_0x589ae5[0] ^ shift_l_64([0, get_tail_byte(14)], 0x30)[0], _0x589ae5[1] ^ shift_l_64([0, get_tail_byte(14)], 0x30)[1]]
    if _0x1124dd >= 14: _0x589ae5 = [_0x589ae5[0] ^ shift_l_64([0, get_tail_byte(13)], 0x28)[0], _0x589ae5[1] ^ shift_l_64([0, get_tail_byte(13)], 0x28)[1]]
    if _0x1124dd >= 13: _0x589ae5 = [_0x589ae5[0] ^ shift_l_64([0, get_tail_byte(12)], 0x20)[0], _0x589ae5[1] ^ shift_l_64([0, get_tail_byte(12)], 0x20)[1]]
    if _0x1124dd >= 12: _0x589ae5 = [_0x589ae5[0] ^ shift_l_64([0, get_tail_byte(11)], 0x18)[0], _0x589ae5[1] ^ shift_l_64([0, get_tail_byte(11)], 0x18)[1]]
    if _0x1124dd >= 11: _0x589ae5 = [_0x589ae5[0] ^ shift_l_64([0, get_tail_byte(10)], 0x10)[0], _0x589ae5[1] ^ shift_l_64([0, get_tail_byte(10)], 0x10)[1]]
    if _0x1124dd >= 10: _0x589ae5 = [_0x589ae5[0] ^ shift_l_64([0, get_tail_byte(9)],  0x08)[0], _0x589ae5[1] ^ shift_l_64([0, get_tail_byte(9)],  0x08)[1]]
    if _0x1124dd >= 9:
        _0x589ae5 = [_0x589ae5[0] ^ [0, get_tail_byte(8)][0], _0x589ae5[1] ^ [0, get_tail_byte(8)][1]]
        _0x589ae5 = multiply64(_0x589ae5, _0x585386); _0x589ae5 = rot_l_64(_0x589ae5, 33); _0x589ae5 = multiply64(_0x589ae5, _0x3feee0)
        _0x3b4772 = [_0x3b4772[0] ^ _0x589ae5[0], _0x3b4772[1] ^ _0x589ae5[1]]

    if _0x1124dd >= 8: _0x5d1478 = [_0x5d1478[0] ^ shift_l_64([0, get_tail_byte(7)], 0x38)[0], _0x5d1478[1] ^ shift_l_64([0, get_tail_byte(7)], 0x38)[1]]
    if _0x1124dd >= 7: _0x5d1478 = [_0x5d1478[0] ^ shift_l_64([0, get_tail_byte(6)], 0x30)[0], _0x5d1478[1] ^ shift_l_64([0, get_tail_byte(6)], 0x30)[1]]
    if _0x1124dd >= 6: _0x5d1478 = [_0x5d1478[0] ^ shift_l_64([0, get_tail_byte(5)], 0x28)[0], _0x5d1478[1] ^ shift_l_64([0, get_tail_byte(5)], 0x28)[1]]
    if _0x1124dd >= 5: _0x5d1478 = [_0x5d1478[0] ^ shift_l_64([0, get_tail_byte(4)], 0x20)[0], _0x5d1478[1] ^ shift_l_64([0, get_tail_byte(4)], 0x20)[1]]
    if _0x1124dd >= 4: _0x5d1478 = [_0x5d1478[0] ^ shift_l_64([0, get_tail_byte(3)], 0x18)[0], _0x5d1478[1] ^ shift_l_64([0, get_tail_byte(3)], 0x18)[1]]
    if _0x1124dd >= 3: _0x5d1478 = [_0x5d1478[0] ^ shift_l_64([0, get_tail_byte(2)], 0x10)[0], _0x5d1478[1] ^ shift_l_64([0, get_tail_byte(2)], 0x10)[1]]
    if _0x1124dd >= 2: _0x5d1478 = [_0x5d1478[0] ^ shift_l_64([0, get_tail_byte(1)], 0x08)[0], _0x5d1478[1] ^ shift_l_64([0, get_tail_byte(1)], 0x08)[1]]
    if _0x1124dd >= 1:
        _0x5d1478 = [_0x5d1478[0] ^ [0, get_tail_byte(0)][0], _0x5d1478[1] ^ [0, get_tail_byte(0)][1]]
        _0x5d1478 = multiply64(_0x5d1478, _0x3feee0); _0x5d1478 = rot_l_64(_0x5d1478, 31); _0x5d1478 = multiply64(_0x5d1478, _0x585386)
        _0x23efda = [_0x23efda[0] ^ _0x5d1478[0], _0x23efda[1] ^ _0x5d1478[1]]

    _0x23efda = [_0x23efda[0] ^ [0, key_len][0], _0x23efda[1] ^ [0, key_len][1]]
    _0x3b4772 = [_0x3b4772[0] ^ [0, key_len][0], _0x3b4772[1] ^ [0, key_len][1]]

    _0x23efda = add64(_0x23efda, _0x3b4772)
    _0x3b4772 = add64(_0x3b4772, _0x23efda)
    _0x23efda = mix64(_0x23efda)
    _0x3b4772 = mix64(_0x3b4772)
    _0x23efda = add64(_0x23efda, _0x3b4772)
    _0x3b4772 = add64(_0x3b4772, _0x23efda)

    def hex32(v): 
        return format(v & 0xffffffff, '08x')
    
    return hex32(_0x23efda[0]) + hex32(_0x23efda[1]) + hex32(_0x3b4772[0]) + hex32(_0x3b4772[1])


def create_hash(ubi_key: str, response_hash: str) -> str:
    murmur_bytes = murmurhash3(ubi_key).encode('utf-8')

    mmBL1 = bytes(b ^ 0x36 for b in murmur_bytes).decode('utf-8')
    mmBL2 = bytes(b ^ 0x5c for b in murmur_bytes).decode('utf-8')

    final = murmurhash3(mmBL1 + response_hash)
    return murmurhash3(mmBL2 + final)

def get_hash(response_hash: str, ubi_key: str = 'e4273686554a4abe9505354bd2959332'):
    return create_hash(ubi_key, response_hash)