import time
from mnemonic import Mnemonic
import colorama
from colorama import Fore, Style

# Initialize colorama
colorama.init()

def simulate_hacking_text(text, delay=0.03):
    for char in text:
        print(Fore.RED + char, end='', flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)

def generate_mnemonic(strength):
    mnemo = Mnemonic("english")
    return mnemo.generate(strength=strength)

def main():
    simulate_hacking_text("Software Name: Mnemonic Generator")
    simulate_hacking_text("Software Developed By- Pikai")
    simulate_hacking_text("Software Version: 1.0.1")
    simulate_hacking_text("Description: This software rapidly generates BIP39 standard Mnemonic Phrases")
    
    input(Fore.GREEN + "\nPress Enter to Proceed" + Style.RESET_ALL)
    
    simulate_hacking_text("Warning: Please use these mnemonic phrases carefully, accessing other's wallet without proper consent is illegal.")
    
    while True:
        word_count = input(Fore.GREEN + "Do you want 12 or 24 words Mnemonic phrases? " + Style.RESET_ALL)
        if word_count in ['12', '24']:
            strength = 128 if word_count == '12' else 256
            break
        else:
            print(Fore.RED + "Invalid input. Please enter 12 or 24." + Style.RESET_ALL)
    
    while True:
        try:
            num_phrases = int(input(Fore.GREEN + "How many Mnemonic phrases do you want (1-1000)? " + Style.RESET_ALL))
            if 1 <= num_phrases <= 1000:
                break
            else:
                print(Fore.RED + "Please enter a number between 1 and 1000." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number." + Style.RESET_ALL)
    
    print(Fore.RED + "\nGenerating mnemonic phrases:" + Style.RESET_ALL)
    
    start_time = time.time()
    phrases = []
    for i in range(num_phrases):
        phrase = generate_mnemonic(strength)
        phrases.append(phrase)
        print(Fore.RED + f"{i+1}. {phrase}" + Style.RESET_ALL)
    end_time = time.time()

    generation_time = end_time - start_time
    print(Fore.RED + f"\nGenerated {num_phrases} phrases in {generation_time:.2f} seconds" + Style.RESET_ALL)

    filename = input(Fore.GREEN + "Please enter a file name with .txt to save your file: " + Style.RESET_ALL)
    if not filename.endswith('.txt'):
        filename += '.txt'
    
    with open(filename, 'w') as f:
        for phrase in phrases:
            f.write(phrase + '\n')
    
    print(Fore.GREEN + f"\nMnemonic phrases have been saved to {filename}" + Style.RESET_ALL)

if __name__ == "__main__":
    main()