def police_check(age: int) -> bool:
    return age >= 18


if police_check(21):
    print("you may pass")
else:
    print("Pay a fine.")
