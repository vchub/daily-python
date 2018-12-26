# def count_down() -> None:
#     try:
#         while True:
#             i = yield
#             print('T-minus', i)
#     except GeneratorExit as e:
#         print('Kaboon')


def count_down(i) -> None:
    # init
    self = yield
    cd2 = count_down_2()
    cd2.send(None)
    cd2.send(self)

    print('\ncd2 in count_down: ', cd2)
    j = 5
    while i > 0:
        print('count_down: ', i)
        cd2.send(i - 1)
        i = yield

        # guard
        j -= 1
        if j < 0:
            break


def count_down_2() -> None:
    # init
    cd1 = yield
    print('\ncd1 in count_down_2: ', cd1)

    i = yield
    j = 5
    while i > 0:
        print('count_down_2: ', i)
        cd1.send(i - 1)
        i = yield

        # guard
        j -= 1
        if j < 0:
            break


def run_friend(i: int) -> None:
    cd1 = count_down(i)
    cd1.send(None)
    cd1.send(cd1)

    # cd2.send(None)
    #
    # cd2.send(cd1)


def xtest0():
    run_friend(5)

    # for i in range(5):
    #     cd.send(i)
