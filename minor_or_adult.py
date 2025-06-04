"""A simple script that determines whether a user is an adult or a minor."""

from typing import Callable


def get_age(input_func: Callable[[str], str] = input) -> int:
    """Prompt the user for their age until a valid integer is provided.

    Parameters
    ----------
    input_func : Callable[[str], str], optional
        Function used to obtain input from the user. Defaults to Python's
        built-in ``input`` function. This parameter is provided to make the
        function easier to test.

    Returns
    -------
    int
        The age entered by the user as an integer.
    """

    # Keep asking for age until the user enters a valid integer.
    while True:
        # Request a value from the user.
        age_input = input_func("Enter your age: ")
        try:
            # Try to convert the input to an integer.
            return int(age_input)
        except ValueError:
            # If conversion fails, inform the user and loop again.
            print("Please enter a valid integer for age.")


def is_adult(age: int) -> bool:
    """Return ``True`` if ``age`` represents an adult (18 or older)."""

    return age >= 18


def main(input_func: Callable[[str], str] = input, print_func: Callable[[str], None] = print) -> None:
    """Main program logic for interactive execution.

    Parameters
    ----------
    input_func : Callable[[str], str], optional
        Function used for user input. Defaults to ``input``.
    print_func : Callable[[str], None], optional
        Function used for output. Defaults to ``print``.
    """

    # Ask the user for their name using the provided input function.
    name = input_func("Enter your name: ")
    # Obtain a valid integer age from the user.
    age = get_age(input_func)
    # Decide whether the user is an adult.
    if is_adult(age):
        print_func(f"Hello {name}. You are an adult.")
    else:
        print_func(f"Hello {name}. You are a minor.")


if __name__ == "__main__":
    # Execute the program only when run directly.
    main()
