from database import Query
from constants import DNA_CONVERT_RULES, DNA_CONVERT_OFFSET


class ADN:

    def __init__(self, originalGen):
        self.originalGen = originalGen
        self.convertedGen = None
        self.geneId = None
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
                'qsd',
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
                return [False, []]

            wordIndex += 1

        return [True, occurences]

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
