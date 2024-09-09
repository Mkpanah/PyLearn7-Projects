import pytube
import datetime
from idm import IDMan
from Represent import *
from DataBase import *
downloader = IDMan()


class Main:
    @staticmethod
    def add():
        print("Enter the DataBase you wish to append information onto from the following options")
        print("1 - Film")
        print("2 - Series")
        print("3 - Documentary")
        print("4 - Clip")
        selection = int(input("Enter Your Desired Option: "))
        if selection == 1:
            title = input("Title : ")
            film_df[f"A{film_df.max_row + 1}"] = title

            production_year = input("Production Year : ")
            film_df[f"B{film_df.max_row}"] = production_year

            length = input("Enter the duration of the Movie in HH:MM:SS Format: ")
            lst_int = [int(x) for x in length.split(":")]
            duration = datetime.time(hour=lst_int[0], minute=lst_int[1], second=lst_int[2])
            film_df[f"C{film_df.max_row}"] = duration

            url = input("URL : ")
            film_df[f"D{film_df.max_row}"] = url

            imdb_score = input("IMDB Score : ")
            film_df[f"E{film_df.max_row}"] = imdb_score

            director = input("Director : ")
            film_df[f"F{film_df.max_row}"] = director

            casts = input("Casts : ")
            film_df[f"G{film_df.max_row}"] = casts

            genre = input("Genre : ")
            film_df[f"H{film_df.max_row}"] = genre

            df.save("Media.xlsx")

        elif selection == 2:
            title = input("Title : ")
            series_df[f"A{series_df.max_row + 1}"] = title

            production_year = input("Production Year : ")
            series_df[f"B{series_df.max_row}"] = production_year

            length = input("Enter the duration of the Movie in HH:MM:SS Format: ")
            lst_int = [int(x) for x in length.split(":")]
            duration = datetime.time(hour=lst_int[0], minute=lst_int[1], second=lst_int[2])
            series_df[f"C{series_df.max_row}"] = duration

            url = input("URL : ")
            series_df[f"D{series_df.max_row}"] = url

            imdb_score = input("IMDB Score : ")
            series_df[f"E{series_df.max_row}"] = imdb_score

            n_seasons = int(input("Number of the Seasons: "))
            series_df[f"F{series_df.max_row}"] = n_seasons

            n_episodes = int(input("Total number of the Episodes: "))
            series_df[f"G{series_df.max_row}"] = n_episodes

            director = input("Director : ")
            series_df[f"H{series_df.max_row}"] = director

            casts = input("Casts : ")
            series_df[f"I{series_df.max_row}"] = casts

            genre = input("Genre : ")
            series_df[f"J{series_df.max_row}"] = genre

            df.save("Media.xlsx")

        elif selection == 3:
            title = input("Title : ")
            doc_df[f"A{doc_df.max_row + 1}"] = title

            production_year = input("Production Year : ")
            doc_df[f"B{doc_df.max_row}"] = production_year

            length = input("Enter the duration of the Movie in HH:MM:SS Format: ")
            lst_int = [int(x) for x in length.split(":")]
            duration = datetime.time(hour=lst_int[0], minute=lst_int[1], second=lst_int[2])
            doc_df[f"C{doc_df.max_row}"] = duration

            url = input("URL : ")
            doc_df[f"D{doc_df.max_row}"] = url

            imdb_score = input("IMDB Score : ")
            doc_df[f"E{doc_df.max_row}"] = imdb_score

            director = input("Director : ")
            doc_df[f"F{doc_df.max_row}"] = director

            casts = input("Casts : ")
            doc_df[f"G{doc_df.max_row}"] = casts

            subject = input("Subject : ")
            doc_df[f"H{doc_df.max_row}"] = subject

            df.save("Media.xlsx")

        elif selection == 4:
            title = input("Title : ")
            clip_df[f"A{clip_df.max_row + 1}"] = title

            production_year = input("Production Year : ")
            clip_df[f"B{clip_df.max_row}"] = production_year

            length = input("Enter the duration of the Movie in HH:MM:SS Format: ")
            lst_int = [int(x) for x in length.split(":")]
            duration = datetime.time(hour=lst_int[0], minute=lst_int[1], second=lst_int[2])
            clip_df[f"C{clip_df.max_row}"] = duration

            url = input("URL : ")
            clip_df[f"D{clip_df.max_row}"] = url

            views = int(input("Views : "))
            clip_df[f"E{clip_df.max_row}"] = views

            uploader = input("Uploader : ")
            clip_df[f"F{clip_df.max_row}"] = uploader

            df.save("Media.xlsx")

        else:
            print("Enter the correct Number!! ")

    @staticmethod
    def remove():
        print("Enter the DataBase you wish to REMOVE information from the following options")
        print("1 - Film")
        print("2 - Series")
        print("3 - Documentary")
        print("4 - Clip")
        selection = int(input("Enter Your Desired Option: "))
        if selection == 1:
            value_to_delete = input("Enter the Title of the Movie to REMOVE: ")
            rows_to_delete = []
            # Iterate through the rows and check the value in the specified column
            for row in range(1, film_df.max_row + 1):
                cell_value = film_df[f'A{row}'].value
                if cell_value == value_to_delete:
                    rows_to_delete.append(row)
            # Delete the rows from bottom to top
            for row in sorted(rows_to_delete, reverse=True):
                film_df.delete_rows(row)

            # Save the updated workbook
            df.save('Media.xlsx')

        elif selection == 2:
            value_to_delete = input("Enter the Title of the Series to REMOVE: ")
            rows_to_delete = []
            # Iterate through the rows and check the value in the specified column
            for row in range(1, series_df.max_row + 1):
                cell_value = series_df[f'A{row}'].value
                if cell_value == value_to_delete:
                    rows_to_delete.append(row)
            # Delete the rows from bottom to top
            for row in sorted(rows_to_delete, reverse=True):
                series_df.delete_rows(row)

            # Save the updated workbook
            df.save('Media.xlsx')

        elif selection == 3:
            value_to_delete = input("Enter the Title of the Document to REMOVE:")
            rows_to_delete = []
            # Iterate through the rows and check the value in the specified column
            for row in range(1, doc_df.max_row + 1):
                cell_value = doc_df[f'A{row}'].value
                if cell_value == value_to_delete:
                    rows_to_delete.append(row)
            # Delete the rows from bottom to top
            for row in sorted(rows_to_delete, reverse=True):
                doc_df.delete_rows(row)

            # Save the updated workbook
            df.save('Media.xlsx')

        elif selection == 4:
            value_to_delete = input("Enter the Title of the Clip to REMOVE: ")
            rows_to_delete = []
            # Iterate through the rows and check the value in the specified column
            for row in range(1, clip_df.max_row + 1):
                cell_value = clip_df[f'A{row}'].value
                if cell_value == value_to_delete:
                    rows_to_delete.append(row)
            # Delete the rows from bottom to top
            for row in sorted(rows_to_delete, reverse=True):
                clip_df.delete_rows(row)

            # Save the updated workbook
            df.save('Media.xlsx')

        else:
            print("Enter the Correct VALUE!")

    @staticmethod
    def edit():
        print("Enter the DataBase you wish to EDIT Information!")
        print("1 - Movie")
        print("2 - Series")
        print("3 - Documentary")
        print("4 - Clip")
        option = int(input("Enter Your Desired Option: "))
        if option == 1:
            column_values = []
            for row in range(2, film_df.max_row + 1):
                cell_value = film_df[f'A{row}'].value
                column_values.append(cell_value)
            name = input("Enter the Title of the movie you wish to Edit information! ")
            if name in column_values:
                row_number = column_values.index(name) + 2
                keys = [cell.value for cell in film_df[1]]
                print("Enter the Information you want to Edit from the Following.")
                for i, key in enumerate(keys, start=1):
                    print(f"{i} - {key}")
                option = int(input("Enter the Desire Value: "))
                if option == 1:
                    film_df[f"A{row_number}"] = input("Enter the new Title of the Movie: ")
                elif option == 2:
                    film_df[f"B{row_number}"] = input("Enter the new Production Year of the Movie: ")
                elif option == 3:
                    length = input("Enter the New duration of the Movie in HH:MM:SS Format: ")
                    lst_int = [int(x) for x in length.split(":")]
                    film_df[f"C{row_number}"] = datetime.time(hour=lst_int[0], minute=lst_int[1], second=lst_int[2])
                elif option == 4:
                    film_df[f"D{row_number}"] = input("Enter the new URL of the Movie: ")
                elif option == 5:
                    film_df[f"E{row_number}"] = input("Enter the new IMDB Score of the Movie: ")
                elif option == 6:
                    film_df[f"F{row_number}"] = input("Enter the new Director of the Movie: ")
                elif option == 7:
                    film_df[f"G{row_number}"] = input("Enter the new Casts of the Movie: ")
                elif option == 8:
                    film_df[f"H{row_number}"] = input("Enter the new Genre of the Movie: ")
                else:
                    print("Enter correct value")
            else:
                print("Not Existed in the DataBase! ")

            df.save("Media.xlsx")

        elif option == 2:
            column_values = []
            for row in range(2, series_df.max_row + 1):
                cell_value = series_df[f'A{row}'].value
                column_values.append(cell_value)
            name = input("Enter the Title of the Series you wish to Edit information! ")
            if name in column_values:
                row_number = column_values.index(name) + 2
                keys = [cell.value for cell in series_df[1]]
                print("Enter the Information you want to Edit from the Following.")
                for i, key in enumerate(keys, start=1):
                    print(f"{i} - {key}")
                option = int(input("Enter the Desire Value: "))
                if option == 1:
                    series_df[f"A{row_number}"] = input("Enter the new Title of the Series: ")
                elif option == 2:
                    series_df[f"B{row_number}"] = input("Enter the new Production Year of the Series: ")
                elif option == 3:
                    length = input("Enter the New duration of the Series in HH:MM:SS Format: ")
                    lst_int = [int(x) for x in length.split(":")]
                    series_df[f"C{row_number}"] = datetime.time(hour=lst_int[0], minute=lst_int[1], second=lst_int[2])
                elif option == 4:
                    series_df[f"D{row_number}"] = input("Enter the new URL of the Series: ")
                elif option == 5:
                    series_df[f"E{row_number}"] = input("Enter the new IMDB Score of the Series: ")
                elif option == 6:
                    series_df[f"F{row_number}"] = input("Enter the new Number of the Seasons of the Series: ")
                elif option == 7:
                    series_df[f"G{row_number}"] = input("Enter the new Number of the Episodes of the Series: ")
                elif option == 8:
                    series_df[f"H{row_number}"] = input("Enter the new Director(s) of the Series: ")
                elif option == 9:
                    series_df[f"I{row_number}"] = input("Enter the new Casts of the Series: ")
                elif option == 10:
                    series_df[f"J{row_number}"] = input("Enter the new Genre of the Series: ")
                else:
                    print("Enter correct value")
            else:
                print("Not Existed in the DataBase! ")

            df.save("Media.xlsx")

        elif option == 3:
            column_values = []
            for row in range(2, doc_df.max_row + 1):
                cell_value = doc_df[f'A{row}'].value
                column_values.append(cell_value)
            name = input("Enter the Title of the Document you wish to Edit information! ")
            if name in column_values:
                row_number = column_values.index(name) + 2
                keys = [cell.value for cell in doc_df[1]]
                print("Enter the Information you want to Edit from the Following.")
                for i, key in enumerate(keys, start=1):
                    print(f"{i} - {key}")
                option = int(input("Enter the Desired Value: "))
                if option == 1:
                    doc_df[f"A{row_number}"] = input("Enter the new Title of the Document: ")
                elif option == 2:
                    doc_df[f"B{row_number}"] = input("Enter the new Production Year of the Document: ")
                elif option == 3:
                    length = input("Enter the New duration of the Document in HH:MM:SS Format: ")
                    lst_int = [int(x) for x in length.split(":")]
                    doc_df[f"C{row_number}"] = datetime.time(hour=lst_int[0], minute=lst_int[1], second=lst_int[2])
                elif option == 4:
                    doc_df[f"D{row_number}"] = input("Enter the new URL of the Document: ")
                elif option == 5:
                    doc_df[f"E{row_number}"] = input("Enter the new IMDB Score of the Document: ")
                elif option == 6:
                    doc_df[f"F{row_number}"] = input("Enter the new Director of the Document: ")
                elif option == 7:
                    doc_df[f"G{row_number}"] = input("Enter the new Casts of the Document: ")
                elif option == 8:
                    doc_df[f"H{row_number}"] = input("Enter the new Subject of the Document: ")
                else:
                    print("Enter correct value")
            else:
                print("Not Existed in the DataBase! ")

            df.save("Media.xlsx")

        elif option == 4:
            column_values = []
            for row in range(2, clip_df.max_row + 1):
                cell_value = clip_df[f'A{row}'].value
                column_values.append(cell_value)
            name = input("Enter the Title of the movie you wish to Edit information! ")
            if name in column_values:
                row_number = column_values.index(name) + 2
                keys = [cell.value for cell in clip_df[1]]
                print("Enter the Information you want to Edit from the Following.")
                for i, key in enumerate(keys, start=1):
                    print(f"{i} - {key}")
                option = int(input("Enter the Desire Value: "))
                if option == 1:
                    clip_df[f"A{row_number}"] = input("Enter the new Title of the Clip: ")
                elif option == 2:
                    clip_df[f"B{row_number}"] = input("Enter the new Production Year of the Clip: ")
                elif option == 3:
                    length = input("Enter the New duration of the Clip in HH:MM:SS Format: ")
                    lst_int = [int(x) for x in length.split(":")]
                    clip_df[f"C{row_number}"] = datetime.time(hour=lst_int[0], minute=lst_int[1], second=lst_int[2])
                elif option == 4:
                    clip_df[f"D{row_number}"] = input("Enter the new URL of the Clip: ")
                elif option == 5:
                    clip_df[f"E{row_number}"] = input("Enter the Updated Views of the Clip: ")
                elif option == 6:
                    series_df[f"F{row_number}"] = input("Enter the new Uploader of the Clip: ")
                else:
                    print("Enter correct value")
            else:
                print("Not Existed in the DataBase! ")

            df.save("Media.xlsx")

    @staticmethod
    def search():
        db = Database
        film_list, series_list, doc_list, clip_list = db.read_from_database()
        print("Enter the DataBase you wish to SEARCH information from the following options.")
        print("1 - Film")
        print("2 - Series")
        print("3 - Documentary")
        print("4 - Clip")
        selection = int(input("Enter Your Desired Option: "))
        if selection == 1:
            name = input("Enter the Title of the Movie you want to see the other information: ")
            if name in film_list["title"]:
                i = film_list["title"].index(name)
                for key in film_list.keys():
                    print(f"{key}: {film_list[f'{key}'][i]}")
            else:
                print("Not Existed.")

        elif selection == 2:
            name = input("Enter the Title of the Series you want to see the other information: ")
            if name in series_list["title"]:
                i = series_list["title"].index(name)
                for key in series_list.keys():
                    print(f"{key}: {series_list[f'{key}'][i]}")
            else:
                print("Not Existed.")

        elif selection == 3:
            name = input("Enter the Title of the Series you want to see the other information: ")
            if name in doc_list["title"]:
                i = doc_list["title"].index(name)
                for key in doc_list.keys():
                    print(f"{key}: {doc_list[f'{key}'][i]}")
            else:
                print("Not Existed.")

        elif selection == 4:
            name = input("Enter the Title of the Series you want to see the other information: ")
            if name in clip_list["title"]:
                i = clip_list["title"].index(name)
                for key in clip_list.keys():
                    print(f"{key}: {clip_list[f'{key}'][i]}")
            else:
                print("Not Existed.")

        else:
            print("Enter the correct VALUE!")

    @staticmethod
    def time_search():
        print("Enter the DataBase you wish to SEARCH Based on TIME from the following.")
        print("1 - Film")
        print("2 - Series")
        print("3 - Documentary")
        print("4 - Clip")
        selection = int(input("Enter Your Desired Option: "))
        a = int(input("Enter the first step in Minutes : "))
        b = int(input("Enter the Second Step in Minutes : "))
        durations = []
        durations_in_minutes = []
        titles = []

        if selection == 1:
            for row in film_df.iter_rows(min_row=2):
                duration = row[2].value
                title = row[0].value
                durations.append(duration)
                titles.append(title)
                durations_in_minutes.append(duration.hour * 60 + (duration.minute * 1) + (duration.second / 60))

            for i in range(len(durations)):
                if abs(a - b) > durations_in_minutes[i]:
                    print(titles[i])

        elif selection == 2:
            for row in series_df.iter_rows(min_row=2):
                duration = row[2].value
                title = row[0].value
                durations.append(duration)
                titles.append(title)
                durations_in_minutes.append(duration.hour * 60 + (duration.minute * 1) + (duration.second / 60))

            for i in range(len(durations)):
                if abs(a - b) > durations_in_minutes[i]:
                    print(titles[i])

        elif selection == 3:
            for row in doc_df.iter_rows(min_row=2):
                duration = row[2].value
                title = row[0].value
                durations.append(duration)
                titles.append(title)
                durations_in_minutes.append(duration.hour * 60 + (duration.minute * 1) + (duration.second / 60))

            for i in range(len(durations)):
                if abs(a - b) > durations_in_minutes[i]:
                    print(titles[i])

        elif selection == 4:
            for row in clip_df.iter_rows(min_row=2):
                duration = row[2].value
                title = row[0].value
                durations.append(duration)
                titles.append(title)
                durations_in_minutes.append(duration.hour * 60 + (duration.minute * 1) + (duration.second / 60))

            for i in range(len(durations)):
                if abs(a - b) > durations_in_minutes[i]:
                    print(titles[i])

        else:
            print("Enter Correct VALUE!")

    @staticmethod
    def casts():
        print("Enter the DataBase you wish to APPEND all the Casts onto!")
        print("1 - Movie")
        print("2 - Series")
        print("3 - Documentary")
        option = int(input("Enter Your Desired Option: "))
        if option == 1:
            # Specify the column to extract values from
            column_letter = 'G'  # For example, column 'A'
            column_values = []

            # Iterate through each row in the specified column and append the values to the list
            for row in range(2, film_df.max_row + 1):
                cell_value = film_df[f'{column_letter}{row}'].value
                column_values.append(cell_value)

            split_values = [i.split(', ') for i in column_values]
            unified_values = [j for sub in split_values for j in sub]
            actors = list(set(unified_values))
            print(f"Actors Presented in the Film DataBase are: {actors}.")

        elif option == 2:
            # Specify the column to extract values from
            column_letter = 'I'  # For example, column 'A'
            column_values = []

            # Iterate through each row in the specified column and append the values to the list
            for row in range(2, series_df.max_row + 1):
                cell_value = series_df[f'{column_letter}{row}'].value
                column_values.append(cell_value)

            split_values = [i.split(', ') for i in column_values]
            unified_values = [j for sub in split_values for j in sub]
            actors = list(set(unified_values))
            print(f"Actors Presented in the Series DataBase are: {actors}.")

        elif option == 3:
            # Specify the column to extract values from
            column_letter = 'G'  # For example, column 'A'
            column_values = []

            # Iterate through each row in the specified column and append the values to the list
            for row in range(2, doc_df.max_row + 1):
                cell_value = doc_df[f'{column_letter}{row}'].value
                column_values.append(cell_value)

            split_values = [i.split(', ') for i in column_values]
            unified_values = [j for sub in split_values for j in sub]
            actors = list(set(unified_values))
            print(f"Actors Presented in the Documentary DataBase are: {actors}.")

        else:
            print("Enter Correct VALUE!!!")

    @staticmethod
    def download():
        print("Make sure you have IDM application installed on your PC!")
        print("1 - Download Movie")
        print("2 - Download Series")
        print("3 - Download Documentary")
        print("4 - Download Clip")
        option = int(input("Enter Your Desired Option: "))
        db = Database
        film_list, series_list, doc_list, clip_list = db.read_from_database()
        if option == 1:
            print(film_list["title"])
            movie_title = input("Enter the Title of the Movie you want to Download: ")
            if movie_title not in film_list["title"]:
                print("Not Available in the DataBase Yet!")
            else:
                downloader.download(film_list["url"][film_list["title"].index(movie_title)], r"c:\DOWNLOADS",
                                    output=None, referrer=None, cookie=None, postData=None, user=None,
                                    password=None, confirm=False, lflag=None, clip=False)
        elif option == 2:
            print(series_list["title"])
            series_title = input("Enter the Title of the Series you want to Download: ")
            if series_title not in series_list["title"]:
                print("Not Available in the DataBase Yet!")
            else:
                downloader.download(series_list["url"][series_list["title"].index(series_title)], r"c:\DOWNLOADS",
                                    output=None, referrer=None, cookie=None, postData=None, user=None,
                                    password=None, confirm=False, lflag=None, clip=False)

        elif option == 3:
            print(doc_list["title"])
            doc_title = input("Enter the Title of the Series you want to Download: ")
            if doc_title not in doc_list["title"]:
                print("Not Available in the DataBase Yet!")
            else:
                downloader.download(doc_list["url"][doc_list["title"].index(doc_title)], r"c:\DOWNLOADS",
                                    output=None, referrer=None, cookie=None, postData=None, user=None,
                                    password=None, confirm=False, lflag=None, clip=False)
        elif option == 4:
            print(clip_list["title"])
            clip_title = input("Enter the Title of the Series you want to Download: ")
            if clip_title not in clip_list["title"]:
                print("Not Available in the DataBase Yet!")
            else:
                link = clip_list["url"][clip_list["title"].index(clip_title)]
                print(link)
                first_stream = pytube.YouTube(link).streams.first()
                first_stream.download(output_path='./', filename=f"{clip_title}.mp4")

        else:
            print("Enter Valid Choice among the Options!!")


print("Welcome to Media App")
print("Loading...")
Database.read_from_database()
print("Data loaded...")

while True:
    Represent.show_menu()
    choice = int(input("Please enter your choice: "))
    if choice == 1:
        Main.add()
    elif choice == 2:
        Main.remove()
    elif choice == 3:
        Main.edit()
    elif choice == 4:
        Main.search()
    elif choice == 5:
        Main.time_search()
    elif choice == 6:
        Main.casts()
    elif choice == 7:
        Main.download()
    elif choice == 8:
        Database.write_to_database()
        exit(0)
    else:
        print("Incorrect input!")
