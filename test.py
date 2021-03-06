from playLA.Vector import Vector

if __name__ == "__main__":
    vec = Vector([2, 5])
    print(vec, len(vec))
    print("vec[0] = {}, vec[1] = {}".format(vec[0], vec[1]))

    vec2 = Vector([3, 1])
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))

    print("{} * {} = {}".format(vec, 3, vec * 3))
    print("{} * {} = {}".format(3, vec, 3 * vec))

    print("+{} = {}".format(vec, +vec))
    print("-{} = {}".format(vec, -vec))

    zero = Vector.zero(2)
    print(zero)
    print("{} + {} = {}".format(vec, zero, vec + zero))

    print("norm({}) = {}".format(vec, vec.norm()))

    print("normalize {} is {}".format(vec, vec.normalize()))
    print(vec.normalize().norm())

    try:
        zero.normalize()
    except ZeroDivisionError:
        print("Cannot normalize zero vector {}.".format(zero))