def cache_decorator(func):
    """
    Декоратор, который кэширует результаты вызова функции (LRU)
    :param func: декорируемая функция
    :return: декоратор
    """
    cache = {}
    root = [None, None, None, None]
    root[0] = root[1] = root
    cache_size = 3

    def wrapper(*args):
        link = cache.get(args)
        if link is not None:
            link_prev, link_next, link_args, value = link
            link_prev[1] = link_next
            link_next[0] = link_prev
            last = root[0]
            last[1] = root[0] = link
            link[0] = last
            link[1] = root
            return value
        value = func(*args)
        if len(cache) >= cache_size:
            oldest = root[1]
            next_oldest = oldest[1]
            root[1] = next_oldest
            next_oldest[0] = root
            del cache[oldest[2]]
        last = root[0]
        last[1] = root[0] = cache[args] = [last, root, args, value]
        return value

    return wrapper
