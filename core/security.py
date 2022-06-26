from tkinter.messagebox import RETRY
from asyncpg import DeprecatedFeature
from passlib.context import CryptContext

CRIPTO = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def check_pass(_pass: str, hash: str) -> bool:
    return CRIPTO.verify(_pass, hash)

def generate_hash_pass(_pass: str) -> str:
    return CRIPTO.hash(_pass)