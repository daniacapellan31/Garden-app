def get_garden_advice(month, season):
    """
    Returns gardening advice based on the month and season.
    """

    # TODO: Validate user input for month and season.
    # TODO: Add support for more months and seasons.
    # TODO: Improve documentation and usage examples.

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


def main():
    month = input("Enter the month: ")
    season = input("Enter the season: ")

    advice = get_garden_advice(month, season)
    print("\nGardening Advice:")
    print(advice)


if __name__ == "__main__":
    main()
