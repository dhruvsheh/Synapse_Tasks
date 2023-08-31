jumbled_superheroes = ['DocToR_STRangE', 'SPidERmaN', 'MoON _KnigHT', 'caPTAIN_aMERICa', 'hULK']

indices = []
decoded_names = []

for index, name in enumerate (jumbled_superheroes):
    indices.append(index)
    decoded_names.append(name.replace("_", "").lower())

name_lengths = list(map(lambda name: len(name), decoded_names))
indices_sorted = sorted(indices, key=lambda index: name_lengths [index])
sorted_guest_list = [(i+1, decoded_names[index].title()) for i, index in enumerate(indices_sorted)]

print('Phase 5 kickoff list:')
for number, name in sorted_guest_list:
    print(f"({number}.{name}")
    