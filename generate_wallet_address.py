import bitcoin


def run():
    valid_private_key = False
    while not valid_private_key:
        private_key = input("Enter private key")
        with open('tried_combinations.txt', 'a') as file:
            file.write(private_key+"\n")
        print("Generating Wallet Address...")
        decoded_private_key = bitcoin.decode_privkey(private_key, 'hex')
        valid_private_key = 0 < decoded_private_key < bitcoin.N

        wif_encoded_private_key = bitcoin.encode_privkey(decoded_private_key, 'wif')
        print("wif_encoded_private_key\n", wif_encoded_private_key)
        public_key = bitcoin.fast_multiply(bitcoin.G, decoded_private_key)
        address = bitcoin.pubkey_to_address(public_key)
        print("wallet address\n", address)
        print("Success!")
        return
    print("Failure.")
    
run()