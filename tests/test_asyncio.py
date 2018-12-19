import asyncio


# definition of a coroutine
async def coroutine_1():
    print('coroutine_1 is active on the event loop')

    print('coroutine_1 yielding control. Going to be blocked for 4 seconds')
    await asyncio.sleep(1)

    print('coroutine_1 resumed. coroutine_1 exiting')


# definition of a coroutine


async def coroutine_2():
    print('coroutine_2 is active on the event loop')

    print('coroutine_2 yielding control. Going to be blocked for 5 seconds')
    await asyncio.sleep(2)

    print('coroutine_2 resumed. coroutine_2 exiting')


def xtest0():
    # this is the event loop
    loop = asyncio.get_event_loop()

    # schedule both the coroutines to run on the event loop
    loop.run_until_complete(asyncio.gather(coroutine_1(), coroutine_2()))
    # assert 0 is 1
