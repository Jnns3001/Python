def hanoi(count: int, src: int, mid: int, dest: int) ->  None:
    if count <= 1:
        move(count, src, dest)
        return
    hanoi(count-1, src, dest, mid)
    move(count, src, dest)
    hanoi(count-1, mid, src, dest)
    return

def move(count: int, src: int, dest: int) -> None:
    print("lege %s. Scheibe von %s zu %s") % str(count), str(src), str(dest)
    return

print("lege die Anzahl an Scheiben fest.")
hanoi(int(input()), 1, 2, 3)