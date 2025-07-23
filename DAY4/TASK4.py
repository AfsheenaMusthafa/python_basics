movies = []

while True:
    print("\nTop 5 Movies Menu:")
    print("1. Add Movie")
    print("2. Show Movies by Rating")
    print("3. Highest Rated Movie")
    print("4. Lowest Rated Movie")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        if len(movies) < 5:
            name = input("Enter movie name: ")
            rating = int(input("Enter rating (1-10): "))
            movies.append([name, rating])
            print("Movie added!")
        else:
            print("You can only add 5 movies.")

    elif choice == "2":
        if not movies:
            print("No movies added yet.")
        else:
            print("\nMovies by Rating:")
            for movie in sorted(movies, key=lambda x: x[1], reverse=True):
                print(movie[0], "-", movie[1], "/10")

    elif choice == "3":
        if movies:
            best = movies[0]
            for m in movies:
                if m[1] > best[1]:
                    best = m
            print("Highest Rated:", best[0], "-", best[1], "/10")
        else:
            print("No movies yet.")

    elif choice == "4":
        if movies:
            worst = movies[0]
            for m in movies:
                if m[1] < worst[1]:
                    worst = m
            print("Lowest Rated:", worst[0], "-", worst[1], "/10")
        else:
            print("No movies yet.")

    elif choice == "5":
        print("Bye!")
        break

    else:
        print("Invalid choice.")


