# Keyboard
My Keyboard is a standard 80% keyboard with an added Rotary Encoder for volume control.

I made this Keyboard for myself, And to learn. This was my first time using Chip on Board tech, so it was quite a challenge for me, but it helped me learn alot.

## Features:
- 80% Keyboard
- 87 Keys
- Rotary Encoder 
- Arrow Keys
- F Keys

## CAD Model:
I designed the Case to fit together with 3 pieces and 8 M2.5 screws. The 3 pieces are the Bottom of the case, The sides of the case (with a cutout for the USB-C) and the Top of the case, which includes the switch plate and the Top Frame.

<img src=assets/cad.png alt="Keyboard" width="500"/>

## PCB:
I made my PCB in KiCad. This was my first time using CoB, Chip on Board, where instead of using a microcontroller, The RP2040 chip is directly on the board with all the other necessary components. I ended up reffereing to [RP2040 Datasheet](https://pip.raspberrypi.com/documents/RP-008371-DS-rp2040-datasheet.pdf) alot for this. 

Here is the Schematic, I spend alot of time figuring out how to get the whole CoB system working, but I think I did well.

<img src=assets/schematic.png alt="Keyboard" width="500"/>

Here is the PCB, I think I was able to make it pretty Compact with the components, however I am still unsure about the USB-C port.

<img src=assets/pcb.png alt="Keyboard" width="500"/>

## Firmware:
I decided on [KMK](https://github.com/KMKfw/kmk_firmware) firmware for this keyboard, as it is quite easy to code and implement.

## BOM:
|Name                    |Purpose                     |Quantity|Total Cost (USD)|Link                                                                                                                                                                                                                                                              |Distributor|
|------------------------|----------------------------|--------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
|PCBA                    |Printed Circuit Board       |2       |63.79           |https://cart.jlcpcb.com/shopcart/cart                                                                                                                                                                                                                             |JLCPCB     |
|3x4mm SMD tactile switch|BOOT and RESET              |100     |3.04            |https://www.aliexpress.com/item/1005005551946922.html?spm=a2g0o.cart.0.0.6cea38daTwsp4M&mp=1&pdp_npi=6%40dis%21AUD%21AUD%204.43%21AUD%204.43%21%21AUD%204.34%21%21%21%402103274e17748741857928605e241d%2112000033511703865%21ct%21AU%216079532204%21%211%210%21   |Aliexpress |
|Hotswap Sockets         |For the switches to go into.|110     |6.78            |https://www.aliexpress.com/item/1005007232040760.html?spm=a2g0o.cart.0.0.691238daXmoF8z&mp=1&pdp_npi=6%40dis%21AUD%21AUD%2021.04%21AUD%209.89%21%21AUD%209.79%21%21%21%402101d6ff17748726457652554ef3f5%2112000039893759777%21ct%21AU%216079532204%21%211%210%21  |Aliexpress |
|Rotary Encoder          |Volume Control              |2       |2.33            |https://www.aliexpress.com/item/1005009360298765.html?spm=a2g0o.cart.0.0.691238daXmoF8z&mp=1&pdp_npi=6%40dis%21AUD%21AUD%207.09%21AUD%203.40%21%21AUD%203.37%21%21%21%402101d6ff17748726457652554ef3f5%2112000049239221996%21ct%21AU%216079532204%21%211%210%21   |Aliexpress |
|Mechanical Switches     |Register Keystrokes         |90      |11.10           |https://www.aliexpress.com/item/1005010733013518.html?spm=a2g0o.cart.0.0.691238daXmoF8z&mp=1&pdp_npi=6%40dis%21AUD%21AUD%205.39%21AUD%205.39%21%21AUD%205.39%21%21%21%402101d6ff17748726457652554ef3f5%2112000053347971169%21ct%21AU%216079532204%21%213%210%21   |Aliexpress |
|Keycap Set              |To press on                 |1       |12.61           |https://www.aliexpress.com/item/1005009316481772.html?spm=a2g0o.cart.0.0.691238daXmoF8z&mp=1&pdp_npi=6%40dis%21AUD%21AUD%2018.39%21AUD%2018.39%21%21AUD%2018.39%21%21%21%402101d6ff17748723426904626ef3f5%2112000048726412320%21ct%21AU%216079532204%21%211%210%21|Aliexpress |
|Stabilizers             |Prevent Wobbling            |1       |2.60            |https://www.aliexpress.com/item/1005007212869086.html?spm=a2g0o.cart.0.0.691238daXmoF8z&mp=1&pdp_npi=6%40dis%21AUD%21AUD%203.79%21AUD%203.79%21%21AUD%203.79%21%21%21%402101d6ff17748723426904626ef3f5%2112000039826435204%21ct%21AU%216079532204%21%211%210%21   |Aliexpress |
|1N5819 Diode (SMD)      |Diodes for Matrix           |100     |2.03            |https://www.aliexpress.com/item/1005010391501956.html?mp=1&pdp_npi=6%40dis%21AUD%21AUD%202.96%21AUD%202.96%21%21AUD%202.87%21%21%21%402101d6ff17748723426904626ef3f5%2112000052256220506%21ct%21AU%216079532204%21%211%210%21                                     |Aliexpress |
|                        |                            |        |                |                                                                                                                                                                                                                                                                  |           |


