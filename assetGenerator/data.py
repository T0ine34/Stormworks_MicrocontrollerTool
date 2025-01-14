from enum import StrEnum

class TYPES(StrEnum):
    LOGIC = 'logic'
    NUMBER = 'number'
    COMPOSITE = 'composite'
    VIDEO = 'video'
    AUDIO = 'audio'

COLORS = {
    TYPES.LOGIC : (255, 0, 0),
    TYPES.NUMBER : (0, 255, 0),
    TYPES.COMPOSITE : (129, 20, 196),
    TYPES.VIDEO : (0, 255, 255),
    TYPES.AUDIO : (189, 126, 43)
}

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