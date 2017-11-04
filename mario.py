def mario():
    """
    Input: integer [1:23]
    draws the pyramid from the Mario videogame to the specified height.
    """
    height = -1
    while (height > 23 or height < 0):
        height = int(input("Height: "))
    for blocks in range(2, height + 2):
        print('{}{}  {}'.format(' ' * (height + 1 - blocks),
                                '#' * blocks, '#' * blocks))

if __name__ == "__main__":
    mario()
