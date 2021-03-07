load("@rules_python//python:defs.bzl", "py_binary")
load("@pip//:requirements.bzl", "requirement")

py_binary(
    name = "degiro_query",
    python_version = "PY3",
    srcs = ["degiro_query.py"],
    deps = [
        requirement("requests"),
        requirement("argparse"),
        # Dependency taken from https://github.com/lolokraus/DegiroAPI/tree/master/degiroapi.
        "//deps/degiroapi",
    ],
)

py_test(
    name = "degiro_query_test",
    python_version = "PY3",
    srcs = ["degiro_query_test.py"],
    deps = [
        requirement("requests"),
        ":degiro_query",
    ],
)