import json

with open("files_account_1.json", "r") as file:
    data = json.load(file)
with open("files_account_2.json", "r") as file:
    og_data = json.load(file)
print(len(data))
print(len(og_data))


file_names_og = [i["filename"] for i in og_data]
file_names = [i["filename"] for i in data]

dupes_og = len(file_names_og) - len(set(file_names_og))
print("There are", dupes_og, "duplicates in the og storage itself.")
dupes = [i for i in file_names if i in file_names_og]
print("There are", len(dupes), "duplicates.")

url_list = []
for i in dupes:
    for j in og_data:
        if j["filename"] == i:
            url_list.append(j)
with open("url_remove.json", "w") as file:
    json.dump(url_list, file, indent=4)
