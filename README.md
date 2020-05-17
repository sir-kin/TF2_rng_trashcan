# TF2_rng_trashcan
Implements a 15-bit linear feedback shift register (LFSR) random number generator into Team Fortress 2's scripting language.

Uses this to randomly select a phrase to spam chat with whenever you fire (press mouse1). The LFSR's state is additionally cycled each time 'wasd' is pressed.

This offers considerably more randomness than the usual approach, which just cycles through a list each time 'wasd' is pressed.

https://wiki.teamfortress.com/wiki/Scripting#Randomization
