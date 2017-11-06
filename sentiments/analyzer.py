import nltk


class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        self.positives = set()
        self.negatives = set()
        self.tokenizer = nltk.tokenize.casual.TweetTokenizer()
        # add positive words to set
        with open(positives) as lines:
            for line in lines:
                if line.startswith(";"):
                    continue
                word = line.strip()
                if word != "":
                    self.positives.add(word)
        # add negative words to set
        with open(negatives) as lines:
            for line in lines:
                if line.startswith(";"):
                    continue
                word = line.strip()
                if word != "":
                    self.negatives.add(word)

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""

        score = 0
        tokens = self.tokenizer.tokenize(text)
        for token in tokens:
            word = token.lower()
            # add 1 for positive words, subtract 1 for negatives
            if word in self.positives:
                score += 1
            elif word in self.negatives:
                score -= 1
        return score
