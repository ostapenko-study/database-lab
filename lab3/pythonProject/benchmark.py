def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        result = None
        try:
            result = func(*args, **kwargs)
        except Exception as err:
            print('ERROR: ', err)
        end = time.time()
        print('[*] {} | Executing time: {} sec.'.format(func.__name__, end - start))
        return result

    return wrapper
