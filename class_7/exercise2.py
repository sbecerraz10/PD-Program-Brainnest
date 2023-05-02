from dataclasses import dataclass
import json

@dataclass
class Book:
    title: str
    author: str
    year: int
    pages: int
    rating: float
    publisher: str
    genres : list[str]

    def has_genre(self, genre) -> bool:
        return genre in self.genres


    def to_dict(self) -> dict:
        return vars(self)

book_1 = Book("The Power Of Now", "Eckhart Tolle", 1997, 205, 4.6, "Namaste", ["Self-growth", "Psychology"])
book_2 = Book("Lord of the Rings","That Author Guy",2020,3000,4.75,"That Publisher Guy",["Fantasy", "Action", "Drama"])
book_3=Book("Avengers","Tony",1,100,5.0,"actions",["Action","Adventure","Thriller","Drama"])

print(book_1.has_genre("Psychology"))
print(book_1.to_dict())
print(book_2.has_genre("Fantasy"))
print(book_2.to_dict())
print(book_3.has_genre("Action"))
print(book_3.to_dict())