print('Enter q at any time to quit');
vowels = "a,e,i,o,u";
playGame = True;

while playGame:
    englishString = input("Please enter an english sentence: ");
    playGame = englishString != 'q';
    if(playGame):
        words = englishString.split();

        for word in words:
            firstLetter = word[0];
            if vowels.__contains__(firstLetter.lower()):
                firstLetter = 'w';
            else:
                word = word[1:];
                if not vowels.__contains__(word[0].lower()):
                    firstLetter += word[0];
                    word = word[1:];
            pigLatinWord = word + firstLetter + "ay";
            print(pigLatinWord, end=" ");

        print('\n');