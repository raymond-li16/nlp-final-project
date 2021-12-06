from bs4 import BeautifulSoup
import requests
import sys, os
import shutil

file = "state_urls.txt"
urls = []
states = []
with open(file, 'r') as urls_file:
    lines = urls_file.readlines()
    for line in lines:
        url, state = line.split()
        urls.append(url)
        states.append(state)

def url_to_text(url):
	response = requests.get(url)
	assert(response.status_code == 200)
	html = response.text
	return BeautifulSoup(html, 'html.parser').get_text()

def state_file(state):
    return "./{}".format(state)

for state in states:
    if os.path.isdir(state_file(state)):
        shutil.rmtree(state_file(state))
    os.mkdir(state_file(state))

state_count = {state_name: 0 for state_name in set(states)}
for url, state in zip(urls, states):
    state_count[state] += 1
    content = url_to_text(url)
    outfile_name = os.path.join(state_file(state), str(state_count[state]) + ".txt")
    with open(outfile_name, 'w') as f:
        f.write(content)