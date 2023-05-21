import time


# countdown number for a limited time towards an event or personal reference
def countdown(cn, n):
    series = []  # to a series of numbers where the length is n and the sum is N,
    # with each next number multiplied by its position, you can use the following algorithm
    avg = cn // 5

    for x in range(1, 5 + 1):
        series.append(avg * x)
        # series[-1] += N - sum(series)

    x1 = series[0]
    # x2 = series[1]
    # x3 = series[2]
    # x4 = series[3]
    # print(x1)
    # countdown block
    for secs in range(cn, 0, -1):
        print(secs)
        time.sleep(1)

        # code block for the triangle shape
        if secs == x1:
            for i in range(1, n + 1):
                print(' ' * n, end='')
                print('# ' * i)
                n -= 1  # this give it the order, top to bottom
        # elif secs == x3:
        #     for a in range(1, n + 1):
        #         print(' ' * n, end='')
        #         print('% ' * a)
        #         n -= 1

    print('Happy Birthday')


countdown(cn=int(input('enter countdown number > ')), n=int(input('enter range (number) > ')))
