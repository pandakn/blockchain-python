import hashlib
import json
from datetime import datetime

class Blockchain:
    def __init__(self):
        self.blocks = []    # เก็บ Blocks

        # Create Genesis block
        genesis = self.genesis_block = Block(index=len(self.blocks), data='Genesis Block', prev_hash='0')
        self.blocks.append(genesis)

    # Create block to blockchain
    def add_block(self, data):
        index = len(self.blocks)
        prev_hash = self.blocks[-1].hash
        block = Block(index, data, prev_hash)

        self.blocks.append(block)

    def select_condo(self):
        condo = Condo(condo_name='Supalai Oriental', size='40 m^2', address='Sukhumvit 39', province='Bangkok', price=5300000)
        condo_b = Condo(condo_name='LA', size='31.5 m^2', address='Sripatum', province='Bangkok', price=4000000)
        condo_c = Condo(condo_name='Na Reva', size='35.3 m^2', address='Charoennakhon', province='Bangkok', price=3900000)
        condo_d = Condo(condo_name='The ESSE', size='32 m^2', address='Sukhumvit 36', province='Bangkok', price=6400000)
        condo_e = Condo(condo_name='Impression', size='37 m^2', address='Charoennakhon', province='Bangkok', price=3700000)        

        print("1. Supalai Oriental")
        print("2. LA")
        print("3. Na Reva")
        print("4. The ESSE")
        print("5. Impression")
        choice = int(input("Select condo: "))
        buyer = input("Type your name: ")

        while True:
            if choice == 1:
                condo.purchase(buyer)
                break
            elif choice == 2:
                condo_b.purchase(buyer)
                break
            elif choice == 3:
                condo_c.purchase(buyer)
                break
            elif choice == 4:
                condo_d.purchase(buyer)
                break
            elif choice == 5:
                condo_e.purchase(buyer)
                break
            else:
                print("Out of scope")
                continue

    def display(self):
        for block in self.blocks:
            print(f'Index : {block.index}')
            print(f'Previous Hash : {block.prev_hash}')
            print(f'Data : {block.data}')
            print(f'Timestamp : {block.timestamp}')
            print(f'Block Hash : {block.hash}\n')

    def display_by_idx(self, idx):
        for block in self.blocks:
            if self.blocks.index(block) == idx:
                print(f'Index : {idx}')
                print(f'Previous Hash : {block.prev_hash}')
                print(f'Data : {block.data}')
                print(f'Timestamp : {block.timestamp}')
                print(f'Block Hash : {block.hash}\n')

    def edit_data(self, idx, new_owner):
        for block in self.blocks:
            if self.blocks.index(block) == idx:
                block.data['buyer'] = new_owner
                block.hash = block.compute_hash()       

    def validate(self):
        for i in range(1, len(self.blocks)):
            current_block = self.blocks[i]
            previous_block = self.blocks[i - 1]
            if current_block.prev_hash != previous_block.hash:
                return "Transaction has been edited!!"
        return "No change."

class Block:
    def __init__(self, index, data, prev_hash):
        self.index = index
        self.timestamp = str(datetime.now())
        self.data = data
        self.prev_hash = prev_hash
        # self.hash = hashlib.sha256(json.dumps(data).encode()).hexdigest()
        self.hash = self.compute_hash()

    def compute_hash(self):
        tx = json.dumps(self.data)
        block_contents = (str(tx) + str(self.prev_hash)).encode()
        return hashlib.sha256(block_contents).hexdigest()

class Condo:
    def __init__(self, condo_name, size, address, province, price):
        self.condo_name = condo_name
        self.size = size
        self.address = address
        self.province = province
        self.price = price
        self.owner = None

    # ซื้อคอนโด
    def purchase(self, buyer):
        self.owner = buyer
        transaction_data = {
            'condo_name': self.condo_name,
            'size': self.size,
            'address': self.address,
            'province': self.province,
            'price': self.price,
            'buyer': buyer,
            'timestamp': '31-12-2022'
        }

        blockchain.add_block(transaction_data)
    

blockchain = Blockchain()

while True:
    #แสดงฟังก์ชันต่างๆของระบบ
    print("======================================================")
    print("Select Option")
    print("1. Purchase Condo")
    print("2. Displays information in selected block condos")
    print("3. Display blocks")
    print("4. Edit TX")
    print("5. Validate")
    print("6. Exit")
    print("======================================================")

    choice = int(input("Select Choice: "))

    if choice == 1:
        condo_name = blockchain.select_condo()
        print(condo_name)
    elif choice == 2:
        block_index = int(input("Blog you want to show: "))
        blockchain.display_by_idx(block_index)
        print("")
    elif choice == 3:
        blockchain.display()
    elif choice == 4:
        block_index = int(input("Type the block number you want to edit: "))
        owner = input("Owner: ")
        print("")
        blockchain.edit_data(block_index, owner)
    elif choice == 5:
        valid = blockchain.validate()
        print(valid)
        
    elif choice == 6:
        break
    else:
        print("Wrong Choice, choose again")