from gensim.models import TfidfModel


class Utils:

    #It is filtering corpus from rare occurred low_value words and these which are not in tfidf model
    def filterCorpus(self, corpus, dictionary, low_value):
        tfidf = TfidfModel(corpus, id2word=dictionary)

        for i in range(0, len(corpus)):
            bow = corpus[i]
            tfidf_ids = [id for id, value in tfidf[bow]]
            bow_ids = [id for id, value in bow]
            low_value_words = [id for id, value in tfidf[bow] if value < low_value]
            words_missing_in_tfidf = [id for id in bow_ids if
                                      id not in tfidf_ids]  # The words with tf-idf socre 0 will be missing
            new_bow = [b for b in bow if b[0] not in low_value_words and b[0] not in words_missing_in_tfidf]
            # reassign
            corpus[i] = new_bow