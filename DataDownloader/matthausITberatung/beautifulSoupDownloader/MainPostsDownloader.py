import re


class MainPostsDownloader:

    def getMainUsersOpinions(self, beautifulSoupObject):
        usersOpinionsArray = []
        for item in self.gatDataArray(beautifulSoupObject):
            userPost = self.processSingleRow(item)
            usersOpinionsArray.append(self.getExtractedUserOpinion(userPost))
        return usersOpinionsArray

    def getExtractedUserOpinion(self, userPost):
        return userPost[len(userPost) - 1].replace("|", "").lstrip().rstrip()

    def processSingleRow(self, item):
        return item.find('div').find('div').find_all(text=True)

    def gatDataArray(self, beautifulSoupObject):
        return beautifulSoupObject.findAll('div', id=re.compile("anchor"))


