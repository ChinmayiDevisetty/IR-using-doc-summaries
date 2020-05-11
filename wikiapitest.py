import wikipedia
page = wikipedia.page("google")
#print(page.content)
l=wikipedia.search("machine learning")
print(page.title)
for i in l:
    print(i)
