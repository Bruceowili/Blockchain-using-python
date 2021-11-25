# answer_4
def serialize(self):
    result = int_to_little_endian(self.version, 4)
    result += self.prev_block[::-1]
    result += self.merkle_root[::-1]
    result += int_to_little_endian(self.timestamp, 4)
    result += self.bits
    result += self.nonce
    return result
