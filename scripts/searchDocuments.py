import os
from datetime import datetime

class searchEngine:
    def __init__(self):
        self.indexes = {}
        self.stopWords = {'the', 'is', 'and', 'in', 'to', 'of', 'a', 'with', 'for', 'on', 'by'}

    def readFile(self, filePath):
        try:
            with open(filePath, 'r') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            print(f'The file {filePath} does not exist.')
        
        return None

    def insertInDictionary(self, fileName, contentWords):
        # Remove .txt if any word has
        if 'txt' in fileName:
            fileName = fileName.split('.')[0]

        for wordInFileName in fileName.split() + contentWords:
            wordInFileName = wordInFileName.lower()

            if '.' in wordInFileName:
                wordInFileName = wordInFileName.replace('.', '')
            if ',' in wordInFileName:
                wordInFileName = wordInFileName.replace(',', '')

            if wordInFileName not in self.indexes:
                self.indexes[wordInFileName] = [fileName]
            elif fileName not in self.indexes[wordInFileName]:
                self.indexes[wordInFileName].append(fileName)

    def createIndexes(self, documentsFolderPath):
        for filename in os.listdir(documentsFolderPath):
            if filename.endswith('.txt'):
                filePath = os.path.join(documentsFolderPath, filename)
                fileContent = self.readFile(filePath)

                if fileContent:
                    fileContent = self.filterImportantWords(fileContent)

                self.insertInDictionary(filename, fileContent)

    def filterImportantWords(self, text):
        wordsList = []
        for word in text.split():
            if word not in self.stopWords:
                wordsList.append(word)

        return wordsList

    def searchDocuments(self, query):
        if len(self.indexes) == 0:
            displayMsg('Create Indexes to search a document!')
            return None
        
        results = []
        for subQuery in query.split():
            subQuery = subQuery.lower()
            if subQuery in self.indexes:
                results.extend(self.indexes[subQuery])

        if len(results) == 0:
            displayMsg('No Document found against the query!')
        
        return results

    def lookupIndexes(self):
        if len(self.indexes) == 0:
            return displayMsg('Create indexes to look up!')

        print('\n-------------------------------------')
        for index in self.indexes:
            print(index, '=>', end=' ')
            for file in self.indexes[index]:
                print('\t', file, end=', ')
            print()
        print('-------------------------------------')

    def displayResult(self, query, result):
        print('\n-------------------------------------')
        print('Searched Query: ', query)
        if len(result) == 0:
            print('No Documents found!')
        else:
            print('Results:')
            for index, file in enumerate(result):
                print('\t', index + 1, file)
        print('-------------------------------------')


def displayMsg(msg):
    print('\n-------------------------------------')
    print(msg)
    print('-------------------------------------')

if __name__ == '__main__':
    documentsFolderPath = './documents'
    searchEngineInstance = searchEngine()

    while True:
        print('\nMenu:')
        print('1. Create Indexes')
        print('2. Lookup Indexes')
        print('3. Search FileName')
        print('4. Exit')

        choice = input('Enter your choice (1-4): ')

        startTime = datetime.now()
        if choice == '1':
            searchEngineInstance.createIndexes(documentsFolderPath)
            displayMsg('Indexes created successfully!')
        elif choice == '2':
            searchEngineInstance.lookupIndexes()
        elif choice == '3':
            query = input('\nEnter Query: ')
            startTime = datetime.now()
            results = searchEngineInstance.searchDocuments(query)
            if results:
                searchEngineInstance.displayResult(query, results)
        elif choice == '4':
            print('Exiting program.')
            break
        else:
            displayMsg('Invalid choice. Please enter a number between 1 and 4.')

        timeDifference = (datetime.now() - startTime).total_seconds() * 10**3
        print("Execution time of program is: ", timeDifference, "ms")