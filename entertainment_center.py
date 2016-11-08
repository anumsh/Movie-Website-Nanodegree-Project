#this is main file where we create the instances of Movie class
#and run the file to view the movie website page
# we have to import media and fresh_tomatoes python files
import media
import fresh_tomatoes

#below are various instances (alaska,bfg,starwar,american_sniper,
#now_you_can_see_me,the_secret_life_of_pets) of movie class

alaska = media.Movie("Mystery, Alaska",
                     "1 hour 59 mins",
                     "360p",
                     "A publicity stunt turns into the ultimate lopsided"
                     "competition,when the world famous New York Rangers"
                     "face off against the team from Mystery, Alaska",
                     "Drama/Sport",
                     "Jay Roach",
                     "http://www.hollywoodmoviejerseys.com/uploads/1/0/2/3/10237892/3921667.jpg",  # noqa
                     "https://www.youtube.com/watch?v=a80x06Wn91U",
                     "R")

bfg = media.Movie("The BFG",
                  "1 hour 57 mins",
                  "180p",
                  "Ten-year-old Sophie is in for the adventure"
                  "of a lifetime when she meets the Big Friendly Giant",
                  "Fantasy",
                  "Steven Spielberg",
                  "https://upload.wikimedia.org/wikipedia/en/thumb/a/af/The_BFG_poster.jpg/220px-The_BFG_poster.jpg", # noqa
                  "https://www.youtube.com/watch?v=VG5MtenlP-A",
                  "PG")

starwar = media.Movie("Star Wars",
                      "2 hour 5 mins",
                      "360p",
                      "The Imperial Forces -- under orders from cruel"
                      "Darth Vader (David Prowse) -- hold Princess Leia"
                      "(Carrie Fisher) hostage, in their efforts to quell"
                      "the rebellion against the Galactic Empire.",
                      "Science Fiction",
                      "George Lucas",
                      "http://ia.media-imdb.com/images/M/MV5BOTAzODEzNDAzMl5BMl5BanBnXkFtZTgwMDU1MTgzNzE@._V1_UY1200_CR91,0,630,1200_AL_.jpg", # noqa
                      "https://www.youtube.com/watch?v=2gCbnwavkKc",
                      "PG")


american_sniper = media.Movie("American Sniper",
                              "2 hour 13 mins",
                              "270p",
                              "U.S. Navy SEAL Chris Kyle (Bradley Cooper) takes"
                              "his sole mission -- protect his comrades -- to"
                              "heart and becomes one of the most lethal"
                              "snipers in American history.",
                              "Drama Film",
                              "Clint Eastwood",
                              "http://wp.production.patheos.com/blogs/lookingcloser/files/2015/02/american-sniper-poster.jpg", # noqa
                              "https://www.youtube.com/watch?v=NTya9A4O9Ws",
                              "R")


now_you_can_see_me = media.Movie("NOW YOU CAN SEE ME 2",
                                 "2 hour 9 mins",
                                 "270p",
                                 "One year after outwitting the FBI and winning"
                                 "the public's adulation with their magic spectacles"
                                 "the remaining members of the Four Horsemen"
                                 "are in hiding, awaiting further instructions from"
                                 "the Eye, the secret society of magicians they've"
                                 "been recruited into.",
                                 "Thriller",
                                 "Jon M. Chu",
                                 "http://www.impawards.com/2016/posters/now_you_see_me_two_ver17.jpg", # noqa
                                 "https://www.youtube.com/watch?v=JzZh8kJJwe4",
                                 "PG-13")

the_secret_life_of_pets = media.Movie("The Secret Life of Pets",
                                 "1 hour 30 mins",
                                 "180p",
                                 "One year after outwitting the FBI and winning"
                                 "the public's adulation with their magic"
                                 "spectacles the remaining members of the Four"
                                 "Horsemen are in hiding, awaiting further"
                                 "instructions from the Eye, the secret society"
                                 "of magicians they've been recruited into.",
                                 "Comedy",
                                 "Chris Renaud",
                                 "http://www.birthdaydirect.com/images/59902-the-secret-life-of-pets-tote-bag.jpg", # noqa
                                 "https://www.youtube.com/watch?v=1UXWIVAIimU",
                                 "PG")



# we create a list of instances of movie class and assign it to movies variable
movies = [alaska,bfg,starwar,american_sniper,
          now_you_can_see_me,the_secret_life_of_pets]

# calling open_movies_page method to view movie website
# input is  list of all the instances
fresh_tomatoes.open_movies_page(movies)

# print media.Movie.show_image.__doc__
#(above line is one example how to read the documentation of
#function of Movie class)
