import os
import hashlib


def create_merkle_tree(path: str) -> str:
    """
    Computes the Merkle tree for a given directory path.
    Returns the root hash of the Merkle tree.
    """
    if not os.path.isdir(path):
        raise ValueError("Invalid directory path")

    tree = []
    for dir_path, dir_names, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dir_path, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'rb') as f:
                    hash_value = hashlib.sha256(f.read()).hexdigest()
                    tree.append(hash_value)
        for dir_name in dir_names:
            hash_value = hashlib.sha256(dir_name.encode()).hexdigest()
            tree.append(hash_value)
    while len(tree) > 1:
        new_level = []
        for i in range(0, len(tree), 2):
            left = tree[i]
            right = tree[i+1] if i+1 < len(tree) else ''
            combined = left + right
            new_hash = hashlib.sha256(combined.encode('utf-8')).hexdigest()
            new_level.append(new_hash)
        tree = new_level

    return tree[0] if tree else ''
