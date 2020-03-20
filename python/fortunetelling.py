from random import randint as rand
import sys

def main(args):

    #Main program logic
    try:
        #Declare variables
        output_string = ""
        predicates = gather_words("predicates")
        adjectives = gather_words("adjectives")
        nouns = gather_words("nouns")

    
        for x in range(int(args[1])):
            output_string += build_response(predicates, adjectives, nouns)
            output_string += "#"
    except Exception as e:
        output_string = "Server Error: " + str(e)

    print(output_string)
        

def gather_words(partofspeech):

    #Declare variables
    words = []
    words2 = []

    #Open file and read everything
    with open("python/words/" + partofspeech + ".txt", "r") as f:
        words = f.readlines()

    #Strip the newline character
    for word in words:
        words2.append(word.strip("\n"))

    return words2
    
def build_response(predicates, adjectives, nouns):

    #Choose a random predicate, adjective, and noun
    predicate = predicates[rand(0, len(predicates) - 1)]
    adjectives = adjectives[rand(0, len(adjectives) - 1)]
    nouns = nouns[rand(0, len(nouns) - 1)]

    return "I predict: " + predicate + " " + adjectives + " " + nouns

main(sys.argv)     
