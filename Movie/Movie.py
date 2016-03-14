__author__ = 'asee2278'
import webbrowser
import ui

class Movie :
    def __init__(self,title,trailer_youtube_url):
        self.title=title
        self.trailer_youtube_url=trailer_youtube_url
        self.poster_image_url="http://movie.idevcreations.com/uploads//packages-0484761001339357801.jpeg"

    def show_trailer(self):
        webbrowser.open_new_tab(self.trailer_youtube_url)


sex_tape = Movie("sex Tape","https://www.youtube.com/watch?v=WZoe4mMXcv4")
bad_teacher = Movie("bad Teacher","https://www.youtube.com/watch?v=VihlsPKMh4U")

#sex_tape.show_trailer();

list =[sex_tape,bad_teacher]
ui.create_movie_tiles_content(list)
ui.open_movies_page(list)