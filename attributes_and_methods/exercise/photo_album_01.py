class PhotoAlbum:
    page_space = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]
        self.counter = 0

    @classmethod
    def from_photos_count(cls, photos_count):
        new_pages = photos_count / 100 * 25
        return cls(int(new_pages))

    def add_photo(self, label):
        current_page = self.photos[self.counter]
        if len(current_page) == PhotoAlbum.page_space:
            self.counter += 1

        if self.counter >= self.pages:
            return "No more free spots"

        self.photos[self.counter].append(label)
        current_slot = len(self.photos[self.counter])
        return f"{label} photo added successfully on page {self.counter+1} slot {current_slot}"

    def display(self):
        strings = f"-----------\n"
        result = strings
        result += ''.join(f"{' '.join(['[]'] * len(page))}\n{strings}" for page in self.photos)
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())



