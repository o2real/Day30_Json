# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"That key{error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Huma Height shuold not over 3 meters.")

bmi = weight / height ** 2
print(bmi)