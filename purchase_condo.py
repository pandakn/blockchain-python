import hashlib
import json
from datetime import datetime

class Blockchain:
    def __init__(self):
        self.blocks = []    # เก็บ Blocks

        # Create Genesis block
        genesis = self.genesis_block = Block(index=len(self.blocks) + 1, data='Genesis Block', prev_hash='0')
        self.blocks.append(genesis)

    # Create block to blockchain
    def add_block(self, data):
        index = len(self.blocks) + 1
        prev_hash = self.blocks[-1].hash
        block = Block(index, data, prev_hash)

        self.blocks.append(block)

    def validate(self):
        for i in range(1, len(self.blocks)):
            if self.blocks[i].prev_hash != self.blocks[i-1].hash:
                return False
        return True

    def display(self):
        for block in self.blocks:
            print(f'Index : {block.index}')
            print(f'Previous Hash : {block.prev_hash}')
            print(f'Data : {block.data}')
            print(f'Timestamp : {block.timestamp}')
            print(f'Block Hash : {block.hash}\n')

class Block:
    def __init__(self, index, data, prev_hash):
        self.index = index
        self.timestamp = str(datetime.now())
        self.data = data
        self.prev_hash = prev_hash
        self.hash = hashlib.sha256(json.dumps(data).encode()).hexdigest()

class Condo:
    def __init__(self, condo_name, size, address, province, price):
        self.condo_name = condo_name
        self.size = size
        self.address = address
        self.province = province
        self.price = price
        self.owner = None

    def purchase(self, buyer):
        self.owner = buyer
        transaction_data = {
            'condo_name': self.condo_name,
            'size': self.size,
            'address': self.address,
            'province': self.province,
            'price': self.price,
            'buyer': buyer,
            'timestamp': str(datetime.now())
        }

        blockchain.add_block(transaction_data)


blockchain = Blockchain()

# Create a new condominium
condo = Condo(condo_name='Supalai Oriental', size='40 m^2', address='Sukhumvit 39', province='Bangkok', price=5300000)
condo_b = Condo(condo_name='LA', size='31.5 m^2', address='Sripatum', province='Bangkok', price=4000000)
condo_c = Condo(condo_name='Na Reva', size='35.3 m^2', address='Charoennakhon', province='Bangkok', price=3900000)
condo_d = Condo(condo_name='The ESSE', size='32 m^2', address='Sukhumvit 36', province='Bangkok', price=6400000)
condo_e = Condo(condo_name='Impression', size='37 m^2', address='Charoennakhon', province='Bangkok', price=3700000)
condo_f = Condo(condo_name='Belle Grand', size='31 m^2', address='Rama', province='Bangkok', price=4200000)
condo_g = Condo(condo_name='The Base', size='39.4 m^2', address='Sukhumvit 50', province='Bangkok', price=6700000)
condo_h = Condo(condo_name='The President', size='32.5 m^2', address='Sukhumvit', province='Bangkok', price=3400000)
condo_i = Condo(condo_name='B-Loft Lite', size='30.5 m^2', address='Sukhumvit 107', province='Bangkok', price=7100000)
condo_j = Condo(condo_name='Plum Condo', size='30.5 m^2', address='Rangsit', province='Bangkok', price=3300000)

# Purchase the condominium  
condo.purchase('John Doe')
condo_b.purchase('Dang Guitar')
condo_c.purchase('Lion Aon')
condo_d.purchase('Panda KN')
condo_e.purchase('Joom Meng')
condo_f.purchase('Me Alia')
condo_g.purchase('Eren Yeager')
condo_h.purchase('Tony Smoke')
condo_i.purchase('Jack The Ghost')
condo_j.purchase('Mike Wazowski')

blockchain.display()

# Validate the blockchain
# print(f'Blockchain is valid : {blockchain.validate()}')
