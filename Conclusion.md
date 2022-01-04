## Conclusion

The results of this experiment show that addresses created with private keys that pertain to specific patterns have been used and shown to have had balances at some point, most of these have since had the balances spent.

The private key that consists of 64 zeroes has a balance of 0.01 BTC but due to the method of importing a wallet which encodes the hex address into base58 and in the process strips the leading zeroes. The generated Wallet Import Format (WIF) cannot be imported.

The workflow consisted of feeding the private key to the generate_wallet_address.py function after running it on the command line
Then pasting the output to [this][1] link to check whether it contains or contained any funds at any certain point. Then generating the WIF and importing it [here][2] to see if the funds were available


[1]: https://bitref.com/17YED8YEwDJnHTpExRX9hpiZmFDSCqfh9w 'Check Transaction History'
[2]: https://login.blockchain.com/en/#/settings/addresses/btc 'Learn Markdown'

lockton.sam@gmail.com