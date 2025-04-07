"""Code to Plan a Cozy Tea Party"""

__author__: str = "730772722"


def main_planner(people: int) -> None:
    """Entrypoint to cozy tea party function"""
    print("A Cozy Tea Party for " + str(people) + " People!")
    print("Tea Bags: " + str(tea_bags(people)))
    print("Treats: " + str(treats(people)))
    print("Cost: $" + str(cost(tea_bags(people), treats(people))))


def tea_bags(people: int) -> int:
    """Returns number of tea bags needed"""
    return 2 * people


def treats(people: int) -> int:
    """Returns number of treats needed"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_bags: int, treats: int) -> float:
    """Returns cost of tea and treats"""
    return (tea_bags * 0.5) + (treats * 0.75)


if __name__ == "__main__":
    main_planner(people=int(input("How many guests are attending your tea party? ")))
