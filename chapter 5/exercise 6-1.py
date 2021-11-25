 # answer6[]
def fee(self, testnet=False):
    input_sum, output_sum = 0, 0
    for tx_in in self.tx_ins:
        input_sum += tx_in.value(testnet=testnet)
    for tx_out in self.tx_outs:
        output_sum += tx_out.amount
    return input_sum - output_sum
