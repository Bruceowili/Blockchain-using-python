
# 1
def is_coinbase(self):
    if len(self.tx_ins) != 1:
        return False
    first_input = self.tx_ins[0]
    if first_input.prev_tx != b'\x00' * 32:
        return False
    if first_input.prev_index != 0xffffffff:
        return False
    return True
