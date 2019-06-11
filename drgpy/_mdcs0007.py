
def mdcs00(x):

    y = []

    # 001 - 002
    if (x["001&002|HEART TRANSPLANT ORPCS"] +
        x["001&002|IMPLANT OF HEART ASSIST SYSTEM"] > 0):
        if x["_MCC"] > 0:
            y.append("001")
        else:
            y.append("002")

    # 003 - 004
    # NOTE for interpreting 003 and 004
    # c1: TRACHEOSTOMY WITH 
    # c2:    (MV >96 HOURS OR PDX EXCEPT FACE, MOUTH AND NECK)
    # c3:     WITH/WITHOUT MAJOR O.R. PROCEDURE
    c1 = (x["003&004|TRACHEOSTOMY ORPCS"] + x["003&004|OR NON-ORPCS"])
    c2 = (x["003&004|MECHANICAL VENTILATION >96 HOURS NON-ORPCS"] + 
            int(x["011&012&013|PDX"] == 0))
    c3 = (x["_ORPCS"] > x["_UNRELATED_ORPCS"]) 
    if x["003&004|ECMO ORPCS"] > 0:
        y.append("003")
    elif c1 * c2 > 0:
        if c3 > 0:
            y.append("003")
        else:
            y.append("004")

    # 005- 006
    if (x["005&006|LIVER TRANSPLANT ORPCS"]*x["_MCC"] +
        x["005&006|INTESTINAL TRANSPLANT ORPCS"]) > 0:
        y.append("005")
    elif x["005&006|LIVER TRANSPLANT ORPCS"] > 0:
        y.append("006")

    # 014
    if x["014|NON-ORPCS"] > 0:
        y.append("014")

    # 007
    if x["007|ORPCS"] > 0:
        y.append("007")

    # 008
    if x["008|ORPCS"] * x["008|PSDX"] * x["008|AND PSDX"] > 0:
        y.append("008")

    # 016 - 017
    if x["016&017|T-CELL IMMUNOTHERAPY NON-ORPCS"] > 0:
        y.append("016")
    elif x["016&017|BONE MARROW TRANSPLANT NON-ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("016")
        else:
            y.append("017")

    # 010
    if x["010|ORPCS"] * x["010|PSDX"] > 0:
        y.append("010")

    # 011 - 013
    s1 = ("011&012&013|AND TRACHEOSTOMY " + 
        "FOR FACE,MOUTH & NECK DIAGNOSIS ORPCS")
    if (x["011&012&013|PDX"] * (x[s1] + x["011&012&013|OR NON-ORPCS"]) + 
        x["011&012&013|LARYNGECTOMY ORPCS"]) > 0:
        if x["_MCC"] > 0:
            y.append("011")
        elif x["_CC"] > 0:
            y.append("012")
        else:
            y.append("013")

    return y

def mdcs01(x):
    y = []
    if x["_MDC01"] == 0:
        return y

    # 020 - 022
    if (x["020&021&022|INTRACRANIAL VASCULAR PROCEDURE ORPCS"] * 
            x["020&021&022|HEMORRHAGE PDX"] > 0):
        if x["_MCC"] > 0:
            y.append("020")
        elif x["_CC"] > 0:
            y.append("021")
        else:
            y.append("022")

    # 023 - 024
    c1 = ((x["023&024|CRANIOTOMY ORPCS"] * 
            x["023&024|MAJOR DEVICE IMPLANT"]) + 
            x["023&024|ACUTE COMPLEX CNS PDX"])
    c2 = x["023&024|CHEMOTHERAPY IMPLANT NON-ORPCS"]
    c3 = x["023&024|EPILEPSY PDX"] * x["023&024|NEUROSTIMULATOR"]
    if c1*x["_MCC"] + c2 + c3 > 0:
        y.append("023")
    elif c1 > 0:
        y.append("024")

    # 025 - 027
    if x["025&026&027|CRANIOTOMY ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("025")
        elif x["_CC"] > 0:
            y.append("026")
        else:
            y.append("027")

    # 028 - 030
    if x["028&029&030|SPINAL PROCEDURE ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("028")
        elif x["_CC"] > 0:
            y.append("029")
        elif x["028&029&030|SPINAL NEUROSTIMULATORS"] > 0:
            y.append("029")
        else:
            y.append("030")

    # 031 - 033
    if x["031&032&033|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("031")
        elif x["_CC"] > 0:
            y.append("032")
        else:
            y.append("033")

    # 034 - 036
    if ((x["034&035&036|ORPCS"] + 
        (x["034&035&036|OR ORPCS"] * x["034&035&036|WITH ORPCS"])) > 0):
        if x["_MCC"] > 0:
            y.append("034")
        elif x["_CC"] > 0:
            y.append("035")
        else:
            y.append("036")

    # 037 - 039
    if x["037&038&039|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("037")
        elif x["_CC"] > 0:
            y.append("038")
        else:
            y.append("039")
    
    # 040 - 042
    s1 = ("040&041&042|PERIPHERAL / CRANIAL NERVE & " + 
            "OTHER NERVOUS SYSTEM PROCEDURE ORPCS")
    if x[s1] + x["040&041&042|NON-ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("040")
        elif x["_CC"] > 0:
            y.append("041")
        elif x["040&041&042|PERIPHERAL NEUROSTIMULATORS"] > 0:
            y.append("041")
        else:
            y.append("042")

    # 052 - 053
    if x["052&053|PDX"] > 0:
        if x["_MCC"] + x["_CC"] > 0:
            y.append("052")
        else:
            y.append("053")

    # 054 - 055
    if x["054&055|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("054")
        else:
            y.append("055")

    # 056 - 057
    if x["056&057|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("056")
        else:
            y.append("057")

    # 058 - 060
    if x["058&059&060|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("058")
        elif x["_CC"] > 0:
            y.append("059")
        else:
            y.append("060")

    # 061 - 063
    if x["061&062&063|PDX"] * x["061&062&063|NON-ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("061")
        elif x["_CC"] > 0:
            y.append("062")
        else:
            y.append("063")


    # 064 - 066
    if x["064&065&066|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("064")
        elif x["_CC"] > 0:
            y.append("065")
        elif x["064&065&066|tPA within 24 hours Secondary diagnosis"] > 0:
            y.append("065")
        else:
            y.append("066")

    # 067 - 068
    if x["061&062&063|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("067")
        else:
            y.append("068")

    # 069
    if x["069|PDX"] > 0:
        y.append("069")

    # 070 - 072
    if x["070&071&072|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("070")
        elif x["_MCC"] > 0:
            y.append("071")
        else:
            y.append("072")
    
    # 073 - 074
    if x["073&074|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("073")
        else:
            y.append("074")

    # 075 - 076
    if x["075&076|PDX"] > 0:
        if x["_MCC"] + x["_CC"] > 0:
            y.append("075")
        else:
            y.append("076")

    # 077 - 079
    if x["077&078&079|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("077")
        elif x["_CC"] > 0:
            y.append("078")
        else:
            y.append("079")

    # 080 - 081
    if x["080&081|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("080")
        else:
            y.append("081")

    # 082 - 084
    if ((x["082&083&084|PDX"] + 
        (x["082&083&084|OR PDX"] * x["082&083&084|AND SDX"])) > 0):
        if x["_MCC"] > 0:
            y.append("082")
        elif x["_CC"] > 0:
            y.append("083")
        else:
            y.append("084")
       
    # 085 - 087
    if x["085&086&087|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("085")
        elif x["_CC"] > 0:
            y.append("086")
        else:
            y.append("087")

    # 088 - 090
    if x["088&089&090|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("088")
        elif x["_CC"] > 0:
            y.append("089")
        else:
            y.append("090")
           
    # 091 - 093
    if x["091&092&093|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("091")
        elif x["_CC"] > 0:
            y.append("092")
        else:
            y.append("093")

    # 094 - 096
    if x["094&095&096|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("094")
        elif x["_CC"] > 0:
            y.append("095")
        else:
            y.append("096")

    # 097 - 099
    if x["097&098&099|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("097")
        elif x["_CC"] > 0:
            y.append("098")
        else:
            y.append("099")

    # 100 - 101
    if x["100&101|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("100")
        else:
            y.append("101")

    # 102 - 103
    if x["102&103|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("102")
        else:
            y.append("103")

    return y

def mdcs02(x):
    y = []
    
    if x["_MDC02"] == 0:
        return y

    # 113 - 114
    if x["113&114|ORPCS"] > 0:
        if x["_MCC"] + x["_CC"] > 0:
            y.append("113")
        else:
            y.append("114")

    # 115
    if x["115|ORPCS"] > 0:
        y.append("115")

    # 116 - 117
    if x["116&117|ORPCS"] > 0:
        if x["_MCC"] + x["_CC"] > 0:
            y.append("116")
        else:
            y.append("117")

    # 121 - 122
    if x["121&122|PDX"] > 0:
        if x["_MCC"] + x["_CC"] > 0:
            y.append("121")
        else:
            y.append("122")

    # 123
    if x["123|PDX"] > 0:
        y.append("123")

    # 124 - 125
    if x["124&125|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("124")
        else:
            y.append("125")

    return y

def mdcs03(x):
    y = []
    if x["_MDC03"] == 0:
        return y

    # 129 - 130
    if x["129&130|HEAD AND NECK PROCEDURE ORPCS"] > 0:
        if (x["_MCC"] + x["_CC"] + 
                x["129&130|MAJOR DEVICE IMPLANT ORPCS"] > 0):
            y.append("129")
        else:
            y.append("130")
       
    # 131 - 132
    if x["131&132|ORPCS"] > 0:
        if x["_MCC"] + x["_CC"] > 0:
            y.append("131")
        else:
            y.append("132")

    # 133 - 134
    if x["133&134|ORPCS"] > 0:
        if x["_MCC"] + x["_CC"] > 0:
            y.append("133")
        else:
            y.append("134")

    # 135 - 136
    if x["135&136|ORPCS"] > 0:
        if x["_MCC"] + x["_CC"] > 0:
            y.append("135")
        else:
            y.append("136")

    # 137 - 138
    if x["137&138|ORPCS"] > 0:
        if x["_MCC"] + x["_CC"] > 0:
            y.append("137")
        else:
            y.append("138")

    # 139
    if x["139|ORPCS"] > 0:
        y.append("139")

    # 146 - 148
    if x["146&147&148|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("146")
        elif x["_CC"] > 0:
            y.append("147")
        else:
            y.append("148")

    # 149
    if x["149|PDX"] > 0:
        y.append("149")

    # 150 - 151
    if x["150&151|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("150")
        else:
            y.append("151")

    # 152 - 153
    if x["152&153|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("152")
        else:
            y.append("153")
    
    # 154 - 156
    if x["154&155&156|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("154")
        elif x["_CC"] > 0:
            y.append("155")
        else:
            y.append("156")

    # 157 - 159
    if x["157&158&159|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("157")
        elif x["_CC"] > 0:
            y.append("158")
        else:
            y.append("159")

    return y

def mdcs04(x):

    y = []
    if x["_MDC04"] == 0:
        return y

    # 163 - 165
    if x["163&164&165|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("163")
        elif x["_CC"] > 0:
            y.append("164")
        else:
            y.append("165")

    # 166 - 168
    if x["166&167&168|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("166")
        elif x["_CC"] > 0:
            y.append("167")
        else:
            y.append("168")

    # 207 - 208
    if (x["207&208|ANY PDX IN MDC 4 ECMO NON-ORPCS"] +
        x["207&208|MECHANICAL VENTILATION >96 HOURS NON-ORPCS"] > 0):
        y.append("207")   
    elif x["207&208|MECHANICAL VENTILATION <96 HOURS NON-ORPCS"] > 0:
        y.append("208")

    # 175 - 176
    if x["175&176|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("175")
        else:
            y.append("176")
    
    # 177 - 179
    if (x["177&178&179|PDX"] * x["793|OR SDX"] + 
            x["177&178&179|or PDX"] > 0):
        if x["_MCC"] > 0:
            y.append("177")
        elif x["_CC"] > 0:
            y.append("178")
        else:
            y.append("179")

    # 180 - 182
    if x["180&181&182|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("180")
        elif x["_CC"] > 0:
            y.append("181")
        else:
            y.append("182")

    # 183 - 185
    if x["183&184&185|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("183")
        elif x["_CC"] > 0:
            y.append("184")
        else:
            y.append("185")

    # 186 - 188
    if x["186&187&188|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("186")
        elif x["_CC"] > 0:
            y.append("187")
        else:
            y.append("188")

    # 189
    if x["189|PDX"] > 0:
        y.append("189")

    # 190 - 192
    if x["190&191&192|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("190")
        elif x["_CC"] > 0:
            y.append("191")
        else:
            y.append("192")

    # 193 - 195
    if x["193&194&195|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("193")
        elif x["_CC"] > 0:
            y.append("194")
        else:
            y.append("195")

    # 196 - 198
    if x["196&197&198|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("196")
        elif x["_CC"] > 0:
            y.append("197")
        else:
            y.append("198")

    # 199 - 201
    if x["199&200&201|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("199")
        elif x["_CC"] > 0:
            y.append("200")
        else:
            y.append("201")

    # 202 - 203
    if x["202&203|PDX"] > 0:
        if x["_MCC"] + x["_CC"] > 0:
            y.append("202")
        else:
            y.append("203")

    # 204
    if x["204|PDX"] > 0:
        y.append("204")

    # 205 - 206
    if x["205&206|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("205")
        else:
            y.append("206")

    return y


