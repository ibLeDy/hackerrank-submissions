class TestDataEmptyArray(object):
    @staticmethod
    def get_array():
        return []


class TestDataUniqueValues(object):
    @staticmethod
    def get_array():
        return [3, 1]

    @staticmethod
    def get_expected_result():
        return 1


class TestDataExactlyTwoDifferentMinimums(object):
    @staticmethod
    def get_array():
        return [1, 1]

    @staticmethod
    def get_expected_result():
        return 0
