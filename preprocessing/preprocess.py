import sys, os

regions_to_states = {
    1: ["CT", "ME", "MA", "NH", "RI", "VT"],
    2: ["NJ", "NY"],
    3: ["DE", "MD", "PA", "VA", "WV"],
    4: ["AL", "FL", "GA", "KY", "MS", "NC", "SC", "TN"],
    5: ["IL", "IN", "MI", "MN", "OH", "WI"],
    6: ["AR", "LA", "NM", "OK", "TX"],
    7: ["IA", "KS", "MO", "NE"],
    8: ["CO", "MT", "ND", "SD", "UT", "WY"],
    9: ["AZ", "CA", "HI", "NV"],
    10: ["AK", "ID", "OR", "WA"]
}

reduced_regions_to_states = {
    4: ["AL"],
    10: ["AK"],
    6: ["AR"],
    9: ["AZ", "CA"],
}

for region in regions_to_states:
    states = regions_to_states[region]
    region_path = "./region_{}".format(str(region))
    if not os.path.isdir(region_path):
        os.mkdir(region_path)
    for state in states:
        for i in range(1, 21):
            with open(os.path.join("../data/{}/{}.txt".format(state, str(i)))) as raw_file:
                text = raw_file.read()
                if len(text) < 5:
                    print("Text file {} in state {} not filled out!".format(i, state))
                while "\n\n" in text:
                    text = text.replace("\n\n", "\n")
                text = text.replace("\n", " ")
            with open(os.path.join(region_path, "{}_{}.txt".format(state, i)), "w") as out_file:
                out_file.write(text)
