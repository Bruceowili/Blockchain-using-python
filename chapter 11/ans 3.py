#3
def merkle_root(hashes):
    '''Takes a list of binary hashes and returns the merkle root
    '''
    current_level = hashes
    while len(current_level) > 1:
        current_level = merkle_parent_level(current_level)
    return current_level[0]

