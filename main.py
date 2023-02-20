'''
CHATBOT TIW-TIW
FEB 20,2023
Group 4
- Aleacel Retamal Postor
- Lynzelle Urbano
- Margarette Roque
- Nella Punzal
- Agustin Carlos Teodoro
- John Kim Alcantara
'''
import re
import long_response as long

print('Ask Tiw-tiw by typing words (lower-case only)')

def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    # Calculates the percent of recognized words in a user message
    percentage = float(message_certainty) / float(len(recognized_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    #Response------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'sup', 'hey', 'heyo', 'hoy'], single_response=True)
    response('My name is Tiw-Tiw, what about you?', ['name', 'pangalan'], single_response=True)
    response('Yes! I\'m fluent in English.', ['english', 'understand'], required_words=['english'])
    response('I\'m doing fine, how about you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('A little. Are you from the Philippines?', ['tagalog', 'understand'], required_words=['tagalog'])
    response('Congrats! Keep up the good work.', ['passed', 'pass', 'pasado'], single_response=True)
    response('Better luck next time',['bagsak', 'failed', 'fail'], single_response=True)
    response('Ang hobby ko ay to talk with you YIEEEE', ['hobbies','hobby'], single_response=True)
    response('Mahal rin kita', ['mahal', 'kita'], required_words=['mahal'])
    response('I Love You Too', ['love'], required_words=['love'])

    #Long_Response----------------------------------------------------------------------
    response(long.R_INS, ['insecure', 'felt'], required_words=['insecure'])
    response(long.R_ADV, ['give', 'advice'], required_words=['advice'])
    response(long.R_HAP, ['happy', 'feel'], required_words=['happy'])
    response(long.R_BOR, ['bored', 'tinatamad'], single_response=True)
    response(long.R_SAD, ['sad', 'depress', 'lonely'], single_response=True)
    response(long.R_BYE, ['goodbye', 'bye', 'later', 'paalam'], single_response=True)
    response(long.R_EAT, ['what', 'you','eat', 'kinakain', 'kumain'], single_response=True)
    response(long.R_BRO, ['broken', 'broke up', 'hearted', 'naghiwalay', 'hiwalay'], single_response=True)

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

#Testing the response system
while True:
    print('Tiwtiw: ' + get_response(input('You: ')))
