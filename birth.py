def print_ascii_cake():
    cake = r"""
        🎂🍰🎂🍰🎂
      🍰           🍰
    🎂  H A P P Y  🎂
      🍰     B I R T H D A Y   🍰
        🎂         🎂
    """
    print(cake)

def wish_birthday(name):
    print_ascii_cake()
    print(f"\nWishing you a fantastic birthday, {name}!\nMay your day be filled with joy and wonderful moments. 🎉🎈🎁")

# Replace 'Emily' with the person's name you want to wish
person_name =input("eneter your friends name")
wish_birthday(person_name)
