from functools import wraps


def timer(func):
    import time

    @wraps(func)
    def wrapper():
        start = time.time()
        res = func()
        end = time.time() - start
        print('{0}: {1:.3} sec'.format(func.__name__, end))
        return res
    return wrapper


def logger(func):
    import json
    import time

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time() - start
        with open('log_file.txt', 'a+') as log_file:
            o = json.dumps({
                'function': func.__name__,
                'duration': end,
                'arguments': [args, kwargs]})
            log_file.write(o + '\n')
    return wrapper


def type_checker(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        pos = [type(arg).__name__ for arg in args]
        kw = {key: type(val).__name__ for key, val in kwargs.items()}
        print('Positional arguments types: {}\nKeyword arguments types: {}'. format(pos, kw))
        return func(*args, **kwargs)
    return wrapper


def buffer(func):
    buff = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal buff

        if args in [item[0] for item in buff.keys()] \
        and tuple(kwargs.items()) in [item[1] for item in buff.keys()]:
            print('Buffer')
            return buff[(args, tuple(kwargs.items()))]

        print('New arguments')
        buff[(args, tuple(kwargs.items()))] = func(*args, **kwargs)
        return buff[(args, tuple(kwargs.items()))]
    return wrapper


if __name__ == '__main__':

    @buffer
    def test(*args, **kwargs):
        return 10

    print(test(1, 3, 5))
    print(test(1, 3, 4, s=1))
    print(test(1, 3, 4, k=6))
    print(test(1, 3, 4, s=1))
    print(test(1, 3, 4, k=6))
    print(test(1, 3, 5))
