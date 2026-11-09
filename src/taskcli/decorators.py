import functools , logging

log = logging.getLogger('taskcli')

def logged(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kwargs):
        log.info('running %s',fn.__name__)
        try:
            return fn(*args,**kwargs)
        except Exception:
            log.exception('%s failed',fn.__name__)
            raise
    return wrapper
