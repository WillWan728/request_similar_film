import spacy

nlp = spacy.load("en_core_web_md")

# Function returning movies a user should watch next if they have watched the Hulk


def find_movie(title):
    """
    Opening movies.txt and returning all lines in the file, as a list where each line is an item in the list object
    Creating a dictionary to access the key (movie title), value (movie description)
    """
    movie_file = open("movies.txt", "r")
    movie_dict = {}
    for line in movie_file:
        line = line.strip()
        key, value = line.split(" :")
        movie_dict[key] = value.strip("\n")

    hulk = nlp(title)
    temp_film = 0

    with open("movies.txt", "r") as movie_file:
        """
        Opening movie.txt again as movie_file
        for loop to compare each film to the hulk and find its similarity  
        find the most similar film to hulk and print as the next film for user to watch
        """
        for film in movie_file:
            similarity = nlp(film).similarity(hulk)
            if similarity > temp_film:
                temp_film = similarity
                closest_film = film
        film_split = closest_film.split(" :")
        print(f"The next movie you should watch is: \n{movie_dict[film_split[0]]}")


compare_hulk = "Will he save their world or destroy it? When the hulk becomes too dangerous for the Earth, " \
               "the illuminati trick Hulk into a shuttle and launch him into space to a planet where the" \
               " Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where" \
               " he is sold into slavery and trained as a gladiator."

find_movie(compare_hulk)
