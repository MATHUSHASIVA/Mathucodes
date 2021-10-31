while True:
    word = input("Enter Word: ") #input
    Word = word.lower()
    n=len(Word)
    x=0
                                           ###  nooncivic

    if Word == "bye": 
        print("Bye!")
        break

    else:
        for i in Word:
            p=Word.find(i,x+1)
            P=p
            a=Word.index(i,x)
            A=a
            substring_len = p-a+1
            x=x+1
            if p > 0:
                while substring_len > 1:
                    if Word[a+1] == Word[p-1]:
                        a=a+1
                        p=p-1
                        substring_len = p-a+1
                        
                    else :
                        break
                else:
                    substring = Word[A:P+1]
                    print("Longest Palindrome:",substring)
                    break

            else:
                continue
        else:
            print("There are no palindromes")

           
               
                
            
                
                
            
                
                
                    
