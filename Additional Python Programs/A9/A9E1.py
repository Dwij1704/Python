import sys
import re
def clean_string(string):
    res=re.sub(' +', ' ', string)
    return res
def get_song_desc(song_name,artist_name):
    """input the folowing in the command line: python A9E1.py ' bLindIng StaRs ' ' The   Weeknd ' """
    res="The song is "+str(song_name.upper())+" by "+str(artist_name.capitalize())
    return res
def get_movie_desc(movie_name,director,actor):
    """input the folowing in the command line: python A9E1.py ' star WARS ' ' george lucas ' ' MARK HamiLL ' """
    """input the folowing in the command line: python A9E1.py ' saVitA Bhabi-2 ' ' NickS    indian ' ' dwIj Patel ' """
    movie_name=re.sub(' +', ' ', sys.argv[1])
    director=re.sub(' +', ' ', sys.argv[2])
    actor=re.sub(' +', ' ', sys.argv[3])
    if any(chr.isdigit() for chr in movie_name):
        res="The movie sequel is \""+str(movie_name.title())+"\", directed by "+str(director.title())+" starring "+str(actor.title())
    else:
        res="The movie is \""+str(movie_name.title())+"\", directed by "+str(director.title())+" starring "+str(actor.title())
    return res
def main():
    l=len(sys.argv)
    if l-1==1:
        print(clean_string(sys.argv[1]))
    elif l-1==2:    
        song_name=re.sub(' +', ' ', sys.argv[1])
        artist_name=re.sub(' +', ' ', sys.argv[2])
        print(get_song_desc(song_name,artist_name))
    elif l-1==3:
        movie_name=re.sub(' +', ' ', sys.argv[1])
        director=re.sub(' +', ' ', sys.argv[2])
        actor=re.sub(' +', ' ', sys.argv[3])
        print(get_movie_desc(movie_name,director,actor))
    else:
        print("Error: Missing Parameters")
main()