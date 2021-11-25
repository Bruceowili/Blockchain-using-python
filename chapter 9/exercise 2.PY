
# answer2
def coinbase_height(self):
    if not self.is_coinbase():
        return None
    element = self.tx_ins[0].script_sig.cmds[0]
    return little_endian_to_int(element)

