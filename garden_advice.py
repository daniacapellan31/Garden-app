def get_garden_advice(month, season):
    """
    Returns gardening advice based on the month and season.
    """

    # TODO: Move gardening advice into a dictionary to avoid hardcoded values.
    # TODO: Validate user input for month and season.
    # TODO: Split logic into smaller helper functions for better readability.
    # TODO: Add support for more months and seasons.
    # TODO: Improve documentation and usage examples.

    if month == "March" and season == "Spring":
        return "Start planting vegetables such as carrots, spinach, and lettuce."
    elif month == "June" and season == "Summer":
        return "Water plants early in the morning and monitor soil moisture regularly."
    elif month == "September" and season == "Autumn":
        return "Prepare your garden for cooler weather by pruning and mulching."
    elif month == "December" and season == "Winter":
        return "Protect delicate plants from frost and reduce watering."
    else:
        return "General gardening tip: observe your local climate and water appropriately."


def main():
    month = input("Enter the month: ")
    season = input("Enter the season: ")

    advice = get_garden_advice(month, season)
    print("\nGardening Advice:")
    print(advice)


if __name__ == "__main__":
    main()