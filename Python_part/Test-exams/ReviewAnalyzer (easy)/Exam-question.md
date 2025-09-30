# Question

### Customer Review Sentiment Analysis

You are tasked with analyzing customer reviews stored in a text file.  
Each line in the file represents a single review, for example `reviews.txt`.


---

## Your Task

Design two Python classes:

### 1. `ReviewAnalyzer`
This class should:
- Read all reviews from the file.  
- Contain a predefined set of positive and negative words:
  - Positive: `"good"`, `"great"`, `"excellent"`, `"amazing"`, `"recommend"`, `"perfect"`  
  - Negative: `"bad"`, `"awful"`, `"terrible"`, `"hate"`, `"poor"`, `"slow"`  
- Provide the following methods:
  - `_get_words(text)`: Returns a set of lowercase words from the text, removing punctuation.  
  - `count_positive_reviews()`: Counts reviews containing at least one positive word.  
  - `count_negative_reviews()`: Counts reviews containing at least one negative word.  
  - `average_review_length()`: Returns the average length of the reviews in characters.  

### 2. `SentimentReporter`
This class should:
- Be initialized with a `ReviewAnalyzer` object.  
- Provide a method `report_sentiment()` that:
  - Returns `"Overall Positive Sentiment"` if positive reviews > negative reviews.  
  - Returns `"Overall Negative Sentiment"` if negative reviews > positive reviews.  
  - Returns `"Mixed or Neutral Sentiment"` otherwise.  

---

## Tasks

1. Implement the two classes described above.  
2. Demonstrate the code using the provided `reviews.txt`.  
3. Print:
   - Number of positive reviews  
   - Number of negative reviews  
   - Average review length  
   - Overall sentiment report  

---
