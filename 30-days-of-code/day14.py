def computeDifference(self):
    sorted_elements = sorted(self.__elements)
    self.maximumDifference = abs(
        sorted_elements[-1] - sorted_elements[0]
    )
