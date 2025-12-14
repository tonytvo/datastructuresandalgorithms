class CanPlaceFlowers:
    def canPlaceFlowers(self, flowerbeds, numberOfFlowers: int) -> bool:
        """Return True if `n` flowers can be planted without adjacency (inputs stay unchanged)."""
        if numberOfFlowers <= 0:
            return True

        length = len(flowerbeds)
        if length == 0:
            return False

        greedyFlowerBeds = flowerbeds[:]  # work on a copy to avoid mutating the caller's list
        for plantedIndex in range(length):
            if self.canFlowerBePlantedAt(greedyFlowerBeds, plantedIndex, length):
                greedyFlowerBeds[plantedIndex] = 1
                numberOfFlowers -= 1
                if numberOfFlowers == 0:
                    return True

        return numberOfFlowers <= 0

    def canFlowerBePlantedAt(self, greedyFlowerBeds, plantedIndex: int, length: int) -> bool:
        if greedyFlowerBeds[plantedIndex] != 0:
            return False

        isThereLeftFlowerAdjacent = (plantedIndex == 0) or (greedyFlowerBeds[plantedIndex - 1] == 0)
        isThereRightFlowerAdjacent = (plantedIndex == length - 1) or (greedyFlowerBeds[plantedIndex + 1] == 0)
        canFlowwerBePlantedAt = isThereLeftFlowerAdjacent and isThereRightFlowerAdjacent
        return canFlowwerBePlantedAt
