import timeit
from multiprocessing.dummy import Pool as ThreadPool

import requests

urls = [
    'http://www.python.org', 'http://www.python.org/about/',
    'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
    'http://www.python.org/doc/', 'http://www.python.org/download/',
    'http://www.python.org/getit/', 'http://www.python.org/community/',
    'https://wiki.python.org/moin/', 'http://planet.python.org/',
    'https://wiki.python.org/moin/LocalUserGroups',
    'http://www.python.org/psf/', 'http://docs.python.org/devguide/',
    'http://www.python.org/community/awards/'
    # etc..
]


def exec(th_num):
    # Make the Pool of workers
    pool = ThreadPool(th_num)
    # Open the urls in their own threads
    # and return the results
    # results = pool.map(urllib3.urlopen, urls)
    results = pool.map(requests.get, urls)
    # close the pool and wait for the work to finish
    pool.close()
    pool.join()
    return results
    # print(results)


def xtest():
    for th_num in range(4, len(urls) + 2):
        print(f'th_num: {th_num}', timeit.timeit(
            lambda: exec(th_num), number=1))
