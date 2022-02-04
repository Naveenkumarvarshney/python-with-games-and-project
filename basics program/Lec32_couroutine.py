def searcher():
    import time
    book="Hello how are you naveen"
    time.sleep(2)
    # print(book)

    while True:
        text=(yield)
        if text in book:
            print("this is present")
            print(f"{text} is present")
        else:
            print("This is not present")    

search=searcher()
print("this is starting of couroutine")
next(search)

# search.send("naveen")
# search.close()

