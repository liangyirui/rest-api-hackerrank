import requests

URL = "https://jsonmock.hackerrank.com/api/food_outlets"


def highest_rated_restaurant(city: str, vote_counts) -> str:
    """
    Fetch resturants data from given URL
    Returns the resturant's name by the following conditions:
    1. Matches the given city
    2. votes under user_rating must be greater than or equal to vote_counts
    3. Return the restaurant's name with the highest rating
    3. If there is a tie, return the one with higher user votes
    """
    url = f"{URL}?city={city}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Something is wrong")
        return ""
    data = response.json()
    total_pages = data["total_pages"]
    candidate = ""
    max_rating = 0
    candidate_votes = 0
    for page_no in range(1, total_pages + 1):
        _url = f"{url}&page={page_no}"
        _response = requests.get(_url)
        if _response.status_code != 200:
            print("Something is wrong")
            return ""
        restaurants = _response.json()["data"]
        if not restaurants:
            continue
        for restaurant in restaurants:
            if (
                restaurant["city"].lower() != city.lower()
                or restaurant["user_rating"]["votes"] < vote_counts
            ):
                continue
            if restaurant["user_rating"]["average_rating"] > max_rating:
                candidate = restaurant["name"]
                candidate_votes = restaurant["user_rating"]["votes"]
            elif (
                restaurant["user_rating"]["average_rating"] == max_rating
                and restaurant["user_rating"]["votes"] > candidate_votes
            ):
                candidate = restaurant["name"]
                candidate_votes = restaurant["user_rating"]["votes"]
    return candidate


if __name__ == "__main__":
    candidate = highest_rated_restaurant("houston", 200)
    print(candidate)
