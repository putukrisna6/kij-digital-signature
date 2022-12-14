from constant import RSA_KEY_PAIR_BITS, KEY_PAIR_DIR_NAME, \
                        PRIVATE_KEY_FILE_NAME, PUBLIC_KEY_FILE_NAME
from crypto.rsa import PyCryptodomeRSA
import os

class GenerateRSAKeyPair:
    @staticmethod
    def do():
        privateKey = PyCryptodomeRSA.generateKeyPair(RSA_KEY_PAIR_BITS)
        PyCryptodomeRSA.exportKey(
            privateKey,
            os.path.join(
                KEY_PAIR_DIR_NAME,
                PRIVATE_KEY_FILE_NAME
            )
        )
        PyCryptodomeRSA.exportKey(
            privateKey.public_key(),
            os.path.join(
                KEY_PAIR_DIR_NAME,
                PUBLIC_KEY_FILE_NAME
            )
        )