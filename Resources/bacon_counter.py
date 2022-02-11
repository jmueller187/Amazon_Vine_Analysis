# Import mrjob
from mrjob.job import MRJob

# Create Bacon_count class
class Bacon_count(MRJob):
    # Create a mapper() function
    def mapper(self, _, line):
        for word in line.split():
            if word.lower() == "bacon":
                yield "bacon", 1

    # Crate reducer() function
    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == "__main__":
    Bacon_count.run()
