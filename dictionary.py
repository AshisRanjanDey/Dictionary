import json
from difflib import get_close_matches as gcm

def get_meaning(word):

    if word in data:                                            #word is in dataionary
        return data[word]

    #elif word.title() in data:
    #    return data[word.title()]

    #elif word.upper() in data:
    #    return data[word.upper()]

    elif len(gcm(word,data.keys(),n=11,cutoff=0.6))>0:
        mtch_list=gcm(word,data.keys(),n=11,cutoff=0.6)            #other similar words in dictionary
        print('Do you mean %s?'%mtch_list[0])
        user_response=str(input('y means yes | n means no : '))

        if user_response.lower()=='y':
            return data[mtch_list[0]]

        elif user_response.lower()=='n' and len(mtch_list)>1:#list contains more than one match or similar word
            print('Other matches :')
            for i in range(1,len(mtch_list)):
                print('%d. %s'%(i,mtch_list[i]))
            user_response2=str(input('Enter number to see meaning |or| Enter n if none matches : '))
            if user_response2.isdigit():                     #Integer responce <1,2,34,90>
                if int(user_response2)>=1 and int(user_response2)<len(mtch_list):
                    return data[mtch_list[int(user_response2)]]
                else:
                    return 'Sorry! Invalid entry'
            elif user_response2=='n':                        #no match acc. to user
                return 'Sorry! Word not found'
            else:
                return 'Sorry! Invalid entry'


        elif user_response.lower()=='n' and len(mtch_list)==1:#list contains only one match
            return 'Sorry! Word not found'

        else:
            return 'Sorry! Invalid entry'

    else:#no word is similar
        return 'Sorry! Word not found'


if __name__=='__main__':
    data=json.load(open("dictionary_webster.json"))
    s=str(input("Enter word : ").upper())
    output=get_meaning(s)
    if type(output)==list:
        for item in output: print(item)
    else:
        print(output)
