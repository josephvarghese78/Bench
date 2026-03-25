def task(name=None, enabled=True, weight=1):

    def decorator(func):
        func.enabled=enabled
        func.is_task=True
        func.test_name=name if name else func.__name__
        func.weight=weight
        return func

    return decorator

