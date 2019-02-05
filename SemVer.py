import re

#class denoting a Python semantic versioning module
#available attributes- major, minor, patch, pre_release, metadata
#available functions- parseVersion, str(version), compare(input)
class SemVer:

    #SemVer datatype constructor
    def __init__(self,version):
        if str(version).strip() == "": return
        parsedVersion = self.parseVersion(version)
        if parsedVersion == 'invalid':
            print('invalid')
            return
        self.major = parsedVersion[0]
        self.minor = parsedVersion[1]
        self.patch = parsedVersion[2]
        self.pre_release = ""
        self.metadata = ""
        if parsedVersion[3]:
            self.pre_release = parsedVersion[3][1:]
        if parsedVersion[4]:
            self.metadata = parsedVersion[4][1:]

    #function to check if valid sem version
    def parseVersion(self,version):
        semVerRegex = re.compile('^(\d+)\.(\d+)\.(\d+)(-[0-9A-Za-z]+(?:\.[a-zA-Z0-9]+)*)?(\+[0-9A-Za-z]+(?:\.[a-zA-Z0-9]+)*)?$')
        validMatch = semVerRegex.match(str(version))
        if not validMatch:
            return 'invalid'
        else:
            if validMatch.groups()[0] == '0':
                return 'invalid'
            return validMatch.groups()

    #overriden string operator- convert datatype to string
    def __str__(self):
        resultStr = ''
        versionArray = [self.major,self.minor,self.patch]
        resultStr += '.'.join(str(component) for component in versionArray)
        if self.pre_release:
            resultStr += '-' + self.pre_release
        if self.metadata:
            resultStr += '+' + self.metadata

        return resultStr

    #compare sample SemVer input
    def compare(self,input):
        if str(input).strip() == "": return
        input = re.sub(' +', ' ',str(input))
        input = input.strip()
        version1 = ""
        version2 = ""
        index = 0
        char = input[0]

        #build string for first version
        while char != " " and index < len(input):
            version1 += char
            index += 1
            if index < len(input):
                char = input[index]

        if index == len(input):
            print('invalid')
            return 'invalid'

        index += 1
        char = input[index]

        #if above was valid, build string for second version
        while char != " " and index < len(input):
            version2 += char
            index += 1
            if index < len(input):
                char = input[index]

        if index < len(input):
            print('invalid')
            return 'invalid'

        version1Result = self.parseVersion(version1)
        version2Result = self.parseVersion(version2)

        if version1Result == 'invalid' or version2Result == 'invalid':
            print('invalid')
            return 'invalid'

        version1Result = version1Result[:-1]
        version2Result = version2Result[:-1]
        equalVersions = True

        #version precedence check
        for index,component1 in enumerate(version1Result):
            if component1 is None or version2Result[index] is None:
                continue
            component1 = component1.replace('.','')
            component2 = version2Result[index].replace('.','')
            if index < 3:
                if int(component1) > int(component2):
                    equalVersions = False
                    print('before')
                    return 'before'
                elif int(component1) < int(component2):
                    equalVersions = False
                    print('after')
                    return 'after'
            else:
                if component1 > component2:
                    equalVersions = False
                    print('before')
                    return 'before'
                elif component1 < component2:
                    equalVersions = False
                    print('after')
                    return 'after'

        if equalVersions:
            print('equal')
            return 'equal'
