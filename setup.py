import sys
import csv
import gensim
import logging

from gensim.models import KeyedVectors

from w2vConstituicaoConfiguration import w2vConstituicaoConfiguration

logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s',
    level=logging.INFO)


def read_input(input_file):
    with open(input_file, 'rb') as file:
        for i, line in enumerate(file):

            if (i % 100 == 0):
                logging.info("read {0} reviews".format(i))

            yield gensim.utils.simple_preprocess(line)

def getDocument():
    return list(read_input(w2vConstituicaoConfiguration.getFileName()))

def main():
    documents = getDocument()
    logging.info("Done reading data file")

    # build vocabulary and train model
    model = gensim.models.Word2Vec(
        documents,
        size=150,
        window=10,
        min_count=2,
        workers=10)
    model.train(documents, total_examples=len(documents), epochs=10)

    wordVectors = model.wv

    # Create a array with all words and the number of repetitions in the document
    allWords = []
    for word, vocabObj in wordVectors.vocab.items():
        allWords.append({
            'word': word,
            'repetition': vocabObj.count
        })

    # Order desc all words by number of repetitions (TODO: Please be more efficient)
    logging.info("Order all words desc")

    numberOfWords = len(allWords)
    allWordsDesc = []
    for i in range(0, numberOfWords):
        repetition = -1
        indexWord = -1

        for word in allWords:
            if (repetition < word['repetition']):
                repetition = word['repetition']
                indexWord = allWords.index(word)

        allWordsDesc.append(allWords[indexWord])
        allWords.pop(indexWord)

    # Create a CSV with all words and number of repetitions
    logging.info("Create a CSV file with all words in the document")

    with open('csv/allwords.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['word', 'repetition']
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(fieldnames)

        for word in allWordsDesc:
            writer.writerow([word['word'], word['repetition']])


    listWordsValidation = ["presidente", "vereadores", "deputados", "homem", "mulher", "criança", "petróleo", "gás", "minerais", "crimes", "jurisdição"]
    mostSimilarWords = []
    for word in listWordsValidation:
        tempArray = [word]
        mostSimilar = model.wv.most_similar(
            positive=[word],
            topn=10
        )

        for similar in mostSimilar:
            tempArray.append(similar)

        mostSimilarWords.append(tempArray)

    with open('csv/mostsimilarwords.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')

        for word in mostSimilarWords:
            writer.writerow(word)

    # look up top 6 words similar to 'polite'
    # w1 = ["mulher"]
    # print(
    #     "Most similar to {0}".format(w1),
    #     model.wv.most_similar(
    #         positive=w1,
    #         topn=15))


    # look up top 6 words similar to 'polite'
    # w1 = ["homem"]
    # print(
    #     "Most similar to {0}".format(w1),
    #     model.wv.most_similar(
    #         positive=w1,
    #         topn=15))

    # look up top 6 words similar to 'polite'
    # w1 = ["direito"]
    # print(
    #     "Most similar to {0}".format(w1),
    #     model.wv.most_similar(
    #         positive=w1,
    #         topn=6))



if __name__ == '__main__':
    main()