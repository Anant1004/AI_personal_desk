from google import search

ip=raw_input("What would you like to search for? ")

for url in search(ip, stop=20):
    print(url)