books = {
    "Life of Pi": "Adventure Fiction", 
    "The Three Musketeers": "Historical Adventure",
    "Watchmen": "Comics", 
    "Bird Box": "Horror",
    "Harry Potter":"Fantasy Fiction",
    "Good Omens": "Comedy"
}

book = input()

genre = books.get(book, "Book not found")
print(genre)

"""
Rewrite the given code to use the .get() method instead of the if/else statements.
Also, change the output to "Book not found", when the book is not found.
"""
