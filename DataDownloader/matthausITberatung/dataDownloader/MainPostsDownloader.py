import re


class MainPostsDownloader:

    def getWholeMainUsersOpinionsArrayOfArrays(self, listOfBeautifulSoupObjects):
        wholeMainUsersOpinionsArrayOfArrays = []
        for beautifulSoupObjects in listOfBeautifulSoupObjects:
            wholeMainUsersOpinionsArrayOfArrays.append(self.getMainUsersOpinions(beautifulSoupObjects))
        return wholeMainUsersOpinionsArrayOfArrays

    def getMainUsersOpinions(self, beautifulSoupObject):
        usersOpinionsArray = []
        for item in self.gatDataArray(beautifulSoupObject):
            userPost = self.getProcessedSingleRow(item)
            usersOpinionsArray.append(self.getExtractedUserOpinion(userPost))
        return usersOpinionsArray

    def getExtractedUserOpinion(self, userPost):
        return userPost[len(userPost) - 1].replace("|", "").lstrip().rstrip()

    def getProcessedSingleRow(self, item):
        return item.find('div').find('div').findAll(text=True)

    def gatDataArray(self, beautifulSoupObject):
        return beautifulSoupObject.findAll('div', id=re.compile("anchor"))


