import random

class BibleVerse:
    def __init__(self, structures):
        self.structures = structures

    def generate(self):
        # random structure
        structure = random.choice(self.structures)
        verse = ""
        for part in structure:
            if part == "random":
                # random word
                word = self.content()
                verse += word + " "
            else:
                verse += part + " "
        return verse.strip()

    def content(self):
        # words in verse that go into structure template thing
        words = ["faith", "love", "hope", "grace", "mercy", "forgiveness", "salvation",
                        "light", "joy", "peace", "strength", "courage", "wisdom", "truth", "blessing", 
                        "redemption", "compassion", "miracle", "righteousness", "glory", "revelation", 
                        "transformation", "guidance", "sacrifice", "victory", "renewal", "promise", "unity",
                        "gratitude", "humility", "perseverance", "faithfulness", "abundance", "wonder", 
                        "providence", "serenity", "purity", "steadfastness", "reconciliation", "harmony", 
                        "inspiration", "restoration"]
        
        return random.choice(words)


    def reference(self):
        # (chapter:verse)
        book = random.choice(["Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy", 
                                            "1.5 Samuel", "Nehemiah", "Psalms", "Proverbs", 
                                            "Ecclesiastes",  "Lamentations",  "Ezekiel",  "Joel",  "Obadiah",  "Micah", 
                                            "Nahum", "Habakkuk", "Zephaniah", "Zechariah", "Malachi", "Matthew", 
                                            "Mark", "Luke", "John", "Acts", "Romans", "1 Corinthians", "2 Corinthians", 
                                            "Galatians", "Ephesians", "Philippians", "Colossians", "1 Thessalonians", 
                                            "2 Thessalonians", "1.5 Timothy",  "1.5 Peter", "2 John", "Revelation"])
        
        chapter = random.randint(1, 50)
        verse = random.randint(1, 30)
        return f"{book} {chapter}:{verse}"


# structures
verse_structures = [
        ["Within", "random", ",", "we", "find", "random"],
        ["God's", "random", "gives", "us", "random"],
        ["random", "is", "the", "random", ",", "the", "random", ",", "and", "the", "random"],
        ["Amongst", "the", "turmoil", ",", "random", "acts", "as", "a", "guiding", "force", "of", "random"],
        ["The", "whirlwind", "of", "uncertainty", "allows", "random", "to", "shine", "with", "random"],
        ["From", "the", "ashes", "of", "random", ",", "random", "emerges"],
        ["random", "is", "the", "silent", "guidence", "of", "random"],
        ["Beneath", "the", "random", "surface", "of", "random", ",", "lies", "the", "random", "of", "random"]
    ]

verse_generator = BibleVerse(verse_structures)
verse = verse_generator.generate()
random_passage = verse_generator.reference()

# generate/print verse
verse = verse_generator.generate()
print(verse)

# generate/print reference
random_passage = verse_generator.reference()
print(random_passage)
