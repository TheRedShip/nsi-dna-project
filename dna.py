from database import Query
from constants import DNA_CONVERT_RULES, DNA_CONVERT_OFFSET

def FetchAllDNANames():
    return Query("SELECT `geneId`, `name` FROM dna_genes")

def GetDNAFromId(geneId):
    result = Query("SELECT `geneId`, `name`, `originalText`, `convertedText` FROM dna_genes WHERE geneId = ?", geneId)
    if len(result) == 0:
        return

    return DNA(result[0][2], result[0][3], result[0][1], result[0][0])

class DNA:

    def __init__(self, originalGen, convertedGen = None, name = None, geneId = None):
        self.originalGen = originalGen
        self.convertedGen = convertedGen
        self.geneId = geneId
        self.geneName = name
        self.__initialize()

    def __convert(self):
        convertedGen = ""

        for charIndex in range(DNA_CONVERT_OFFSET, len(self.originalGen), 3):
            sequence = self.originalGen[charIndex:charIndex + 3]

            if (len(sequence) == 3):

                convertedWay = DNA_CONVERT_RULES[sequence[0]][sequence[1]]

                for finalWayIndex in range(len(convertedWay)):

                    finalWay = convertedWay[finalWayIndex]
                    if (sequence[2] in finalWay[0]):
                        convertedGen += finalWay[1]

        self.convertedGen = convertedGen
        return self.convertedGen

    def __initialize(self):
        if (self.geneId): 
            return

        result = Query(
            """
            SELECT `geneId` FROM dna_genes
            WHERE `originalText` = ? 
            LIMIT 1
        """, self.originalGen)

        if len(result) > 0:
            self.geneId = result[0].geneId
        else:
            self.__convert()
            result = Query(
                """
                INSERT INTO dna_genes (
                    `name`,
                    `originalText`,
                    `convertedText`
                )
                VALUES (?, ?, ?)
             """,
                'qsdqsdqsd',
                self.originalGen,
                self.convertedGen,
            )

    def search(self, word: str):
        wordIndex = 0

        occurences = []
        while len(word) > wordIndex:
            lastOccurence = 0

            if (occurences != []):
                lastOccurence = occurences[len(occurences) - 1]

            newIndex = self.convertedGen.find(word[wordIndex], lastOccurence)

            if (newIndex != -1):
                occurences.append(newIndex)
            else:
                return {
                    "finded": False,
                    "occurences": []
                }

            wordIndex += 1

        return {
            "finded": True,
            "occurences": occurences
        }

    def searchHard(self, word: str):
        wordIndex = 0

        occurences = []
        lastTry = 0

        while lastTry < len(self.convertedGen) - 1:
            newIndex = self.convertedGen.find(word[wordIndex], lastTry)
            if (newIndex != -1):
                for char in word:
                    if (self.convertedGen[newIndex] == word[wordIndex]):
                        occurences.append(newIndex)
                        newIndex += 1
                        wordIndex += 1
                        lastTry += 1
                    else:
                        occurences = []
                        wordIndex = 0

                    if (wordIndex == len(word)):
                        return [True, occurences]
            else:
                return [False, []]
