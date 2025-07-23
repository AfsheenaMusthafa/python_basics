movies = []

while True:
    print("\nTop 5 Movies")
    print("1. Add movie")
    print("2. Show movies by rating")
    print("3. Show highest rated movie")
    print("4. Show lowest rated movie")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        if len(movies) < 5:
            name = input("Enter movie name: ")
            rating = int(input("Enter rating (1-10): "))
            movies.append([name, rating])
            print("Movie added!")
        else:
            print("You can only add 5 movies.")

    elif choice == "2":
        for i in range(len(movies)):
            for j in range(i + 1, len(movies)):
                if movies[i][1] < movies[j][1]:
                    movies[i], movies[j] = movies[j], movies[i]
        print("Movies sorted by rating:")
        for m in movies:
            print(m[0], "-", m[1])

    elif choice == "3":
        if movies:
            highest = movies[0]
            for m in movies:
                if m[1] > highest[1]:
                    highest = m
            print("Highest rated movie:", highest[0], "-", highest[1])
        else:
            print("No movies added yet.")

    elif choice == "4":
        if movies:
            lowest = movies[0]
            for m in movies:
                if m[1] < lowest[1]:
                    lowest = m
            print("Lowest rated movie:", lowest[0], "-", lowest[1])
        else:
            print("No movies added yet.")

