import hashlib

def generate_merkle_root(units):
    hashes = [hashlib.sha256(str(i).encode()).hexdigest() for i in range(units)]
    while len(hashes) > 1:
        if len(hashes) % 2 != 0:
            hashes.append(hashes[-1])
        hashes = [hashlib.sha256((hashes[i] + hashes[i+1]).encode()).hexdigest() for i in range(0, len(hashes), 2)]
    return hashes[0]

inventory_count = 30000
root = generate_merkle_root(inventory_count)
print(f"2026 Merkle Root: {root}")
with open("merkle_proof.txt", "w") as f:
    f.write(f"Audit Ref: BNBA-9921-X\nInventory: {inventory_count}\nRoot: {root}")
