# this is class defination file
# declare the parent and child class with class variables and class methods
#importing webbrowser module to open the browser window for trailer
#and poster images.

import webbrowser


class Video():
    
    """ this class is parent class which provide the information related to video"""    

# init method is a constructor that initializes the data.
# self is the instance(like alaska,bfg,starwar,american_sniper)
# there are 3 arguments- title, duration and quality. They are instance variables

    def __init__(self,title,duration,quality):
        """ this method is constructor for initialize the values of parent class"""
        self.title=title
        self.duration=duration
        self.quality=quality
        
# show_info is a method of class Video. input is self(instance) 
    def show_info(self):
        """ it will take instances of class and print the information of parent class"""
        print ("the title is : "+self.title)
        print ("the duration is: "+self.duration)
        print("the quality is :"+self.quality)

class Movie(Video):
    
    """ this class is child class which provide information related to Movie"""
# init method is constructor for child class(Movie)
# input are movie_storyline,movie_category,movie_director,movie_image,
# movie_trailer,movie_rating along with parent instance variables
# Movie class is inheriting 3 instance variables of Video class
    def __init__(self,title,duration,quality,movie_storyline,movie_category,movie_director,movie_image,movie_trailer,movie_rating):
        """ this method is constructor for initialize the values of child class"""
        Video.__init__(self,title,duration,quality)
        self.storyline=movie_storyline
        self.category=movie_category
        self.director=movie_director
        self.image_url=movie_image
        self.trailer_url=movie_trailer
        self.rating=movie_rating

# the show_info is child class method .
# if this method is called by instance of Movie class, then it will
#display all the info related to this Movie class .
#this is called method overriding
    def show_info(self):
        """ it will take instances of class and print the information of child class"""
        print("the title is :"+self.title)
        print ("the duration is: "+self.duration)
        print("the quality is :"+self.quality)
        print ("the storyline  is: "+self.storyline)
        print("the category is :"+self.category)
        print("the director is :"+self.director)
        print ("the image is: "+self.image)
        print("the trailer is :"+self.trailer)
        print ("the rating is: "+self.rating)

# show _image method will show the poster image of movie class
#inputs are self(instance ) for example- starwar.show_image().
#it will show the starwar movie poster'''
    def show_image(self):
        """ it will take instance of Movie class and show the image of that instance"""
        webbrowser.open(self.image_url)
        
# show _trailer method will show the trailer from youtube link of movie class
    def show_trailer(self):
        """ it will take instance of Movie classs and show the trailer of that instance"""
        webbrowser.open(self.trailer_url)
