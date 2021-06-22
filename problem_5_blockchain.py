'''
Blockchain

A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.

Use your knowledge of linked lists and hashing to create a blockchain implementation.
'''

import hashlib
from datetime import datetime


class Chain:
    def __init__(self):
        self.recent = None
        self.difficulty = 4

    def add_block(self, timestamp, data):
        new_block = Block(timestamp, data, self.recent, self.difficulty)
        if self.verify(new_block):
            self.recent = new_block
            return self.recent

    def verify(self, new_block):
        return new_block.hash.startswith("0" * self.difficulty)


class Block:
    def __init__(self, timestamp, data, previous_hash, difficulty):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(difficulty)

    def calc_hash(self, difficulty):
        sha = hashlib.sha256()
        # adding timestamp and previous hash to ensure that the resulting hash is unique
        nonce = 1
        while nonce:
            hash_str = self.data.encode('utf-8') + str(self.timestamp).encode('utf-8') + str(self.previous_hash).encode('utf-8') + str(nonce).encode('utf-8')
            sha.update(hash_str)
            if str(sha.hexdigest()).startswith("0" * difficulty):
                #print(f"found hash after {i} loops.")
                #print(sha.hexdigest())
                return sha.hexdigest()
            nonce += 1


# Testcases in the form of adding blocks to the chain and comparing the hash with the previous hash

blockchain = Chain()
timestamp = datetime.now()
data = "some very important data"
block = blockchain.add_block(timestamp, data)
print(f"current block data: {block.data} | current block hash: {block.hash} | current time stamp: {block.timestamp} \n"
      f"previous block data: {block.previous_hash} | previous block hash: {block.previous_hash}")
prev_block = block

timestamp = datetime.now()
data = "another very important data piece"
block = blockchain.add_block(timestamp, data)
print(f"current block data: {block.data} | current block hash: {block.hash} | current time stamp: {block.timestamp} \n"
      f"previous block data: {block.previous_hash.data} | previous block hash: {block.previous_hash.hash}")
print(True if block.previous_hash.hash == prev_block.hash else False)
prev_block = block

timestamp = datetime.now()
data = "a third very important data piece"
block = blockchain.add_block(timestamp, data)
print(f"current block data: {block.data} | current block hash: {block.hash} | current time stamp: {block.timestamp} \n"
      f"previous block data: {block.previous_hash.data} | previous block hash: {block.previous_hash.hash}")
print(True if block.previous_hash.hash == prev_block.hash else False)
prev_block = block

timestamp = datetime.now()
data = "a forth very important data piece"
block = blockchain.add_block(timestamp, data)
print(f"current block data: {block.data} | current block hash: {block.hash} | current time stamp: {block.timestamp} \n"
      f"previous block data: {block.previous_hash.data} | previous block hash: {block.previous_hash.hash}")
print(True if block.previous_hash.hash == prev_block.hash else False)
prev_block = block

timestamp = datetime.now()
data = "a fifth very important data piece"
block = blockchain.add_block(timestamp, data)
print(f"current block data: {block.data} | current block hash: {block.hash} | current time stamp: {block.timestamp} \n"
      f"previous block data: {block.previous_hash.data} | previous block hash: {block.previous_hash.hash}")
print(True if block.previous_hash.hash == prev_block.hash else False)
prev_block = block

timestamp = datetime.now()
data = "a sixth very important data piece"
block = blockchain.add_block(timestamp, data)
print(f"current block data: {block.data} | current block hash: {block.hash} | current time stamp: {block.timestamp} \n"
      f"previous block data: {block.previous_hash.data} | previous block hash: {block.previous_hash.hash}")
print(True if block.previous_hash.hash == prev_block.hash else False)
prev_block = block