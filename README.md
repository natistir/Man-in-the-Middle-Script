# Man-in-the-Middle-Script
A simple python script that initiates a Man in the Middle Attack using ARP spoof

Step 0: Download test.py and move it to kali Linux’s desktop.

Step 1: Open virtual box and locate windows and kali. Switch windows to a public network by clicking on network and selecting public network. Switch Kali to a public network by clicking on network and selecting public network.

Step 2: Start kali in virtual box and open the terminal, for this man in the middle attack you need the latest version of python.  If you don’t have the latest version of the python installed on kali type “sudo apt-get install python3 ” in kali’s terminal to install python.

Step 3: Install scapy on kali by typing “pip3 install scapy” in kali’s terminal. Finally get kali’s IP address by typing “sudo ifconfig” into kali’s terminal save the IP you will need it later.

Step 4: Open Windows in virtual box and open the terminal and ping kali by typing “ping <IP of KALI>”. Don’t close the terminal now type “arp -a” to get windows IP address.

Step 5: Go back to kali open the terminal and type ” sudo python3 test.py” hit enter now enter in your targets IP (The windows IP address from step 4) and finally enter the gateways IP (the routers IP).

Step 6: Go back to windows and type in “arp -a” in its terminal Kalis Ip and the Router IP should now have the same MAC address

Step 7: To end the script type Ctl+C to end the script on kali

Step 8: Go back to windows and type “arp -a” to verify that the routers IP reverted back to normal.

