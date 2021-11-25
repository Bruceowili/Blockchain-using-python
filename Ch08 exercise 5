#EX_5
def sig_hash(self, input_index, redeem_script=None):
    '''Returns the integer representation of the hash that needs to get
    signed for index input_index'''
    s = int_to_little_endian(self.version, 4)
    s += encode_varint(len(self.tx_ins))
    for i, tx_in in enumerate(self.tx_ins):
        if i == input_index:
            if redeem_script:
                script_sig = redeem_script
            else:
                script_sig = tx_in.script_pubkey(self.testnet)
        else:
            script_sig = None
        s += TxIn(
            prev_tx=tx_in.prev_tx,
            prev_index=tx_in.prev_index,
            script_sig=script_sig,
            sequence=tx_in.sequence,
        ).serialize()
    s += encode_varint(len(self.tx_outs))
    for tx_out in self.tx_outs:
        s += tx_out.serialize()
    s += int_to_little_endian(self.locktime, 4)
    s += int_to_little_endian(SIGHASH_ALL, 4)
    h256 = hash256(s)
    return int.from_bytes(h256, 'big')


def verify_input(self, input_index):
    tx_in = self.tx_ins[input_index]
    script_pubkey = tx_in.script_pubkey(testnet=self.testnet)
    if script_pubkey.is_p2sh_script_pubkey():
        cmd = tx_in.script_sig.cmds[-1]
        raw_redeem = encode_varint(len(cmd)) + cmd
        redeem_script = Script.parse(BytesIO(raw_redeem))
    else:
        redeem_script = None
    z = self.sig_hash(input_index, redeem_script)
    combined = tx_in.script_sig + script_pubkey
    return combined.evaluate(z)
