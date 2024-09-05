print("\n\nЗадача №1\n")
number = float(input("Введіть число: "))
if number > 0:
    print("Positive")
elif number == 0:
    print("Zero")
else:
    print("Negative")

print("\n\nЗадача №2\n")
number = int(input("Введіть число: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

print("\n\nЗадача №3\n")
day = int(input("Введіть число від 1 до 7: "))
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

if 1 <= day <= 7:
    print(days_of_week[day - 1])
else:
    print("Невірне число! Введіть число від 1 до 7.")

print("\n\nЗадача №4\n")
score = int(input("Введіть оцінку від 0 до 100: "))

if 0 <= score <= 100:
    if score >= 90:
        print("A")
    elif score >= 82:
        print("B")
    elif score >= 75:
        print("C")
    elif score >= 64:
        print("D")
    elif score >= 60:
        print("E")
    else:
        print("F")
else:
    print("Оцінка має бути між 0 і 100.")

print("\n\nЗадача №5\n")
exit_keywords = ["Bye", "Good bye", "Have a nice day", "Farewell", "See you later"]

while True:
    text = input("Введіть рядок: ")
    if text in exit_keywords:
        print("Папуга: До побачення!")
        break
    print("Папуга:", text)

print("\n\nЗадача №6\n")
word_list = ["apple", "banana", "orange", "grape", "kiwi", "mango", "lemon", "lime", "pear", "peach"]

word = input("Введіть слово: ")

if word in word_list:
    print(f"Індекс слова {word}: {word_list.index(word)}")
else:
    print("Слово не знайдено.")

print("\n\nЗадача №7\n")
countries = {
    "Ukraine": "Kyiv",
    "France": "Paris",
    "Germany": "Berlin",
    "Spain": "Madrid",
    "Italy": "Rome",
    "USA": "Washington",
    "Canada": "Ottawa",
    "Japan": "Tokyo",
    "China": "Beijing",
    "India": "New Delhi"
}

country = input("Введіть назву країни: ")

if country in countries:
    print(f"Столиця {country}: {countries[country]}")
else:
    print("Країна не знайдена.")

print("\n\nЗадача №8\n")
teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']

for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(f"{home_team} VS {away_team}")

print("\n\nЗадача №9\n")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Введіть число для обчислення факторіалу: "))
print(f"Факторіал {number} дорівнює {factorial(number)}")

print("\n\nЗадача №10\n")
def recursive_reverse(n):
    if n == 0:
        return
    num = int(input())
    recursive_reverse(n - 1)
    print(num, end=' ')

n = int(input("Введіть кількість елементів: "))
print("Введіть елементи:")
recursive_reverse(n)
