# HACKATHON 2023

## Założenie konta github
- Wejść na stronę github.com
- Użyć przycisku Sign up

## Utworzenie tokena github
Na podstawie
https://docs.github.com/en/enterprise-server@3.4/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

- Po zalogowaniu na konto github wejść na ustawienia (Prawy górny róg -> rozwinięcie ikony -> Settings)
- W lewym menu wejść na Developer settings.
- Dalej "Personal access tokens" -> Tokens (classic) -> Generate a personal access token
- W polu Note ustawić nazwę tokena (np. Hackathon 2023).
- Zaznaczyć jego właściwości (można wszystkie).
- Kliknąć Generate Token.
- Przejść do widoku na którym widać wygenerowany token (Będzie on widoczny tylko raz).
- Skopiować go i zachować.

## Wykonanie forka projektu

- Wejść na https://github.com/lkmiecik/room-booking
- Rozwinąć menu Fork (w prawym górnym rogu), a potem kliknąć Create a new fork.
- Można zostawić ustawienia domyślne i kliknąć Create fork.

Po tym działaniu utworzone zostanie nowe repozytorium
https://github.com/[użytkownik]/room-booking

## Klonowanie projektu. (Zwrócić uwagę żeby sklonować fork, a nie oryginalny projekt)
- Wejść do PowerShell
- Wykonać
```bash
git clone https://github.com/[użytkownik]/room-booking.git
```


## Otwieranie projektu

Otworzyć sklonowany katalog ./room-booking w PyCharm.

Jeśli pojawi się pytanie:

File requirements.txt contains project dependencies. Would you like to create a virtual environment using it?

Należy sprawdzić ścieżki i wersję Pythona (powinna być 3.10) i kliknąć OK.

Jeśli pojawi się problem kliknąć OK.

Sprawdzić czy w projekcie pojawił się katalog venv.

Otworzyć terminal:
 View -> Tool Windows -> Terminal
 
Sprawdzić zainstalowane biblioteki:
```bash
pip list
```
Jeśli nie ma django wykonać:
```bash
pip install -r requirements.txt
```


## Uruchamianie projektu (dwa sposoby)

### Z terminala

Wejść do katalogu RoomBooking:
```bash
cd RoomBooking
```

i uruchomić
```bash
python manage.py runserver
```

### Za pomocą przycisku Play w PyCharm

#### Aby móc używać przycisku Play  w PyCharm należy
- Skonfigurować uruchamianie
  - Run -> Edit Configurations -> Add new... (lub plusem w lewym górnym rogu) -> Python
  - Uzupełnić formularz
    - Script path: (tu wybrać plik) ./room-booking/RoomBooking/manage.py
    - Parameters: runserver
  - Apply -> Ok
  - Po tej operacji ikona Play oraz będąca przy niej ikona do debugowania zmieniają kolor na zielony.

#### Aby uruchomić aplikację należy kliknąć w ikonę Play

#### Aby uruchomić aplikację w trybie debug należy kliknąć w ikonę debugowania obok Play

Po kliknięciu może pojawić się komunikat:

Zapora Windows Defender zablokowała nietóre funkcje tej aplikacji.

Należy kliknąć "Zezwalaj na dostęp".

Po uruchomieniu w trybie debug można oznaczyć miejsca zatrzymania klikając dwukrotnie na numer wiersza w wybranym pliku *.py i badać aktualny stan aplikacji.


### W przeglądarce uruchomić  http://127.0.0.1:8000/

## Dodawanie biblioteki

W katalogu room-booking wykonać

```bash
pip install [nazwa biblioteki]
```

Np.

```bash
pip install numpy
```
Następnie trzeba zaktualizować plik requirements.txt

```bash
pip freeze > requirements.txt
```

## Wysyłanie kodu do repozytorium

Otworzyć PowerShell i przejść do katalogu room-booking

Wykonać

```bash
git add .
```
który dodaje wszystkie nowe oraz zmienione pliki, lub dodawać tylko wybrane pliki

```bash
git add [filepath1]
git add [filepath2]
git add ...
```

Następnie wykonać commit z odpowiednim komentarzem

```bash
git commit -m "[komentarz]"
```
Np.

```bash
git commit -m "add numpy library"
```

Wysłać kod poleceniem

```bash
git push
```

Gdy otworzy się okno dialogowe wybrać Token.

Wkleić wcześniej wygenerowany token i kliknąć Sign in.

## Wykonanie Pull Request

Wejść na stronę forka projektu
https://github.com/[użytokwnik]/room-booking

Rozwinąć menu Contribute i kliknąć Open Pull Request