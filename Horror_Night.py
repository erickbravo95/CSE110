print("*************************************")
print("************Horror Night*************")
print("****************V0.2*****************")
print("Welcome to the Horror Night open Beta")
tuki = input ("Please enter your name to continue: ")
tuki = True

if tuki :
    print("There I was, running in the middel of the forest as fast as I could, I knew that the moment I stop")
    print("my life will end, but then I saw a scary old house, so a decided to.. ENTER the house or KEEP running.")
    case_open = input("What do you want to do?")
    if case_open.lower() == "enter":
        print("As soon as I reached the front door, I tried to open it, but the handle was rusty and damaged so")
        print("I slam the door with my shoulder until it opens, It was so dark that I couldn't see anything but")
        print("a BASEMENT and at the end of the hallway the KITCHEN..")
        case1 = input("Where do you want to go?")
        if case1.lower() == "basement":
            print("That was a Horrendous mistake... It was a dead-end... I.. met my doom...GAME OVER...")
        else:
            print("I had to hurry... I could even feel its presence near form me, as I walked to the backdoor I notice")
            print("something shiny over the sink.. it was a flashlight! so I took it and I went outside the house, it was so dark")
            print("that I couldn't see my hand in front of my face so I had two options TURN ON the flashlight or NOT")
            case1_1 = input("turn on the flashlight?")
            if case1_1.lower() == "turn on":
                print("The flashlight worked!! the path was clear, I ran as fast as the wind, I could see the light of the town")
                print("I was so close! but then.. I realized that if I made it to the town.. they will be in danger too.. I had to choose *")
                print("go the POLICE station or go to my HOME...")
                case1_1_1 = input("What do you want to do?")
                if case1_1_1.lower() == "police":
                    print("at last.... it's over.. THANKS FOR PLAYING!!!")
                else:
                    print("at last.... it's over.. THANKS FOR PLAYING!!!")
                
            else:
                print("I didn't turn it on.. I hid behind some bushes but.. It saw it coming.. It was already there...GAME OVER")

    else:
        print("I kept running, but out of nowhere a huge tree started to fall, It was like something knocked it down and it falled")
        print("it fell above a giant boulder, I had to do something quickly or it will cache me, do I JUMP or SLIDE under the tree?")
        case2 = input("What do you want to do?")
        if case2 == "jump":
            print("I jumped as hight as I could, but it wasn't enought.. I felt down the floor, whene I opened my eyes.. I saw it.. GAME OVER..")
        else:
            print("That was so closed.. I barely made it. but I couldn't see anything in front of me, then I remembered I had")
            print("matches in my back pocket, those will help me to see the trail.. but, do I LIGHT the matches or NOT? ")
            case2_1 = input("What do you want to do?")
            if case2_1.lower() == "YES":
                print("The flashlight worked!! the path was clear, I ran as fast as the wind, I could see the light of the town")
                print("I was so close! but then.. I realized that if I made it to the town.. they will be in danger too.. I had to choose *")
                print("go the POLICE station or go to my HOME...")
                case2_1_1 = input("What do you want to do?")
                if case2_1_1.lower() == "POLICE":
                    print("at last.... it's over.. THANKS FOR PLAYING!!!")
                else:
                    print("at last.... it's over.. THANKS FOR PLAYING!!!")
            else:
                print("I didn't turn it on.. I hid behind some bushes but.. It saw it coming.. It was already there...GAME OVER")

            



        

