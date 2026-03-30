# Keyboard
My Keyboard is a standard 80% keyboard with an added Rotary Encoder for volume control.

I made this Keyboard for myself, And to learn. This was my first time using Chip on Board tech, so it was quite a challenge for me, but it helped me learn alot.

## Features:
- 80% Keyboard
- 

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


