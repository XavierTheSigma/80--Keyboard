from kb import keyboard, encoder_handler
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler

keyboard.keymap = [
     # Layer 0
    [
        # ROW0
        KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.TRNS, KC.PSCR, KC.SLCK, KC.PAUS,
        # ROW1
        KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPC, KC.INS, KC.HOME, KC.PGUP,
        # ROW2
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET, KC.BSLS, KC.DEL, KC.END, KC.PGDN,
        # ROW3
        KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENT, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        # ROW4
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, KC.TRNS, KC.TRNS, KC.TRNS, KC.UP, KC.TRNS,
        # ROW5
        KC.LCTL, KC.LGUI, KC.LALT, KC.TRNS, KC.TRNS, KC.SPC, KC.TRNS, KC.TRNS, KC.RALT, KC.RGUI, KC.FN, KC.RCTL, KC.TRNS, KC.TRNS, KC.LEFT, KC.DOWN, KC.RIGHT,
    ]
]

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),), # Layer 0
]

if __name__ == '__main__':
    keyboard.go()