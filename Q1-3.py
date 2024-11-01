# START Q1
id: str = input("ID:")
name1: str = input("first name:")
name2: str = input("last name:")
height: float = float(input("height:"))
bithday: int = int(input("year of birth:"))
print(f"id: {id}, name: {name1} {name2}, height: {height}, yeat-of-bith: {bithday}")
# END Q1

# START Q2
score: int = int(input("score:"))

if 0 > score < 100:
    print("grade illegal")
elif 0 <= score <= 40:
    print("try harder next time...")
elif 41 <= score <= 60:
    print("you're getting there, need some more work")
elif 61 <= score <= 80:
    print("good pretty")
elif 81 <= score <= 95:
    print("!awesome")
elif 96 <= score <= 100:
    print("excellent!!! You're a Star!")
# END Q2

# START Q3
volume: int = int(input('vol. level:'))
match volume:
    case 0:
        print('mute')
    case 1:
        print('very quiet')
    case 2:
        print('very quiet')
    case 3:
        print('quiet')
    case 4:
        print("moderately quiet")
    case 5:
        print("medium ")
    case 6:
        print("moderately loud")
    case 7:
        print("loud")
    case 8:
        print("very loud")
    case 9:
        print("extremely loud")
    case 10:
        print("extremely loud")
# END Q3
