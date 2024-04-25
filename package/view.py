from tkinter import *

root= Tk()
root.title("MapBook")
root.geometry("800x500")

#ramki do porządkowania struktury
ramka_lista_obiektow= Frame(root)
ramka_formularz= Frame(root)
ramka_szczegoly_obiektow= Frame(root)

ramka_lista_obiektow.grid(row=0, column=0, padx=50)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektow.grid(row=1, column=0, columnspan=2)


#lista obiektow
label_lista_obiektow = Label(ramka_lista_obiektow, text="Lista obiektów: ")
listbox_lista_obiektow = Listbox(ramka_lista_obiektow, width=50)
button_pokaz_szczegoly= Button(ramka_lista_obiektow, text="Pokaż szczegóły")
button_usun_obiekt= Button(ramka_lista_obiektow, text="Usuń obiekt")
button_edytuj_obiekt= Button(ramka_lista_obiektow, text="Edytuj obiekt")



label_lista_obiektow.grid(row=0, column=0,  columnspan=3)
listbox_lista_obiektow.grid(row=1,column=0, columnspan=3)
button_pokaz_szczegoly.grid(row=2, column=0)
button_usun_obiekt.grid(row=2, column=1)
button_edytuj_obiekt.grid(row=2, column=2)

#formularz
label_formularz = Label(ramka_formularz, text= "Formularz")
label_imie = Label(ramka_formularz, text= "Imię: ")
label_nazwisko = Label(ramka_formularz, text= "Nazwisko: ")
label_posty = Label(ramka_formularz, text= "Liczba postów: ")
label_lokalizacja = Label(ramka_formularz, text= "Lokalizacja: ")

entry_imie = Entry(ramka_formularz)
entry_nazwisko = Entry(ramka_formularz)
entry_posty = Entry(ramka_formularz)
entry_lokalizacja = Entry(ramka_formularz)

label_formularz.grid(row=0, column=0, columnspan=2)
label_imie.grid(row=1,column=0, sticky=W)
label_nazwisko.grid(row=2,column=0, sticky=W)
label_posty.grid(row=3,column=0,  sticky=W)
label_lokalizacja.grid(row=4,column=0, sticky=W)

entry_imie.grid(row=1, column=1)
entry_nazwisko.grid(row=2, column=1)
entry_posty.grid(row=3, column=1)
entry_lokalizacja.grid(row=4, column=1)

button_dodaj_uzytkownika=Button(ramka_formularz, text="Dodaj użytkownika: ")
button_dodaj_uzytkownika.grid(row=5,column=1, columnspan=2)


#szczegoły
label_szczegoly_obiektow = Label(ramka_szczegoly_obiektow, text= "Szczegóły użytkownika: ")
label_imie_szcegoly_obiektow = Label(ramka_szczegoly_obiektow, text= "Imie: ")
label_nazwisko_szcegoly_obiektow = Label(ramka_szczegoly_obiektow, text= "Nazwisko: ")
label_posty_szczegoly_obiektow = Label(ramka_szczegoly_obiektow, text= "Liczba postów: ")
label_lokalizacja_szczegoly_obiektow= Label(ramka_szczegoly_obiektow, text= "Lokalizacja: ")


label_imie_szcegoly_obiektow_wartosc = Label(ramka_szczegoly_obiektow, text= ".... ")
label_nazwisko_szcegoly_obiektow_wartosc = Label(ramka_szczegoly_obiektow, text= ".... ")
label_posty_szczegoly_obiektow_wartosc = Label(ramka_szczegoly_obiektow, text= ".... ")
label_lokalizacja_szczegoly_obiektow_wartosc = Label(ramka_szczegoly_obiektow, text= ".... ")


label_szczegoly_obiektow.grid(row=0,column=0, sticky=W)
label_imie_szcegoly_obiektow.grid(row=1,column=0)
label_imie_szcegoly_obiektow_wartosc.grid(row=1,column=1)
label_nazwisko_szcegoly_obiektow.grid(row=1,column=2)
label_nazwisko_szcegoly_obiektow_wartosc.grid(row=1,column=3)
label_posty_szczegoly_obiektow.grid(row=1,column=4)
label_posty_szczegoly_obiektow_wartosc.grid(row=1,column=5)
label_lokalizacja_szczegoly_obiektow.grid(row=1,column=6)
label_lokalizacja_szczegoly_obiektow_wartosc.grid(row=1,column=7)

root.mainloop()
