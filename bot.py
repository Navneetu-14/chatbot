from nltk.chat.util import Chat,reflections
pairs = [
    ["(Hello|hi|hey)",["What is your name?"]],
    ["(my name is (.*))",["hi %1. How are you doing today"]],
    ["(good|How are you)",["I'm  very well,thank you"]],
    ["(who are you)",["I am Robot"]],
    ["(i need your help|can you help me)",["How can i help you"]],
    ["(what is java)",["java is object oriented programming language"]],
    ["(what is PI value)",["PI value is 3.14"]],
    ["(Who create you|who is your creator)",["I was created by Navneetu but we all are created by God"]],
    ["(Are you Robot)",["Yes i am a Robot"]],
    [r"quit",["Bye Takecare.see you soon","it was nice talking to you .See you soon"]],
    [
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?",]
        
    ],
     [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot weather  in %1","hot" ,"Too cold man here in %1","Never even heard about %1"]],
    ]

def firstChatBot():
    print("Hi, i am your first chatbot build over nltk module")
    chatbot = Chat(pairs,reflections)
    chatbot.converse()

if __name__ == '__main__':
    firstChatBot()
