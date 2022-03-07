import toml

ETHERSCAN_KEY = ""
try:
    parsed=toml.load("apis/apis.toml")
    ETHERSCAN_KEY = parsed["etherscan"]["default_key"]
except toml.TomlDecodeError: 
    print("TomlDecodeError")

if __name__ == "__main__":
    print(ETHERSCAN_KEY)
