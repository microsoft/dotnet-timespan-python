import doctest
import math
import tqdm
import dotnet_timespan

MAX_TEST_VAL = 1000000  # maximal value to test. its additive inverse number is the minimal value to test
TEST_STEP = 0.987654321  # difference between consecutive test values. should be a number slightly less than 1.0
TEST_PRECISION = 1e-6  # sufferable absolute difference of the required result when converting

def _test(start, stop, step):
    """
    Iterative test of converting float values to TimeSpan and back to float, verifying the value is kept
    """

    num_vals = int((stop - start) / step)
    stop = start + (num_vals + 1) * step
    test_values = (start + i * step for i in range(num_vals))

    print(
        f"Testing {num_vals} values in range",
        f"{dotnet_timespan.g(start)} : {dotnet_timespan.g(stop)}",
        f"with specifiers {dotnet_timespan.FORMAT_SPECIFIERS}",
    )
    for test_time in tqdm.tqdm(test_values, total=num_vals):
        for timespan_ctor in (dotnet_timespan.c, dotnet_timespan.g, dotnet_timespan.G):
            string_from_float = timespan_ctor(test_time)
            float_from_string = dotnet_timespan.from_string(string_from_float).total_seconds()
            assert math.isclose(test_time, float_from_string, abs_tol=TEST_PRECISION),\
                (test_time, float_from_string, timespan_ctor.func.__name__)
    print("Test passed!")


if __name__ == "__main__":
    doctest.testmod(dotnet_timespan, verbose=True)
    _test(start=-MAX_TEST_VAL, stop=MAX_TEST_VAL, step=TEST_STEP)  # guarantees at least 2*MAX_TEST_VAL values were tested
