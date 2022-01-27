class SentimentHelper:

    def getListOfDateFlownAndOpinionFilteredByYear(self, dateAndOpinionList, year):
        lufthansaZippedListOfDateFlownAndOpinion = []
        for dateFlownAndOpinion in dateAndOpinionList:
            if dateFlownAndOpinion[0][len(dateFlownAndOpinion) - 6:] == str(year):
                lufthansaZippedListOfDateFlownAndOpinion.append(dateFlownAndOpinion)
        return lufthansaZippedListOfDateFlownAndOpinion

    def getDictOfDateFlownAndOpinionsFilteredByYear(self, listOfDateFlownAndOpinionFilteredByYear):
        dataDictOfDateFlownAndCollectedOpinions2021 = {}
        for dateFlown in lufthansaDateFlown2021Counter.keys():
            listOfOpinionsForCertainDate = []
            for dateFlownAndOpinion in listOfDateFlownAndOpinionFilteredByYear:
                if str(dateFlownAndOpinion[0]) == str(dateFlown):
                    listOfOpinionsForCertainDate.append(dateFlownAndOpinion[1])
            dataDictOfDateFlownAndCollectedOpinions2021[dateFlown] = ' '.join(listOfOpinionsForCertainDate)


