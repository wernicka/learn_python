#! python3
# pw.py - An example insecure password locker program from Automate the Boring Stuff Chapter 6

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'locker': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '2819'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy acount password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f"Password for {account} copied to clipboard.")
else:
    print(f"There is no account named {account}.")
