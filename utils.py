def lengthOfCallToSeconds(lengthOfCall):
    values = str(lengthOfCall).split(":")
    if (len(values) > 1) :
        values1= values[1].split(".")
        return int(values[0])*10000+int(values1[0])*1000+int(values1[1])*100
    return 0;

def getM104Value(identification, group, member):
    return _getM104(identification, group, member, 0)

def getM104Value1(identification, group, member):
    return _getM104(identification, group, member, 1)

def _getM104(identification, group, member, indexColumn):
    if (len(str(identification).split(",")) > indexColumn):
        return str(identification).split(",")[indexColumn] + ":" + str(group).split(",")[indexColumn] + ":" + str(member).split(",")[indexColumn]
    return ""
