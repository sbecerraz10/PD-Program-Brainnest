'''
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
'''

# Output
'''
You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
'''




def find_letter(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def replace_positions(pos_list, input_letter ,word_secret):
    word = word_secret
    for i in range(len(pos_list)):
        word = replace_str_index(word, pos_list[i], input_letter)
    return word
        
def replace_str_index(text,index,replacement=''):
    return f'{text[:index]}{replacement}{text[index+1:]}'


def print_message(tries_left, used_letters, word_secret, word):
    message = f"You have {tries_left} tries left. \n Used letters: {used_letters} \n Word:{word_secret} \n Guess a letter: "
    input_letter = input(message)
    if input_letter in word:
        pos_list = find_letter(word, input_letter)
        word_secret = replace_positions(pos_list, input_letter, word_secret)
    else:
        tries_left -= 1
    
    used_letters += f" {input_letter}"

    return tries_left, used_letters, word_secret, word
            
        




def main():
    global word 
    word = "java"
    tries_left = 6
    used_letters = ""
    word_secret = "____"
    game_over = False
    winner = False
    while(winner == False and game_over == False):
        tries_left, used_letters, word_secret, word = print_message(tries_left, used_letters, word_secret, word)
        if word.casefold() == word_secret.casefold():
            winner = True
            print(f"Congrats! You are a true champion!!🏆 \n You guessed the word {word} !")
        elif tries_left == 0:
            game_over = True 
            print("Game over try harder next time")

if __name__ == "__main__":
    main()