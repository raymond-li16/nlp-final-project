import sys
import os

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", 
"ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", 
"MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", 
"PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

for state in states:
    if not os.path.isdir("./{}".format(state)):
        os.mkdir("./{}".format(state))
    for i in range(1, 21):
        f = open("{}/{}.txt".format(state, str(i)), "w")
        f.close()
