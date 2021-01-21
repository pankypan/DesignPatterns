import time, copy


class A:
    def __init__(self):
        time.sleep(3)


if __name__ == "__main__":
    import time

    s = time.time()
    a1 = A()
    a2 = A()
    a3 = A()
    e = time.time()
    print(e - s)

    s = time.time()
    b1 = copy.copy(a1)
    b2 = copy.copy(a1)
    b3 = copy.copy(a1)
    e = time.time()
    print(e - s)
