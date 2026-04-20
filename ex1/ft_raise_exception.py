def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    elif temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    return temp


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
    test_one("100")
    print()
    test_one("-50")
    print()
    print("All tests completed - program didn't crash!")


test_temperature()
