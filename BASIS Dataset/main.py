from blockchain_module import PoABlockchain
from smart_contract import SmartContract
import hashlib

# Initialize
blockchain = PoABlockchain()
contract = SmartContract()

# Register nodes
blockchain.register_node("iot_1")
contract.grant_access("iot_1", "sensor_data")

# Simulated data
data = "temperature=25"

# Access check
if contract.check_access("iot_1", "sensor_data"):
    data_hash = hashlib.sha256(data.encode()).hexdigest()
    blockchain.add_block(data_hash, "iot_1")
    print("Data stored securely in blockchain")

print("Blockchain valid:", blockchain.is_valid())