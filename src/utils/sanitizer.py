from urllib.parse import urlsplit

class Sanitizer:
    def sanitizeLink(self, link):
        splitResult = urlsplit(link)
        return "{scheme}://{netloc}{path}".format(
            scheme=splitResult.scheme,
            netloc=splitResult.netloc,
            path=splitResult.path
        )