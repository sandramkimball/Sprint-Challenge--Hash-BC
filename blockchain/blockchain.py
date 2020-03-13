import hashlib
import json
from time import time
from uuid import uuid4
from flask import Flask, jsonify, request, render_template


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []       
        self.new_block(previous_hash=1, proof=100) # Create the genesis block

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.last_block)
        }

        # Reset the current list of transactions
        self.current_transactions = []
        # Append the block to chain
        self.chain.append(block)
        # Return the new block
        return self.chain

    def hash(self, block):
        string_block = json.dumps(block, sort_keys=True)
        raw_hash = hashlib.sha256(string_block.encode())
        hex_hash = raw_hash.hexdigest()
        return hex_hash

    @property 
    def last_block(self): #O(1)
        return self.chain[-1]

    def proof_of_work(self, block):
        block_string = json.dumps(block, sort_keys=True)
        proof = 0
        while self.valid_proof(block_string, proof): #until num proof is found
            proof += 1
        return proof

    @staticmethod
    def valid_proof(block_string, proof):
        guess = f'{block_string}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()

        return guess_hash[:3] =='000'

    def new_transaction(self, sender, recipient, amount): #can't be static, we adding things to current trasnactions
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        #last block is cement, unchangeable, so newest/latest bloack is...
        return self.last_block['index'] + 1 

# Instantiate our Node, unique address and blockchain:
app = Flask(__name__)

node_identifier = str(uuid4()).replace('-', '')

blockchain = Blockchain()


@app.route('/mine', methods=['POST'])
def mine():
    # Handle non json request
    values = request.get_json()

    required = ['proof', 'id']
    if not all(k in values for k in required): #nested for loop, no problem, it's small, O(2n) is constant, linear
        response = {'message': 'Missing values'}
        return jsonify(response), 400

    submitted_proof = values['proof']

    block_string = json.dumps(blockchain.last_block, sort_keys=True)
    if blockchain.valid_proof(block_string, submitted_proof):

        blockchain.new_transaction('0', values['id'], 1)

        #forge new block by adding ...the proof
        previous_hash = blockchain.hash(blockchain.last_block)
        block = blockchain.new_block(proof, previous_hash)
    else:
        response={
            'message': 'Proof was invalid or already used'
        }
        return jsonify(response), 200

    # Run the proof of work algorithm to get the next proof
    proof = blockchain.proof_of_work(blockchain.last_block)
    # Forge the new Block by adding it to the chain with the proof
    previous_hash = blockchain.hash(blockchain.last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'new_block': block
    } #dictionary for response because similar keys:values data structure

    return jsonify(response), 200


# @app.route('/chain', methods=['GET'])
@app.route('/full_chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

# Add an endpoint called `last_block` that returns the last block in the chain
@app.route('/last_block', methods=['GET'])
def return_last_block():
    response = {
        'last_block': blockchain.last_block
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def recieve_transaction():
    values = request.get_json()
    required=['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        response={'message': 'Missing values'}
        return jsonify(response), 400

    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    response = {
        "message": f'Transaction will be added to block {index}.'
    }
    return jsonify(response), 200

@app.route('/totals', methods=['GET'])
def get_totals(): 
    #return totals for each id
    values = request.get_json()
    total = 0
    required=['sender', 'recipient', 'amount']

    if not all(k in values for k in required): 
        response = {'message': 'Missing values'}
        return jsonify(response), 400

    if 'sender' == id:
        total -= amount
    if 'recipient' == id:
        total += amount


    response = {
        "total": total
    }
    return jsonify(response), 200




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
