def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_one(temp_str: str) -> None:
    print(f"Input data is '{temp_str}'")
    try:
        temp = input_temperature(temp_str)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()
    test_one("25")
    print()
    test_one("abc")
    print()
    print("All tests completed - program didn't crash!")


test_temperature()
