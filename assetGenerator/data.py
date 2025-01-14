from enum import StrEnum

class TYPES(StrEnum):
    LOGIC = 'logic'
    NUMBER = 'number'
    COMPOSITE = 'composite'
    VIDEO = 'video'
    AUDIO = 'audio'
    
    
hex2rgb = lambda hex: tuple(int(hex[i:i+2], 16) for i in (1, 3, 5))

COLORS_HEX = {
    TYPES.LOGIC : '#fd004c',
    TYPES.NUMBER : '#00e132',
    TYPES.COMPOSITE : '#7f00fd',
    TYPES.VIDEO : '#25cfb8',
    TYPES.AUDIO : '#bd7e2b'
}

COLORS = {k: hex2rgb(v) for k, v in COLORS_HEX.items()}

DATA = {
    "AND": {
        "inputs": {
            "A": TYPES.LOGIC,
            "B": TYPES.LOGIC
        },
        "outputs": {
            "A AND B": TYPES.LOGIC
        },
    },
    "OR": {
        "inputs": {
            "A": TYPES.LOGIC,
            "B": TYPES.LOGIC
        },
        "outputs": {
            "A OR B": TYPES.LOGIC
        },
    },
    "BUFFER": {
        "inputs": {
            "A": TYPES.LOGIC
        },
        "outputs": {
            "A": TYPES.LOGIC
        },
    },
    "XOR": {
        "inputs": {
            "A": TYPES.LOGIC,
            "B": TYPES.LOGIC
        },
        "outputs": {
            "A XOR B": TYPES.LOGIC
        },
    },
    "NOT": {
        "inputs": {
            "A": TYPES.LOGIC
        },
        "outputs": {
            "NOT A": TYPES.LOGIC
        },
    },
    "NAND": {
        "inputs": {
            "A": TYPES.LOGIC,
            "B": TYPES.LOGIC
        },
        "outputs": {
            "A NAND B": TYPES.LOGIC
        },
    },
    "NOR": {
        "inputs": {
            "A": TYPES.LOGIC,
            "B": TYPES.LOGIC
        },
        "outputs": {
            "A NOR B": TYPES.LOGIC
        },
    },
    "XNOR": {
        "inputs": {
            "A": TYPES.LOGIC,
            "B": TYPES.LOGIC
        },
        "outputs": {
            "A XNOR B": TYPES.LOGIC
        },
    }
}