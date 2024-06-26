import time
import random
from eth_account import Account
from web3 import Web3
import colorama
from colorama import Fore, Style
from mnemonic import Mnemonic
import requests

# Initialize colorama
colorama.init()

# Enable unaudited HD wallet features
Account.enable_unaudited_hdwallet_features()

# API keys
INFURA_API_KEY = "a8cb0c33a1c44927a2ea6fce2b4ba608"
BSCSCAN_API_KEY = "WHX4VAY9NTK333I5NZHNCGMYBK568CEVMSK"

# Network configurations
NETWORKS = {
    "Ethereum": f"https://mainnet.infura.io/v3/{INFURA_API_KEY}",
    "Polygon": f"https://polygon-mainnet.infura.io/v3/{INFURA_API_KEY}",
}

def simulate_hacking_text(text, delay=0.03):
    for char in text:
        print(Fore.RED + char, end='', flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)

def is_valid_mnemonic(mnemonic):
    mnemo = Mnemonic("english")
    return mnemo.check(mnemonic)

def generate_wallet(mnemonic):
    if not is_valid_mnemonic(mnemonic):
        raise ValueError("Invalid mnemonic")
    account = Account.from_mnemonic(mnemonic)
    return account.address

def check_balance_bsc(address):
    url = f"https://api.bscscan.com/api?module=account&action=balance&address={address}&tag=latest&apikey={BSCSCAN_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data["status"] == "1":
            balance = int(data["result"])
            return balance > 0
    return False

def check_existing_wallet(address):
    for network, url in NETWORKS.items():
        w3 = Web3(Web3.HTTPProvider(url))
        balance = w3.eth.get_balance(address)
        if balance > 0:
            return True, network
    
    # Check BSC balance
    if check_balance_bsc(address):
        return True, "BSC"
    
    return False, None

def main():
    simulate_hacking_text("Software Name: Mnemonic Validator")
    simulate_hacking_text("Software Developed By- Pikai")
    simulate_hacking_text("Software Version: 1.0.5")
    simulate_hacking_text("Description: This software validates and generates wallets against BIP39 standard Mnemonic Phrases for Ethereum, BSC, and Polygon")
    
    input(Fore.GREEN + "\nPress Enter to Proceed" + Style.RESET_ALL)
    
    simulate_hacking_text("Warning: Please use the software for security research purposes only, accessing someone else's wallet without proper consent is illegal.")
    
    file_path = input(Fore.GREEN + "Give the .txt file containing mnemonic seed phrases (up to 1000 lines): " + Style.RESET_ALL)
    
    generated_wallets = []
    existing_wallets = []
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                mnemonic = line.strip()
                try:
                    if is_valid_mnemonic(mnemonic):
                        address = generate_wallet(mnemonic)
                        generated_wallets.append(address)
                        print(Fore.GREEN + f"Generated: {address}" + Style.RESET_ALL)
                        
                        exists, network = check_existing_wallet(address)
                        if exists:
                            existing_wallets.append((address, network))
                            print(Fore.RED + f"Accessed: {address} (on {network})" + Style.RESET_ALL)
                    else:
                        print(Fore.RED + f"Invalid mnemonic: {mnemonic}" + Style.RESET_ALL)
                except Exception as e:
                    print(Fore.RED + f"Error processing mnemonic: {mnemonic}. Error: {str(e)}" + Style.RESET_ALL)
    except FileNotFoundError:
        print(Fore.RED + "File not found. Please check the file path and try again." + Style.RESET_ALL)
        return
    
    if generated_wallets:
        generated_file = input(Fore.YELLOW + "Enter a file name with .txt to save the Generated addresses: " + Style.RESET_ALL)
        if not generated_file.endswith('.txt'):
            generated_file += '.txt'
        with open(generated_file, 'w') as f:
            for address in generated_wallets:
                f.write(f"{address}\n")
        print(Fore.GREEN + f"Generated addresses saved to {generated_file}" + Style.RESET_ALL)
    
    if existing_wallets:
        existing_file = input(Fore.YELLOW + "Enter a file name with .txt to save the Accessed addresses: " + Style.RESET_ALL)
        if not existing_file.endswith('.txt'):
            existing_file += '.txt'
        with open(existing_file, 'w') as f:
            for address, network in existing_wallets:
                f.write(f"{address} (on {network})\n")
        print(Fore.GREEN + f"Existing addresses saved to {existing_file}" + Style.RESET_ALL)

if __name__ == "__main__":
    main()