# print("C:/Users/Пользователь/PycharmProjects/CR\\ids.csv")
import plotly.graph_objs as go
import json
import os


while True:
    print("1 - The popular words")
    print("2 - Exit")
    choice = input("Your choice: ")
    if choice == '1':
        print("Example path:  C:/Users/Пользователь/PycharmProjects/CR")
        user_pass = input("Your path: ")
        user_type = input("Your file type(.txt, .csv, .json): ")
        files_name = os.listdir(path=user_pass)
        popular_words = {}
        for file_name in files_name:
            if file_name[-len(user_type):len(file_name)] == user_type:
                file = open(f"{user_pass}/{file_name}", "rt", encoding='utf-8')
                words = json.load(file).split()
                for word in words:
                    if word in popular_words:
                        popular_words[word] += 1
                    else:
                        popular_words[word] = 1
        print("1 - Show in text report")
        print("2 - Show as diagram")
        choice = input("Your choice: ")
        popular_words_l = popular_words.copy()
        leaders = {}
        for i in range(1, 4):
            leader = ["", 0]
            for word in popular_words_l:
                if popular_words_l[word] > leader[1]:
                    leader[0] = word
                    leader[1] = popular_words_l[word]
            popular_words_l.pop(leader[0])
            leaders[i] = {}
            leaders[i]["word"] = leader[0]
            leaders[i]["value"] = leader[1]
        if choice == '1':
            for number in leaders:
                print("-" * 30)
                print(number)
                for object_ in leaders[number]:
                    print(f"    {object_}: {leaders[number][object_]}")
                print("-"*30)
        elif choice == '2':
            words_leaders = []
            value_leaders = []
            for i in leaders:
                words_leaders.append(leaders[i]["word"])
                value_leaders.append(leaders[i]["value"])
            diagram = go.Bar(x=words_leaders, y=value_leaders)
            figure = go.Figure(data=[diagram])
            figure.write_html("words_leaders.html", auto_open=True)
    elif choice == '2':
        break
    else:
        continue
