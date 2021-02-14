first_name = "jouda"
last_name = "almeghari"
full_name = f"{first_name} {last_name}"  # f-strings(f for format )
print(full_name)
print(f"Hello, {full_name.title()}!")  # .title changes the name to title case

massage = f"Hello, {full_name.title()}!"  # f-string can be used to hold a massage,
                                           # and then assign it to a variable print(massage)
print("jouda\nasaad\nalmeghari")    #\n means new line
print("jouda\tasaad\talmeghari")    #\t for tab space

fav_lang = "    python   "
fav_lang1 = fav_lang.strip()        #strip clears extra spaces on both side of a string
fav_lang2 = fav_lang.rstrip()       #trip clears extra spaces on both side of a string## print(fav_lang1)
fav_lang3 = fav_lang.lstrip()

print(fav_lang1)
print(fav_lang2)
print(fav_lang3)

#up-to-date with main