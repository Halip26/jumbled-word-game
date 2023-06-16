# mengimpor modul random
import random


# fungsi untuk memilih kata acak.
def choose():
    # list of word
    words = ['rainbow', 'computer', 'science', 'programming',
             'mathematics', 'player', 'condition', 'reverse',
             'water', 'board', 'geeks']

    # metode choice() memilih secara acak
    # kata apa pun dari daftar.
    pick = random.choice(words)

    return pick


# Function for shuffling the characters of the chosen word.
def jumble(word):

    # metode sample() mengacak huruf dari kata
    random_word = random.sample(word, len(word))

    # metode join() menghubungkan elemen dari iterator (mis. daftar) dengan karakter tertentu.
    jumbled = ''.join(random_word)
    return jumbled


# Fungsi untuk menampilkan skor akhir..
def thank(p1n, p2n, p1, p2):
    print(p1n, 'Your score is : ', p1)
    print(p2n, 'Your score is : ', p2)

    # memanggil fungsi check_win()
    check_win(p1n, p2n, p1, p2)

    print('Thanks for playing...')


# Fungsi untuk mendeklarasikan pemenang.
def check_win(player1, player2, p1score, p2score):
    if p1score > p2score:
        print("winner is : ", player1)
    elif p2score > p1score:
        print("winner is : ", player2)
    else:
        print("Draw..Well Played guys..")


# Fungsi untuk memainkan game.
def play():
    # masukkan nama pemain1 dan pemain2
    p1name = input("Player 1, Please enter your name : ")
    p2name = input("Player 2, Please enter your name : ")

    # variabel untuk menghitung skor.
    pp1 = 0
    pp2 = 0

    # variabel untuk menghitung giliran
    turn = 0

    # keep looping
    while True:

        # memanggil fungsi choose()
        picked_word = choose()

        # memanggil fungsi jumble()
        qn = jumble(picked_word)
        print("jumbled word is : ", qn)

        # memeriksa giliran ganjil atau genap
        if turn % 2 == 0:

            # jika nomor giliran genap
            # giliran pemain 1
            print(p1name, 'Your Turn.')

            ans = input("what is in your mind? ")

            # memeriksa apakah jawaban sama dengan picked_word atau tidak
            if ans == picked_word:

                # variabel pp1 ditambah 1
                pp1 += 1

                print('Your score is : ', pp1)
                turn += 1

            else:
                print("Better luck next time ..")

                # giliran pemain 2
                print(p2name, 'Your turn.')

                ans = input('what is in your mind? ')

                if ans == picked_word:
                    pp2 += 1
                    print("Your Score is :", pp2)

                else:
                    print("Better luck next time...correct word is :", picked_word)

                c = int(input("press 1 to continue and 0 to quit :"))

                # checking the c is equal to 0 or not
                # if c is equal to 0 then break out
                # of the while loop o/w keep looping.
                if c == 0:
                    # thank() function calling
                    thank(p1name, p2name, pp1, pp2)
                    break

        else:

            # jika nomor giliran ganjil
            # giliran pemain 2
            print(p2name, 'Your turn.')
            ans = input('what is in your mind? ')

            if ans == picked_word:
                pp2 += 1
                print("Your Score is : ", pp2)
                turn += 1

            else:
                print("Better luck next time.. :")
                print(p1name, 'Your turn.')
                ans = input('what is in your mind? ')

                if ans == picked_word:
                    pp1 += 1
                    print("Your Score is : ", pp1)

                else:
                    print("Better luck next time...correct word is : ", picked_word)

                    c = int(input("press 1 to continue and 0 to quit : "))

                    if c == 0:
                        # thank() function calling
                        thank(p1name, p2name, pp1, pp2)
                        break

            c = int(input("press 1 to continue and 0 to quit : "))
            if c == 0:
                # thank() function calling
                thank(p1name, p2name, pp1, pp2)
                break


# Driver code
if __name__ == '__main__':

    # play() function calling
    play()
