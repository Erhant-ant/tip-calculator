from typing import Tuple


ALLOWED_TIPS = {10, 12, 15}


def calculate_split_amount(bill: float, tip_percentage: int, split_count: int) -> Tuple[float, float]:
    """Return total cost and per-person payment."""
    tip_amount = bill * (tip_percentage / 100)
    total_cost = bill + tip_amount
    each_person = total_cost / split_count
    return total_cost, each_person


def get_positive_float(prompt: str) -> float:
    """Prompt until user enters a positive float."""
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            if value <= 0:
                print("Please enter a value greater than 0.")
                continue
            return value
        except ValueError:
            print("Invalid number. Please enter a valid numeric value.")


def get_valid_tip(prompt: str) -> int:
    """Prompt until user enters one of ALLOWED_TIPS."""
    while True:
        raw = input(prompt).strip()
        if not raw.isdigit():
            print("Tip percentage must be a whole number.")
            continue

        value = int(raw)
        if value not in ALLOWED_TIPS:
            print("Please choose one of: 10, 12, 15.")
            continue

        return value


def get_valid_split_count(prompt: str) -> int:
    """Prompt until user enters an integer >= 1."""
    while True:
        raw = input(prompt).strip()
        if not raw.isdigit():
            print("Number of people must be a whole number.")
            continue

        value = int(raw)
        if value < 1:
            print("Number of people must be at least 1.")
            continue

        return value


def main() -> None:
    print("\nWelcome to the Tip Calculator!\n")

    bill = get_positive_float("Total meal price: ")
    tip_percentage = get_valid_tip("How much tip would you like to give? (10, 12, or 15): ")
    split_count = get_valid_split_count("How many people to split the bill?: ")

    total_cost, each_person = calculate_split_amount(bill, tip_percentage, split_count)

    print(f"\nTotal cost: ${total_cost:.2f}")
    print(f"Tip percentage: {tip_percentage}%")
    print(f"Each person should pay: ${each_person:.2f}")


if __name__ == "__main__":
    main()
