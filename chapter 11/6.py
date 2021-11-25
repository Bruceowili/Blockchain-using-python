# 6
@classmethod
def parse(cls, s):
    version = little_endian_to_int(s.read(4))
    prev_block = s.read(32)[::-1]
    merkle_root = s.read(32)[::-1]
    timestamp = little_endian_to_int(s.read(4))
    bits = s.read(4)
    nonce = s.read(4)
    total = little_endian_to_int(s.read(4))
    num_hashes = read_varint(s)
    hashes = []
    for _ in range(num_hashes):
        hashes.append(s.read(32)[::-1])
    flags_length = read_varint(s)
    flags = s.read(flags_length)
    return cls(version, prev_block, merkle_root, timestamp, bits,
               nonce, total, hashes, flags)

