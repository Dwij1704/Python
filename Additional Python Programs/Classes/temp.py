def display_student_info(student):
    first_name = student["full_name"].split()[0]
    print(f"My name is {student['full_name']}, but you can address me as Mr. {first_name}.")
    print(f"My student identification number is {student['student_id']}.")

def display_student_pizza_toppings(student):
    print("My favorite pizza toppings are:")
    for i, topping in enumerate(student["pizza_toppings"]):
        print(f"- {topping}")

def add_pizza_toppings_to_student(student, toppings):
    student["pizza_toppings"].extend(toppings)
    student["pizza_toppings"] = sorted(student["pizza_toppings"], key=lambda x: x.lower())

def display_student_favorite_movies(movies):
    movie_titles = [movie["title"].title() for movie in movies]
    last_title = movie_titles.pop()
    fav_movies_string = ", ".join(movie_titles)
    print(f"A few of my favorite movies are {fav_movies_string} and {last_title}.")

def display_student_movie_genres(student):
    genres = [movie["genre"] for movie in student["movies"]]
    num_genres = len(genres)
    genre_string = ", ".join(genres[:-1]) + " and " + genres[-1] if num_genres > 1 else genres[0]
    print(f"I like to watch movies of genres {genre_string}.")

def main_func():
    student = {
        "full_name": "John Doe",
        "student_id": 12345,
        "pizza_toppings": ["PEPPERONI", "MUSHROOMS", "OLIVES"],
        "movies": [
            {"title": "the godfather", "genre": "crime"},
            {"title": "the Shawshank Redemption", "genre": "drama"}
        ]
    }
    student["movies"].append({"title": "the Dark Knight", "genre": "action"})
    display_student_info(student)
    display_student_pizza_toppings(student)
    add_pizza_toppings_to_student(student, ("SAUSAGE", "BACON"))
    display_student_pizza_toppings(student)
    display_student_movie_genres(student)
    display_student_favorite_movies(student['movies'])

if __name__ == "__main__":
    main_func()