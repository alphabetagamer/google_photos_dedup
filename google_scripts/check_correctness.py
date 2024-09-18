import json

with open("files_account_1.json", "r") as file:
    og_data = json.load(file)
with open("files_account_1_post_delete.json", "r") as file:
    del_data = json.load(file)
with open("files_account_1_dupes_left.json", "r") as file:
    dupe_data = json.load(file)

deleted = set([i["filename"] for i in og_data]) - set([i["filename"] for i in del_data])
dupe_data_f = [i["filename"] for i in dupe_data]

why = [i for i in deleted if i not in dupe_data_f]

print(len(deleted))
print(len(dupe_data_f))
print(len([i for i in deleted if i not in dupe_data_f]))

print([i for i in og_data if i["filename"] in why])
