
import random

"""
Bumbler! 
A program in python which tries to provide recommendations to 
users inputs but usually messes it up.
(Note: The messing up is intentional and in good fun. :D)  

Milestone 1 : Setting up the lists and the various elements in them.
Milestone 2 : Checking the user input and asking for fresh input if input is incorrect.
Milestone 3 : Setting up a global list for all lists. 
Milestone 4 : Creating the various fucntions.
Milestone 5 : Asking for user feedback.
Milestone 6 : Presenting a dad joke in case the user is unhappy.
"""

# Milestone 1 : Setting up the list and populating them with elements.

Movie_genre = ['Action','Comedy','Drama','Fantasy','Horror','Romance','Thriller']
Movie_list = ['Die Hard','Red','Taken','The Mask','Hangover','Dumb and Dumber',
              'Shawshank Redemption','Godfather','Schindlers List','Lord of the Rings','Star Wars','Dune',
              'The Ring','The Exorcist','Baskin','Noroi','Pretty Woman','Notebook','La La Land',
              'The Silence of the Lambs','Inception','Gone Girl']
Books_genre= ['Fantasy','Horror','Mystery','Thriller','Romance','Science Fiction',
              'Self Help','Young Adult']
Books_list = ['Eragon','LOTR','Stormlight Archive','Dracula','The Shining',
              'The Shadow over Innsmouth','The hound of Baskerville','Murder on the Orient Express',
              'A Pocket full of Rye','Bourne Identity','Lost Symbol','Are you afraid of the dark',
              'Pride and Prejudice','The fault in our stars','A walk to remember', 'Dear John',
              'I Robot','The Hitchhikkers guide to the galaxy','Do Andorids dream of electronic sheeps',
              'The Monk who sold his ferrari','The subtle art of not giving a F**k','How to win friends and influence people',
              'Twilight Saga','Hunger Games','Harry Potter']
Music_genre = ['Pop','Rock','Blues','Rap','R&B','Metal','Jazz','Phonk','EDM','Classical']
Music_list = ['Espresso','Cardigan','Perfect','Let her Go','Riders on the storm',
              'Another one bites the dust','Hotel California','Playing God','Cocaine','Wonderful Tonight','Lucille',
              'Stan','Riding Dirty','C.R.E.A.M','In da club','Gangsters Paradise','Get low','Fallin','Blinding Lights',
              'The Painkiller','Fuel','Through the Fire and Flames','Take Five','So What','My Favourite Things',
              'Murder on my mind','Gigachad Theme','Rave', 'Close Eyes', 'Divenire','River flows in you',
              'Asturias','Four Seasons']
Cuisine_gnere = ['Korean','Chinese','Japanese','Indian','Middle East','Mediterranean','Continental','Latin American']
Cusine_list = ['Bibimbap','Kimchi Jjigae','Peking Duck', 'Kung-Pao chicken','Tonkotsu Ramen','Nigiri','Mysore Dosa with Sambar','Chicken Tikka Masala with Naan bread',
               'Shakshuka','Falafel Shawarma', 'Paella','Mousaka','Chicken Parmesan','Asparagus au gratin',
               'Pupusas','Feijoada']
Workout_genre = ['Bodyweight', 'Calisthenics', 'Yoga', 'Crossfit', 'Cardio']
Workout_list = ['Bench press','Deadlift', 'Archer pushups','Jumping Jacks','Downward dog','Cobra pose','Box Jump',
                'Double Unders', 'Swimming','Cycling']
Dad_Joke = ['Why did the sacrecrow win an award? Because it was outstanding in its field!','How was the restaurent on the moon? Good food, no atmosphere.',
            'The adjective for metal is mettalic but not for iron...which is ironic.','Any clue as to who built King Arthurs Round Table? Sir Cumference.',
            'Did you watch that documentary about beavers? Best "dam" docu I ever seen!', 'Most puns make me feel numb but maths pun make me feel number.',
            'Justice is a dish best served cold. If it were warm, it would be justwater.']
Conclude = ['Bye', 'Au revoir', 'Adiós', 'Chao', 'Tschüss', 'Arrivederci', 'Alvida', 'Sayonara', 'Annyeong']

            
def main():
    
    print("Hello!. I am JUMBLE-3, your concierge developed at Mumford.")
    print("I can provide you with movie, music, books,food and workout recommendations.")
    print("Enter Movie for movie recommendations.")
    print("Enter Music for music recommendations.")
    print("Enter Books for book recommendations.")
    print("Enter Food for cuisine recommendation.")
    print("Enter Exercise for workout recommendation.")
    print("Remember: to err is Bot, to forgive is Human :p ")
    user_choice = input(':>>>  ') 
    
    # Milestone 2 : Checking the input for correctness. 
    
    choices = ['Movie','Music','Books','Food','Exercise']
    if user_choice not in choices: 
        print('Please enter relevant keywords')
        print()
        new_choice = input("Enter the correct option, please:>>> ")
        user_choice = new_choice

    if user_choice == 'Movie': # movie
        suggestion = musicbasedsuggestion() # will suggest a music in place of movie
    elif user_choice == 'Music': # music
        suggestion = cuisinebasedsuggestion() # will suggest a food in place of music
    elif user_choice == 'Books': # books
        suggestion = workoutbasedsuggestion() # will suggest an exercise in place of book
    elif user_choice == 'Food':# cuisine
        suggestion = bookbasedsuggestion() # will suggest a book in place of food
    elif user_choice == 'Exercise': #workout
        suggestion = moviebasedsuggestion() # suggest a movie in place of a workout
    
    
    print(suggestion)
    print()

    # Milestone 5 : Checking for user feedback.

    print("Are you satisfied with my response? :D ")
    print()
    response = str(input("Enter Y for yes and N for no: "))
    print()
    if response == "Y":
        print("Thank you! Have a nice day!")
    else:
        print("Welp! Here's something to cheer you up.")
        print()
        joke = dadjoke()
        print(joke)
        print()
        end = tata()
        print(end,'!')
print()

# Milestone 3 : Setting up a global list of lists.

Master_list = Movie_list + Music_list + Books_list + Cusine_list + Workout_list

# Milestone 4 : Creating the various functions.

def musicbasedsuggestion(): # present a movie genre but give a music list
    movie = random.choice(Movie_genre)   
    music = random.choice(Master_list)
    suggest = f" Might I suggest a {movie} movie, {music} is going to be an excellent watch!"
    return suggest


def cuisinebasedsuggestion(): #music genre with cuisine list
    music = random.choice(Music_genre)
    cuisine = random.choice(Master_list)
    suggest = f"Me thinks {music} is particularly delightful. Why not listen to {cuisine}."
    return suggest

def workoutbasedsuggestion(): #book genre workout list
    book = random.choice(Books_genre)
    exercise = random.choice(Master_list)
    suggest = f"I believe {book} books make for a fine read. How about giving {exercise} a read, if you haven't already."
    return suggest

def bookbasedsuggestion(): # food genre, book list
    food = random.choice(Cuisine_gnere)
    book = random.choice(Master_list)
    suggest = f"Did you know {food} cuisine is all the rage now a days! How about treating your tastebuds to some {book}."
    return suggest  

def moviebasedsuggestion(): #exercise genre, movie list
    workout = random.choice(Workout_genre)
    movie = random.choice(Master_list)
    suggest = f"Doctors say {workout} is excellent for weight management. Perhaps you should give {movie} a spin."
    return suggest  

# Milestone 6 : Creating jokes function from joke list.
 
def dadjoke():
    djoke = random.choice(Dad_Joke)
    return djoke 

def tata():
    bye = random.choice(Conclude)
    return bye



if __name__ == "__main__":
    main()

