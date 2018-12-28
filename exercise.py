import pandas as pd
import utils

inputData = pd.read_csv("entrada.csv", "|")

outputColumns = "ANI / CPN indicator|Call type|Carrier connect date|Carrier connect time|Carrier elapsed time|Date|Dialing and presubscription indicator|IC / INC Routing Indicator|IC / INC indicator|IC/INC call event status|Operator action|Overseas indicator|Recording Office_ID|Recording Office_Type|Sensor_ID|Sensor_Type|Service feature code|Service observed / Traffic sampled|Study indicator|Time|Timing indicator|type|Trunk Group Number|m104.trunkid|m104.trunkid1|m119.trunkgroupinfo|originatingnpa|originatingnumber|terminatingnpa|terminatingnumber|elapsedtime|structurecode".split("|")
outputData = pd.DataFrame(columns=outputColumns)

type_lookup = {5:"Local message rate call",90:"other",110:"Interlata call",119:"Incoming CDR"}
outputData["type"] = inputData["Call type"].apply(lambda x: type_lookup[x])

outputData["m104.trunkid"] = inputData.apply(lambda row: utils.getM104Value(row["Trunk Identification_Routing Indicator"], row["Trunk Identification_Trunk Group Number"], row["Trunk Identification_Trunk Member Number"]), axis=1)
outputData["m104.trunkid1"] = inputData.apply(lambda row: utils.getM104Value1(row["Trunk Identification_Routing Indicator"], row["Trunk Identification_Trunk Group Number"], row["Trunk Identification_Trunk Member Number"]), axis=1)

outputData["m119.trunkgroupinfo"] = inputData["Trunk Group_Trunk Group Number - Interoffice"]

outputData["originatingnpa"] = inputData["Calling number"].apply(lambda number: str(number)[:3])
outputData["originatingnumber"] = inputData["Calling number"].apply(lambda number: str(number)[4:])
outputData["terminatingnpa"] = inputData["Called number"].apply(lambda number: str(number)[:3])
outputData["terminatingnumber"] = inputData["Called number"].apply(lambda number: str(number)[4:])

outputData["elapsedtime"] = inputData["Length of call"].apply(lambda lengthOfCall: utils.lengthOfCallToSeconds(lengthOfCall))
outputData["structurecode"] = inputData["Structure type"].apply(lambda x:"Modules Attached : " + str(x))

for outputColumn in outputColumns:
    if not(outputColumn in {'type', 'm104.trunkid', 'm104.trunkid1', 'm119.trunkgroupinfo', 'originatingnpa', 'originatingnumber', 'terminatingnpa', 'terminatingnumber', 'elapsedtime', 'structurecode'}):
        outputData[outputColumn] = inputData[outputColumn]

outputData.to_csv("salida.csv","|", index=False)

