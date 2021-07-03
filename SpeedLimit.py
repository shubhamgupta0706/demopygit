def speed(s):
    d = 0
    if s > 70:
        d += int((s-70) / 5)
        print(f'Points: {d}')
    else :
        print('Ok')
    if d >= 12:
        print("License suspended")

speed(86)