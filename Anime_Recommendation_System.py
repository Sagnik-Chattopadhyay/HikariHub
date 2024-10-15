import requests


GENRES = {
    1: ("Action", 1),
    2: ("Adventure", 2),
    3: ("Comedy", 4),
    4: ("Drama", 8),
    5: ("Fantasy", 10),
    6: ("Horror", 14),
    7: ("Romance", 22),
    8: ("Sci-Fi", 24),
    9: ("Slice of Life", 36)
}

def fetch_anime(type_, genre_id, genre_name):
    """Fetch top-rated anime based on type and genre."""
    url = (
        f"https://api.jikan.moe/v4/anime"
        f"?type={type_}&genres={genre_id}&order_by=score&sort=desc&limit=5"
    )

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json().get('data', [])
        if data:
            print(f"\nTop-rated {type_.capitalize()} in {genre_name} genre:")
            for idx, anime in enumerate(data):
                print(f"{idx + 1}. {anime['title']} (Score: {anime['score']})")
                print(f"   Episodes: {anime['episodes']}, Status: {anime['status']}")
                print(f"   Synopsis: {anime['synopsis'][:100]}...\n")
        else:
            print(f"No {type_} found in the {genre_name} genre.")
    elif response.status_code == 429:
        print("Rate limit exceeded. Please try again later.")
    else:
        print("Error fetching anime data.")
        print("Response:", response.json())  

def main():
    print("Welcome to the Anime Recommendation System!")

    
    while True:
        choice = input("Do you want to watch a 'movie' or 'series'? ").strip().lower()
        if choice in ['movie', 'series']:
            type_ = 'tv' if choice == 'series' else 'movie'  
            break
        else:
            print("Please enter 'movie' or 'series'.")

    
    print("\nSelect a genre:")
    for key, (genre, _) in GENRES.items():
        print(f"{key}. {genre}")

    while True:
        try:
            genre_choice = int(input("Enter the number corresponding to your genre: "))
            if genre_choice in GENRES:
                selected_genre, genre_id = GENRES[genre_choice]
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Please enter a valid number.")

    
    fetch_anime(type_, genre_id, selected_genre)

if __name__ == "__main__":
    main()
