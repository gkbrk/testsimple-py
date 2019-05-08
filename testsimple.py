def plan(tests=0):
    print(f"1..{tests}")


__testsimple_test_num = 0


def ok(condition, msg=""):
    global __testsimple_test_num
    __testsimple_test_num += 1
    prefix = "not ok"

    if condition:
        prefix = "ok"

    print(f"{prefix} {__testsimple_test_num} - {msg}")


def done_testing():
    print(f"1..{__testsimple_test_num}")


def diag(*args):
    print("#", *args)
