__author__ = 'asee2278'
import webbrowser

class Movie :
    def __init__(self,name,trailerlink):
        self.name=name
        self.trailerlink=trailerlink

    def show_trailer(self):
        webbrowser.open_new_tab(self.trailerlink)


sex_tape = Movie("sex Tape","https://www.youtube.com/watch?v=WZoe4mMXcv4")
bad_teacher = Movie("bad Teacher","https://www.youtube.com/watch?v=VihlsPKMh4U")

sex_tape.show_trailer();