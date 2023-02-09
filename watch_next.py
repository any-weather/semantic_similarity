import spacy

# specifying the model we want to use.
nlp = spacy.load('en_core_web_md')

# opening movies file and storing all movies in movie_list
with open("movies.txt", "r", encoding="UTF-8") as movies:
    movie_list = [line for line in movies.readlines()]
    
# descrition of a watched movie
watched = ('''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk into a shuttle and launch him into space to aplanet where the Hulk can live in peace. 
Unfortunately, Hulk land on theplanet Sakaar where he is sold into slavery and trained as a gladiator.''')

def movie_advisor(description):
    '''
    movie_advisor analyses the similarity of the description of the watched movie and the list of available moview and prints out he name of the most similar one as a suggestion
    param: descrition: takes a description of the watched movie as an argument
    '''
    #list of numbers representing similarity of each movie in the file 
    similarity_list = [nlp(token).similarity(nlp(description)) for  token in movie_list]

    # maximum number (representin maximum similarity)
    max_sim = max(similarity_list)

    # getting the index of the maximum value to then get the moie with tht index from movie list
    for num, item in enumerate(similarity_list):
        if item == max_sim:
            index = num

    # getting the maximum match movie and splitting it into a list to only print the name
    match = movie_list[index]
    match_list = match.split()


    print(f"Based on your recent watch history, you might like {' '.join(match_list[0:2])}")

movie_advisor(watched)
    