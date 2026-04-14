def get_garden_advice(month, season):
    """
    Returns gardening advice based on the month and season.

    Parameters:
        month (str): The name of the month.
        season (str): The name of the season.

    Returns:
        str: Gardening advice for the given month and season.
    """
    advice_data = {
        ("March", "Spring"): "Start planting vegetables such as carrots, spinach, and lettuce.",
        ("June", "Summer"): "Water plants early in the morning and monitor soil moisture regularly.",
        ("September", "Autumn"): "Prepare your garden for cooler weather by pruning and mulching.",
        ("December", "Winter"): "Protect delicate plants from frost and reduce watering."
    }

    return advice_data.get(
        (month, season),
        "General gardening tip: observe your local climate and water appropriately."
    )


def is_valid_month(month):
    valid_months = ["March", "June", "September", "December"]
    return month in valid_months


def is_valid_season(season):
    valid_seasons = ["Spring", "Summer", "Autumn", "Winter"]
    return season in valid_seasons


def main():
    """
    Main function that asks the user for input, validates it,
    and prints gardening advice.
    """
    month = input("Enter the month: ").strip().title()
    season = input("Enter the season: ").strip().title()

    if not is_valid_month(month):
        print("Invalid month entered. Please use March, June, September, or December.")
        return

    if not is_valid_season(season):
        print("Invalid season entered. Please use Spring, Summer, Autumn, or Winter.")
        return

    advice = get_garden_advice(month, season)
    print("\nGardening Advice:")
    print(advice)


if __name__ == "__main__":
    main()
