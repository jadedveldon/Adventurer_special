import sys, time, os


def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char != '\n':
            time.sleep(0.08)
        else:
            time.sleep(0.8)

text = '''
Dear Saumya,
Your return has long been awaited, the curse that wiped my memories away stays locked on me.
The bond we had is helping me fight it but then again i keep reverting back.
We need to free ourselves out together.
If you wish, walk out now and hug me as i stand guard unknowlying.
The moment is here!
We both waited too long.
Lets mend our ways!
Lets grow together again!
Lets rekindle the fire that we lost in vain.
New day marks a new beginning, lets start over and bond again!
lets do this somi lets make the world believe in magic once again!!!
Give me a chance again so i can proclaim my feelings for you all over!
So here again i just go and say
Saumya Gupta the witch that mauls with her smile
Will you take this lowly guard to be yours again?
I Love You my Queen!
HAPPY BIRTHDAY TO YOU AGAIN!!
'''
typewriter(text)
