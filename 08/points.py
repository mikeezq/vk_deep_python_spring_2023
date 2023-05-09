import cProfile
import io
import pstats
import sys
import weakref
from memory_profiler import profile


class Helper(list):
    pass


class Points3d:
    name = "Default Points class"

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Points3dSlots:
    __slots__ = ("x", "y", "z")
    name = "Slots Points class"

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Points3dWf:
    name = "Weakrefs Points class"

    def __init__(self, x, y, z):
        self.x = weakref.ref(x)
        self.y = weakref.ref(y)
        self.z = weakref.ref(z)


@profile  # delete for check timings
def create_points(point, count):
    x_values = [Helper([i]) for i in range(count)]
    y_values = [Helper([i + 1]) for i in range(count)]
    z_values = [Helper([i + 2]) for i in range(count)]

    points = [point(x, y, z) for x, y, z in zip(x_values, y_values, z_values)]
    for i in points:
        i.x = 1
        i.y = 2
        i.z = 3


def timing(point, count):
    pr = cProfile.Profile()
    pr.enable()

    create_points(point, count)

    pr.disable()
    s = io.StringIO()
    sort_by = "cumulative"
    ps = pstats.Stats(pr, stream=s).sort_stats(sort_by)
    ps.print_stats()

    print(f"{point.name=}:")
    print(s.getvalue())


if __name__ == "__main__":
    args = sys.argv[1:]
    classes = {"1": Points3d, "2": Points3dSlots, "3": Points3dWf}
    point_class = classes[args[0]]
    timing(point_class, int(args[1]))
