import random

with open('db.txt', 'r', encoding='utf-8') as f:
    mots = [line.strip() for line in f]

def generate_mdp(nb_words):
    mdp = ''

    choiced_words = [random.choice(mots) for mot in range(nb_words)]
    choiced_numbers = [str(random.randint(0, 9)) for num in range(2)]
    choiced_special_char = random.choice('!@#$%^&*()_+-=[]{}|;:,.<>?')

    if nb_words == 2:
        mdp = ''.join(str(choiced_words[0].capitalize()) + str(choiced_numbers[0]) + str(choiced_numbers[1]) + str(choiced_special_char) + str(choiced_words[1].capitalize()))
    elif nb_words == 3:
        mdp = ''.join(str(choiced_words[0].capitalize()) + str(choiced_words[1].capitalize()) + str(choiced_numbers[0]) + str(choiced_numbers[1]) + str(choiced_special_char) + str(choiced_words[2].capitalize()))
    elif nb_words == 4:
        mdp = ''.join(str(choiced_words[0].capitalize()) + str(choiced_words[1].capitalize()) + str(choiced_numbers[0]) + str(choiced_numbers[1]) + str(choiced_special_char) + str(choiced_words[2].capitalize()) + str(choiced_words[3].capitalize()))

    return mdp

if __name__ == '__main__':
    print("\n", generate_mdp(3), "\n")
    print("Password generated successfully!")