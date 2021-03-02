mydict = {"А": "6", 
          "Б": "?", 
          "В": "%", 
          "Г": "9", 
          "Д": "E", 
          "Е": "S", 
          "Ё": "$", 
          "Ж": "!", 
          "З": "^", 
          "И": "*", 
          "Й": "#", 
          "К": "?", 
          "Л": "=", 
          "М": ">", 
          "Н": "<", 
          "О": "+", 
          "П": "-", 
          "Р": "/", 
          "С": "\\",
          "Т": ".",
          "У": ",",
          "Ф": "_",
          "Х": ";",
          "Ц": ":",
          "Ч": "A",
          "Ш": "Y",
          "Щ": "Z",
          "Ы": "X",
          "Ь": "8",
          "Ъ": "1",
          "Э": "@",
          "Ю": "(",
          "Я": ")",
          " ": "{",
}

def GetKey(val):
   for key, value in mydict.items():
      if val == value:
         return key


def cipher(plaintext):
    ciphertext = ""
    for i in plaintext:
        ciphertext = ciphertext + mydict[i.upper()]
    print(ciphertext)

def decipher(ciphertext):
    plaintext = " "
    for i in ciphertext:
        plaintext = plaintext + GetKey(i)
    print(plaintext)


def atbash(s):
    abc = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    return s.translate(str.maketrans(abc + abc.upper(), abc[::-1] + abc.upper()[::-1]))


def caesar(text, rotation):
    alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    res = ''
    for c in text:
        if c != " ":
            res += alpha[(alpha.index(c) + rotation) % len(alpha)]
        else:
            res += " "
    print(res)

def rot13(text):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    for c in text:
        if c != " ":
            res += alpha[(alpha.index(c) + 13) % len(alpha)]
        else:
            res += " "
    print(res)



# Шифр простой замены
print("Substitution:")
substitution="\/6%<*.8\){\{\+=<:S>{%{\*)**{*{-/S%^+#.*{S9+{%{E+=9+=S.**"
decipher(substitution)

# Шифр Цезаря
caesarcipher="фъощфйи цэрыфйи нъэркй"
print("Caesar:")
caesar(caesarcipher, 23)


# Rot13
rot13cipher = "tbbq yhpx"
print("Rot13:")
rot13(rot13cipher)

atbashcipher = "цскротяицрссяа юъчрпянсрнмг"
print("Atbash:")
print(atbash(atbashcipher))