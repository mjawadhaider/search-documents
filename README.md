### 1. Introduction

The `search-documents` algorithm is designed to provide a reliable and efficient search mechanism for document files stored in a directory. Its purpose is to simplify the process of finding documents based on specific keywords or phrases, making it especially useful for environments that require fast access to large collections of text documents. This system preprocesses document content, builds an index, and provides a user-friendly interface to perform quick searches by leveraging optimized data structures and techniques for high performance.

---

### 2. Goals

The primary goals of the `search-documents` algorithm are:

- **Efficient Indexing**: Build a fast and lightweight index of document content to support quick keyword searches.
- **Scalable Search Mechanism**: Design the system to handle an increasing number of documents without significant performance degradation.
- **Flexible Query Processing**: Support various types of search queries, such as case-insensitive matches, by normalizing content during indexing and querying.
- **Extensibility**: Ensure the system can be easily extended to handle other file types, like PDFs and web pages, with minor adjustments.
- **Performance Optimization**: Track execution time for search queries to identify bottlenecks and optimize the algorithm as needed.

---

### 3. Implementation Plan

The implementation of the `search-documents` algorithm follows these steps:

- **Step 1**: Define the structure of the search engine class, including attributes like `indexes` (a dictionary to hold keywords and their respective documents) and `stopWords` (common words to exclude from indexing).
- **Step 2**: Develop methods for reading and processing files, including handling punctuation, case normalization, and word tokenization.
- **Step 3**: Build the `createIndexes` method to iterate through all documents, preprocess content, and populate the `indexes` dictionary.
- **Step 4**: Implement the `searchDocuments` method to allow users to search for keywords and retrieve a list of matching documents.
- **Step 5**: Integrate and test the entire system, checking functionality with sample text files and ensuring accurate and fast retrieval.

---

### 4. Approach

The approach for the `search-documents` algorithm emphasizes simplicity, efficiency, and scalability:

- **Indexing Strategy**: 
  - Use a dictionary structure to map keywords to documents, allowing quick lookups.
  - Keywords are extracted from both file names and file contents, providing a broad base for keyword searches.
- **Data Processing**:
  - Convert document content to lowercase and remove unnecessary punctuation to standardize the indexing.
  - Filter out common stop words to reduce the index size and focus only on meaningful keywords.
- **Data Structure**:
  - The dictionary-based `indexes` structure enables efficient storage and retrieval of keyword-document mappings, ensuring O(1) average time complexity for lookups.

---

### 5. Backend Concept

#### **Index Creation**
The `createIndexes` function is responsible for building the index by processing each document as follows:
- Read the document content and tokenize it into individual words.
- Remove stop words and punctuation from tokens, normalizing them into lowercase to ensure case-insensitive matching.
- Use the `insertInDictionary` method to add each unique, relevant keyword to the `indexes` dictionary, with each keyword mapped to a list of documents containing that keyword.

#### **Search Functionality**
The `searchDocuments` method processes search queries by:
- Splitting and normalizing the search terms in the query.
- Checking each term against the `indexes` dictionary to find matching documents.
- Aggregating and returning results, displaying all documents that contain any of the queried keywords.
- Logging execution time to facilitate performance tracking and optimization.

---

### 6. User Interface

The user interface is a text-based command menu that provides a simple and interactive experience for users to:
- **Create Indexes**: Users can choose to generate indexes for all documents in the specified directory.
- **Lookup Indexes**: The `lookupIndexes` feature allows users to view the internal index structure and verify keyword mappings.
- **Search FileName**: The search functionality enables users to enter keywords and retrieve matching document names quickly.
- **Exit**: A straightforward exit option to close the program.

Each option prompts the user and provides clear feedback messages to enhance usability. Execution time for search operations is displayed to indicate performance.

---

### 7. Conclusion / Ending

The `search-documents` algorithm successfully implements an efficient and scalable system for document indexing and searching. It meets key objectives of fast retrieval, case-insensitive search, and extensibility for future improvements. By leveraging a dictionary-based indexing approach and filtering out stop words, the algorithm ensures a manageable index size while maximizing search relevance. Future enhancements, such as supporting other file types (PDFs, web pages) and adding ranking algorithms for improved relevance, can make this tool even more robust and versatile.