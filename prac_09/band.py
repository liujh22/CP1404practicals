"""
Class "band"
"""


class Band:
    """Band Class"""

    def __init__(self, name=""):
        """Construct a Band with a name and empty musician list."""
        self.name = name
        self.musician = []

    def add(self, musician):
        """Add a musician to a band."""
        self.musician.append(musician)

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({self.musician[0]})"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(vars(self))

    def play(self):
        """Return a string showing the musician playing their instrument."""
        if not self.musician:
            return f"{self.musician[0]} needs an instrument!"
        return f"{self.musician[0]} is playing: {self.musician[1]}"

