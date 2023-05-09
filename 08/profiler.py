import cProfile
import io
import pstats


def profile_deco(func):
    profiles = {}

    def wrapped(*args, **kwargs):
        pr = profiles.setdefault(func, cProfile.Profile())
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()
        return result

    def print_stats():
        s = io.StringIO()
        sort_by = "cumulative"
        for func, pr in profiles.items():
            ps = pstats.Stats(pr, stream=s).sort_stats(sort_by)
            ps.print_stats()
        print(s.getvalue())

    wrapped.print_stat = print_stats
    return wrapped


@profile_deco
def add(a, b):
    return a + b


@profile_deco
def sub(a, b):
    return a - b


add(1, 2)
sub(4, 5)
add(4, 5)


add.print_stat()
sub.print_stat()
