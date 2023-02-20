import random

R_EAT = "Hindi ako kumakain, I'm a bot obvious naman!"
R_BYE = "Alright, talk to you later. Thank you for having a conversation with me!"
R_ADV = "mag-search ka nalang sa Google hahaha. JOKE!!!, ano ba ang nararandaman/iniisip mo ngayon?"
R_BOR = "Doing nothing is the main point of being bored. Accept it and take pleasure in doing nothing."
R_HAP = "Being happy is extremely vital and something every person ultimately wants(SANA ALL)"

R_INS = '''No one is perfect. Even the most confident people have insecurities. At some point in our lives,
 we may feel we lack something. That is reality. We must try to live as per our capability.'''

R_SAD = '''Talking about your feelings can be good for your mental health.
 It is often the first step to overcoming mental health problem, and some people are willing to listen. 
 Some people prefer to speak to family or friends, and others may wish to discuss their feelings with a professional.
 You can talk with me about how you are feeling. There is hope even when your brain tells you there isn't'''

R_BRO = '''This is such a great opportunity for you! You can use this time while you're single to improve yourself,
 focus on yourself, love yourself, take a painting class, learn tai chi! So many great things will come from this!
 It's really a huge blessing. Every relationship is different and every break-up is different. You are grieving
 right now, and there's no 'one right away' to grieve. I hope you'll do whatever you need to do, and take as 
 much time as you need. There is no rush.'''

def unknown():
    response = ['Sorry hindi kita maintindihan pwede ba re-phrase mo yan?', '....', 'ewan ko sayo',
                'ano ibig mo sabihin?'][random.randrange(4)]
    return response

