from random import choice
from string import ascii_letters
import zxcvbn


async def generate_password(level: str):
    symbol_str = "!@#$%^&*()_-+={[]}?/|!"
    numbers = "1234567890"
    password = ""

    if level == "Easy":
        for item in range(8):
            password += choice(numbers)

    elif level == "Medium":
        for item in range(8):
            password += choice(numbers) + choice(ascii_letters)

    elif level == "Hard":
        for item in range(8):
            password += choice(numbers) + choice(ascii_letters) + choice(symbol_str)

    else:
        return False

    return password


async def check_password(password: str):
    result = zxcvbn.zxcvbn(password)
    crack_times_seconds = result['crack_times_seconds']['offline_slow_hashing_1e4_per_second']

    day = crack_times_seconds // (24 * 3600)
    hour = crack_times_seconds // (24 * 3600) // 3600
    minute = crack_times_seconds // (24 * 3600) // 60

    return f"Parolmi buzishga ketadigon taxminiy vaqt: {day} kun {hour} soat {minute} minut"