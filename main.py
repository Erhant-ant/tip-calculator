from typing import Dict, Optional, Tuple


PRESET_TIPS: Dict[str, float] = {"1": 10.0, "2": 12.0, "3": 15.0}


def calculate_split_amount(bill: float, tip_percentage: float, split_count: int) -> Tuple[float, float, float]:
    """Return tip amount, total cost, and per-person payment."""
    tip_amount = bill * (tip_percentage / 100)
    total_cost = bill + tip_amount
    each_person = total_cost / split_count
    return tip_amount, total_cost, each_person


def parse_positive_float(raw_value: str) -> Optional[float]:
    """Parse a string into a float greater than zero."""
    try:
        value = float(raw_value)
    except ValueError:
        return None
    if value <= 0:
        return None
    return value


def parse_positive_int(raw_value: str) -> Optional[int]:
    """Parse a string into an integer greater than zero."""
    try:
        value = int(raw_value)
    except ValueError:
        return None
    if value <= 0:
        return None
    return value


def get_positive_float(prompt: str) -> float:
    while True:
        value = parse_positive_float(input(prompt).strip())
        if value is None:
            print("Please enter a valid number greater than 0.")
            continue
        return value


def get_positive_int(prompt: str) -> int:
    while True:
        value = parse_positive_int(input(prompt).strip())
        if value is None:
            print("Please enter a whole number greater than 0.")
            continue
        return value


def get_tip_percentage() -> float:
    print("\nChoose a tip option:")
    print("  1) 10%")
    print("  2) 12%")
    print("  3) 15%")
    print("  4) Custom tip")

    while True:
        choice = input("Select 1, 2, 3, or 4: ").strip()
        if choice in PRESET_TIPS:
            return PRESET_TIPS[choice]
        if choice == "4":
            # Custom tip uses the same positive-number validation as bill input.
            return get_positive_float("Enter custom tip percentage: ")
        print("Please choose one of the available options (1, 2, 3, or 4).")


def print_summary(bill: float, tip_percentage: float, tip_amount: float, total_cost: float, each_person: float, split_count: int) -> None:
    print("\n" + "-" * 34)
    print("Bill summary")
    print("-" * 34)
    print(f"Bill amount         : ${bill:.2f}")
    print(f"Tip percentage      : {tip_percentage:.2f}%")
    print(f"Tip amount          : ${tip_amount:.2f}")
    print(f"Total with tip      : ${total_cost:.2f}")
    print(f"Split between people: {split_count}")
    print(f"Each person pays    : ${each_person:.2f}")
    print("-" * 34)


def main() -> None:
    print("\nWelcome to the Tip Calculator")
    print("Let's quickly split your bill.\n")

    bill = get_positive_float("Total meal price: ")
    tip_percentage = get_tip_percentage()
    split_count = get_positive_int("How many people to split the bill?: ")

    tip_amount, total_cost, each_person = calculate_split_amount(bill, tip_percentage, split_count)
    print_summary(bill, tip_percentage, tip_amount, total_cost, each_person, split_count)


if __name__ == "__main__":
    main()
