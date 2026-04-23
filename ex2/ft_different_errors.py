def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "hello" + 5


def test_one(number: int) -> None:
    print(f"Testing operation {number}...")
    try:
        garden_operations(number)
        print("Operation completed successfully")
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print(f"Caught {e.__class__.__name__}: {e}")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    test_one(0)
    test_one(1)
    test_one(2)
    test_one(3)
    test_one(4)
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
