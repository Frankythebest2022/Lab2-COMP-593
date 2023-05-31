"""
Description:
 Uses a complex data structure to store information about me.

Usage:
 python about_me.py
"""
def main():
    # Step 2: Create a complex data structure that holds information about me
    about_me = {
       'name': 'Frank Choupo',
        'student ID': 10294301,
        'pizza toppings': ['PINEAPPLE', 'SAUSAGE', 'PEPPERONI'],
        'movies': [
            {
                'title': 'The return of the Mommy',
                'genre': 'sci-fi'
            },
            {
                'title': 'The Cosby show',
                'genre': 'comedy'
            },
            {
                'title': 'Hercule',
                'genre': 'fantasy'
            }
        ]
    }

    # Step 3: Print student name and ID
    print_student_name_and_id(about_me)

    # Step 4: Print a bullet list of pizza toppings
    print_pizza_toppings(about_me)

    # Step 5: Add pizza toppings to the data structure
    add_pizza_toppings(about_me, ['MUSHROOMS', 'ONIONS'])
    print_pizza_toppings(about_me)

    # Step 6: Add another movie to the data structure
    add_movie(about_me, 'Rambo', 'Action')

    # Step 7: Print a comma-separated list of movie genres
    print_movie_genres(about_me)

    # Step 8: Print a comma-separated list of movie titles
    print_movie_titles(about_me['movies'])

def print_student_name_and_id(my_info):
    """Prints sentences containing student name and ID

    Args:
        my_info (dict): Data structure containing information about me
    """
    full_name = my_info['name']
    first_name = full_name.split()[0]
    student_id = my_info['student ID']
    print(f"My name is {full_name}, but you can call me Sir {first_name}. \nMy student ID is {student_id}.")


def print_pizza_toppings(my_info):
    """Prints a bullet list of favourite pizza toppings

    Args:
        my_info (dict): Data structure containing information about me
    """
    toppings = my_info['pizza toppings']
    print("\nMy favorite pizza toppings are:")
    for topping in toppings:
        print(f"- {topping}")


def add_pizza_toppings(my_info, toppings):
    """Adds some pizza toppings to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        toppings (list): List of pizza toppings
    """
    my_info['pizza toppings'].extend(toppings)
    my_info['pizza toppings'] = [topping.lower() for topping in my_info['pizza toppings']]
    my_info['pizza toppings'].sort()

def add_movie(my_info, title, genre):
    """Adds a movie to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        title (str): Movie title
        genre (str): Movie genre
    """
    new_movie = {
        'title': title,
        'genre': genre
    }
    my_info['movies'].append(new_movie)

def print_movie_genres(my_info):
    """Prints a sentence listing all favourite movie genres

    Args:
        my_info (dict): Data structure containing information about me
    """
    genres = [movie['genre'] for movie in my_info['movies']]
    genre_list = ", ".join(genres)
    print(f"\nI like to watch {genre_list} movies.")

def print_movie_titles(movie_list):
    """Prints a sentence listing all favourite movie titles

    Args:
        movie_list (list): List of favourite movies
    """
    titles = [movie['title'].title() for movie in movie_list]
    titles_list = ", ".join(titles)
    print(f"\nSome of my favorite movies are {titles_list}!")

if __name__ == '__main__':
    main()