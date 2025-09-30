import string

class ReviewAnalyzer:
    def __init__(self, filename: str):
        self.reviews = []
        with open(filename, 'r') as file:
            for line in file:
                cleaned = line.strip()
                if cleaned:
                    self.reviews.append(cleaned)

        self.positive_words = {"good", "great", "excellent", "amazing", "recommend", "perfect"}
        self.negative_words = {"bad", "awful", "terrible", "hate", "poor", "slow"}

    def _get_words(self, text: str) -> set[str]:
        cleaned = text.lower().translate(str.maketrans('', '', string.punctuation))
        return set(cleaned.split())

    def count_positive_reviews(self) -> int:
        count = 0
        for review in self.reviews:
            words = self._get_words(review)
            if self.positive_words & words:
                count += 1
        return count

    def count_negative_reviews(self) -> int:
        count = 0
        for review in self.reviews:
            words = self._get_words(review)
            if self.negative_words & words:
                count += 1
        return count

    def average_review_length(self) -> float:
        if not self.reviews:
            return 0.0
        total_length = 0
        for review in self.reviews:
            review_length = len(review)
            total_length = total_length + review_length

        return total_length / len(self.reviews)

class SentimentReporter:
    def __init__(self, analyzer: ReviewAnalyzer):
        self.analyzer = analyzer

    def report_sentiment(self) -> str:
        pos = self.analyzer.count_positive_reviews()
        neg = self.analyzer.count_negative_reviews()

        if pos > neg:
            return "Overall Positive Sentiment"
        elif neg > pos:
            return "Overall Negative Sentiment"
        else:
            return "Mixed or Neutral Sentiment"

analyzer = ReviewAnalyzer("reviews.txt")
reporter = SentimentReporter(analyzer)

print("Positive reviews:", analyzer.count_positive_reviews())
print("Negative reviews:", analyzer.count_negative_reviews())
print("Average review length:", analyzer.average_review_length())
print("Sentiment report:", reporter.report_sentiment())