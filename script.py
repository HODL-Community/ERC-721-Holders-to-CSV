from web3 import Web3
import csv

# Connect to the network
rpc_url = ''  # Replace with your RPC URL
web3 = Web3(Web3.HTTPProvider(rpc_url))

# Check if the connection is successful
if not web3.is_connected():
    print("Failed to connect to the network")
    exit()

# ERC-721 Contract Details
contract_address = Web3.to_checksum_address('')
abi = []  # You need to provide the ABI for the contract

# Create a contract instance
contract = web3.eth.contract(address=contract_address, abi=abi)

# Function to get the owner of a token
def get_owner(token_id):
    return contract.functions.ownerOf(token_id).call()

# Store the owners
owners = {}

# Iterate over the token IDs
for token_id in range(x): # Replace 'x' with # of tokens
    try:
        owner = get_owner(token_id)
        owners[owner] = owners.get(owner, 0) + 1
    except Exception as e:
        print(f"Error fetching owner for token {token_id}: {e}")

# Writing results to a CSV file
with open('owners.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Owner (Address)', 'Held NFTs (# of NFTs held)'])

    for address, count in owners.items():
        writer.writerow([address, count])

print("Finished writing to CSV")
