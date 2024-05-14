class CompareVersionNumbers:
    def compareVersion(self, version1: str, version2: str) -> int:
        list1 = version1.split('.')
        list2 = version2.split('.')
        if len(list1) > len(list2):
            for i in range(len(list1) - len(list2)):
                list2.append(0)
        elif len(list2) > len(list1):
            for i in range(len(list2) - len(list1)):
                list1.append(0)
        for i in range(len(list1)):
            if int(list1[i]) > int(list2[i]): return 1
            if int(list1[i]) < int(list2[i]): return -1
        return 0
