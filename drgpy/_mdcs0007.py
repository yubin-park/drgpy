
def mdc00(x):

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
    c3 = (x["_ORPCS*"] > 0) 
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

def mdc01(x):
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
        elif x["064&065&066|TPA WITHIN 24 HOURS SDX"] > 0:
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

def mdc02(x):
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

def mdc03(x):
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

def mdc04(x):

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
    if (x[("207&208|ANY PDX IN MDC 4 "
        +"MECHANICAL VENTILATION >96 HOURS NON-ORPCS")] > 0):
        y.append("207")   
    elif x["207&208|MECHANICAL VENTILATION <96 HOURS NON-ORPCS"] > 0:
        y.append("208")

    # 175 - 176
    if x["175&176|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("175")
        else:
            y.append("176")
    if x["175&176|ACUTE COR PULMONALE PSDX"] + x["175&176|ACUTE COR PULMONALE"] > 0:
        y.append("175")   


    # 177 - 179
    if (x["177&178&179|PDX"] * x["793|OR SDX"] + 
            x["177&178&179|OR PDX"] > 0):
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

def mdc05(x):
    y = []
    if x["_MDC05"] == 0:
        return y

    # 215
    if x["215|ORPCS"] > 0:
        y.append("215")

    # 216 - 221
    s1 = ("216&217&218&219&220&221|CARDIAC VALVE AND " + 
            "OTHER MAJOR CARDIOTHORACIC PROCEDURE ORPCS")
    s2 = "216&217&218&219&220&221|CARDIAC CATHETERIZATION NON-ORPCS"
    if x[s1] > 0:
        if x[s2] > 0:
            if x["_MCC"] > 0:
                y.append("216")
            elif x["_CC"] > 0:
                y.append("217")
            else:
                y.append("218")
        else:
            if x["_MCC"] > 0:
                y.append("219")
            elif x["_CC"] > 0:
                y.append("220")
            else:
                y.append("221")
    
    # 266 - 267
    if x["266&267|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("266")
        else:
            y.append("267")

    # 222 - 227
    s1 = "222&223&224&225&226&227|CARDIAC DEFIBRILLATOR IMPLANT ORPCS"
    s2 = "222&223&224&225&226&227|CARDIAC CATHETERIZATION NON-ORPCS"
    s3 = "222&223&224&225&226&227|AMI / HF / SHOCK PDX"
    s3v40 = "222&223&224&225&226&227|PDX AMI / HF / SHOCK"
    if x[s1] > 0:
        if x[s2] > 0:
            if x[s3] + x[s3v40] > 0:
                if x["_MCC"] > 0:
                    y.append("222")
                else:
                    y.append("223")
            else:
                if x["_MCC"] > 0:
                    y.append("224")
                else:
                    y.append("225")
        else:
            if x["_MCC"] > 0:
                y.append("226")
            else:
                y.append("227")

    # 228 - 229
    if x["228&229|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("228")
        elif x["_CC"] > 0:
            y.append("229")

    # 231 - 236
    s1 = "231&232&233&234&235&236|CORONARY BYPASS ORPCS"
    s2 = "231&232&233&234&235&236|PTCA ORPCS"
    s3 = "216&217&218&219&220&221|CARDIAC CATHETERIZATION NON-ORPCS"
    if x[s1] > 0:
        if x[s2] > 0:
            if x["_MCC"] > 0:
                y.append("231")
            else:
                y.append("232")
        elif x[s3] > 0:
            if x["_MCC"] > 0:
                y.append("233")
            else:
                y.append("234")
        else:
            if x["_MCC"] > 0:
                y.append("235")
            else:
                y.append("236")

    # 268 - 269
    if x["268&269|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("268")
        else:
            y.append("269")

    # 270 - 272
    if x["270&271&272|MAJOR CARDIOVASCULAR PROCEDURE ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("270")
        elif x["_CC"] > 0:
            y.append("271")
        else:
            y.append("272")

    # 239 - 241
    if x["239&240&241|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("239")
        elif x["_CC"] > 0:
            y.append("240")
        else:
            y.append("241")

    # 242 - 244
    if x["242&243&244|CARDIAC PACEMAKER DEVICE"] > 0:
        if x["_MCC"] > 0:
            y.append("242")
        elif x["_CC"] > 0:
            y.append("243")
        else:
            y.append("244")

    # 245
    if x["245|ORPCS"] > 0:
        y.append("245")

    # 265 
    if x["265|ORPCS"] > 0:
        y.append("265")

    # 273 - 274
    if x["273&274|ORPCS"] + x["273&274|OR NON-ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("273")
        else:
            y.append("274")

    # 246 - 249
    # NOTE: v38+, two sets of DRGs (246, 247) and (248, 249)
    # This section applies to v36, v37
    s1 = "246&247&248&249|PERCUTANEOUS CARDIOVASCULAR PROCEDURE ORPCS"
    s2 = "246&247&248&249|OR NON-ORPCS"
    s3 = "246&247&248&249|DRUG-ELUTING STENT"
    s4 = "246&247&248&249|NON-DRUG-ELUTING STENT"
    s5 = "246&247&248&249|ONE STENT"
    s6 = "246&247&248&249|TWO STENTS"
    s7 = "246&247&248&249|THREE STENTS"
    s8 = "246&247&248&249|FOUR OR MORE STENTS"
    s9 = "246&247&248&249|ONE ARTERY"
    s10 = "246&247&248&249|TWO ARTERIES"
    s11 = "246&247&248&249|THREE ARTERIES"
    s12 = "246&247&248&249|FOUR OR MORE ARTERIES"
    base_cnt = x[s1] + x[s2]
    drug_eluting_stent = x[s3]
    non_drug_eluting_stent = x[s4]
    stent_cnt = (x[s5] + 2 * x[s6] + 3 * x[s7] + 4 * x[s8])
    artery_cnt = (x[s9] + 2 * x[s10] + 3 * x[s11] + 4 * x[s12])
    
    
    # This section applies to v38+
    s1 = '246&247|PERCUTANEOUS CARDIOVASCULAR PROCEDURE WITHOUT STENT ORPCS'
    s2 = '246&247|OR NON-ORPCS'
    s3 = '246&247|DRUG-ELUTING STENT'
    s5 = '246&247|ONE STENT'
    s6 = '246&247|TWO STENTS'
    s7 = '246&247|THREE STENTS'
    s8 = '246&247|FOUR OR MORE STENTS'
    s9 = '246&247|ONE ARTERY'
    s10 = '246&247|TWO ARTERIES'
    s11 = '246&247|THREE ARTERIES'
    s12 = '246&247|FOUR OR MORE ARTERIES'
    base_cnt += (x[s1] + x[s2])
    drug_eluting_stent += x[s3]
    non_drug_eluting_stent += x[s4]
    stent_cnt += (x[s5] + 2 * x[s6] + 3 * x[s7] + 4 * x[s8])
    artery_cnt += (x[s9] + 2 * x[s10] + 3 * x[s11] + 4 * x[s12])

    s1 = '248&249|PERCUTANEOUS CARDIOVASCULAR PROCEDURE WITHOUT STENT ORPCS'
    s2 = '248&249|OR NON-ORPCS'
    s4 = '248&249|NON-DRUG-ELUTING STENT'
    s5 = '248&249|ONE STENT'
    s6 = '248&249|TWO STENTS'
    s7 = '248&249|THREE STENTS'
    s8 = '248&249|FOUR OR MORE STENTS'
    s9 = '248&249|ONE ARTERY'
    s10 = '248&249|TWO ARTERIES'
    s11 = '248&249|THREE ARTERIES'
    s12 = '248&249|FOUR OR MORE ARTERIES'
    base_cnt += (x[s1] + x[s2])
    drug_eluting_stent += x[s3]
    non_drug_eluting_stent += x[s4]
    # stent and artery counts should not need to add up
    #stent_cnt += (x[s5] + 2 * x[s6] + 3 * x[s7] + 4 * x[s8])
    #artery_cnt += (x[s9] + 2 * x[s10] + 3 * x[s11] + 4 * x[s12])

    if base_cnt > 0:
        if drug_eluting_stent > 0:
            if (x["_MCC"] > 0 or stent_cnt > 3 or artery_cnt > 3):
                y.append("246")
            else:
                y.append("247")
        elif non_drug_eluting_stent > 0:
            if (x["_MCC"] > 0 or stent_cnt > 3 or artery_cnt > 3):
                y.append("248")
            else:
                y.append("249")
       
    # 250 - 251
    if x["250&251|ORPCS"] + x["250&251|OR NON-ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("250")
        else:
            y.append("251")

    if x["252&253&254|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("252")
        elif x["_CC"] > 0:
            y.append("253")
        else:
            y.append("254")

    if x["255&256&257|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("255")
        elif x["_CC"] > 0:
            y.append("256")
        else:
            y.append("257")

    if x["258&259|NON ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("258")
        else:
            y.append("259")

    if x["260&261&262|ORPCS"] + x["260&261&262|OR NON ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("260")
        elif x["_CC"] > 0:
            y.append("261")
        else:
            y.append("262")

    if x["263|ORPCS"] > 0:
        y.append("263")

    if x["264|ORPCS"] > 0:
        y.append("264")

    # 280 - 285
    if x["280&281&282&283&284&285|PDX OR SDX"] > 0:
        if x["_ALIVE"] > 0: 
            if x["_MCC"] > 0:
                y.append("280")
            elif x["_CC"] > 0:
                y.append("281")
            else:
                y.append("282")
        else:
            if x["_MCC"] > 0:
                y.append("283")
            elif x["_CC"] > 0:
                y.append("284")
            else:
                y.append("285")

    if x["286&287|NON-ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("286")
        else:
            y.append("287")

    if x["288&289&290|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("288")
        elif x["_CC"] > 0:
            y.append("289")
        else:
            y.append("290")

    if x["291&292&293|PDX"] > 0:
        if x["291&292&293|ECMO NON-ORPCS"] + x["_MCC"] > 0:
            y.append("291")
        elif x["_CC"] > 0:
            y.append("292")
        else:
            y.append("293")

    if x["294&295|PDX"] > 0:
        if x["_MCC"] + x["_CC"] > 0:
            y.append("294")
        else:
            y.append("295")

    # 296 - 298
    if x["296&297&298|PDX"] > 0:
        if x["296&297&298|ECMO NON-ORPCS"] + x["_MCC"] > 0:
            y.append("296")
        elif x["_CC"] > 0:
            y.append("297")
        else:
            y.append("298")

    if x["299&300&301|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("299")
        elif x["_CC"] > 0:
            y.append("300")
        else:
            y.append("301")

    # 302 - 303
    if x["302&303|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("302")
        else:
            y.append("303")

    if x["304&305|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("304")
        else:
            y.append("305")

    if x["306&307|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("306")
        else:
            y.append("307")

    if x["308&309&310|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("308")
        elif x["_CC"] > 0:
            y.append("309")
        else:
            y.append("310")

    if x["311|PDX"] > 0:
        y.append("311")

    if x["312|PDX"] > 0:
        y.append("312")

    if x["313|PDX"] > 0:
        y.append("313")
    
    # 314 - 316
    if x["314&315&316|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("314")
        elif x["_CC"] > 0:
            y.append("315")
        else:
            y.append("316")
            
    return y

def mdc06(x):

    y = []
    if x["_MDC06"] == 0:
        return y

    if x["326&327&328|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("326")
        elif x["_CC"] > 0:
            y.append("327")
        else:
            y.append("328")
    
    if x["329&330&331|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("329")
        elif x["_CC"] > 0:
            y.append("330")
        else:
            y.append("331")

    if x["332&333&334|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("332")
        elif x["_CC"] > 0:
            y.append("333")
        else:
            y.append("334")
    
    if x["335&336&337|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("335")
        elif x["_CC"] > 0:
            y.append("336")
        else:
            y.append("337")
        
    if x["338&339&340&341&342&343|APPENDECTOMY ORPCS"] > 0:
        if x["338&339&340&341&342&343|COMPLICATED PDX PDX"] > 0:
            if x["_MCC"] > 0:
                y.append("338")
            elif x["_CC"] > 0:
                y.append("339")
            else:
                y.append("340")
        else:
            if x["_MCC"] > 0:
                y.append("341")
            elif x["_CC"] > 0:
                y.append("342")
            else:
                y.append("343")

    if x["344&345&346|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("344")
        elif x["_CC"] > 0:
            y.append("345")
        else:
            y.append("346")

    if x["347&348&349|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("347")
        elif x["_CC"] > 0:
            y.append("348")
        else:
            y.append("349")

    s1 = ("350&351&352&353&354&355|INGUINAL AND " + 
            "FEMORAL HERNIA PROCEDURE ORPCS")
    s2 = ("350&351&352&353&354&355|HERNIA PROCEDURE EXCEPT " + 
            "INGUINAL AND FEMORAL ORPCS")
    if x[s1] > 0:
        if x["_MCC"] > 0:
            y.append("350")
        elif x["_CC"] > 0:
            y.append("351")
        else:
            y.append("352")
    elif x[s2] > 0:
        if x["_MCC"] > 0:
            y.append("353")
        elif x["_CC"] > 0:
            y.append("354")
        else:
            y.append("355")

    if x["356&357&358|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("356")
        elif x["_CC"] > 0:
            y.append("357")
        else:
            y.append("358")

    if x["368&369&370|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("368")
        elif x["_CC"] > 0:
            y.append("369")
        else:
            y.append("370")

    if x["371&372&373|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("371")
        elif x["_CC"] > 0:
            y.append("372")
        else:
            y.append("373")

    if x["374&375&376|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("374")
        elif x["_CC"] > 0:
            y.append("375")
        else:
            y.append("376")

    if x["377&378&379|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("377")
        elif x["_CC"] > 0:
            y.append("378")
        else:
            y.append("379")

    if x["380&381&382&383&384|COMPLICATED PEPTIC ULCER PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("380")
        elif x["_CC"] > 0:
            y.append("381")
        else:
            y.append("382")
    elif x["380&381&382&383&384|UNCOMPLICATED PEPTIC ULCER PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("383")
        else:
            y.append("384")

    if x["385&386&387|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("385")
        elif x["_CC"] > 0:
            y.append("386")
        else:
            y.append("387")
 
    if x["388&389&390|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("388")
        elif x["_CC"] > 0:
            y.append("389")
        else:
            y.append("390")
 
    if x["391&392|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("391")
        else:
            y.append("392")

    if x["393&394&395|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("393")
        elif x["_CC"] > 0:
            y.append("394")
        else:
            y.append("395")

    return y

def mdc07(x):

    y = []
    if x["_MDC07"] == 0:
        return y

    if x["405&406&407|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("405")
        elif x["_CC"] > 0:
            y.append("406")
        else:
            y.append("407")

    if x["408&409&410|ORPCS"] + x["408&409&410|OR ORPCS"] > 0:
        if x["408&409&410|WITHOUT ORPCS"] == 0:
            if x["_MCC"] > 0:
                y.append("408")
            elif x["_CC"] > 0:
                y.append("409")
            else:
                y.append("410")

    s1 = "411&412&413&414&415&416&417&418&419|ORPCS" 
    s2 = "411&412&413&414&415&416&417&418&419|C.D.E. ORPCS"
    s3 = ("411&412&413&414&415&416&417&418&419|CHOLECYSTECTOMY EXCEPT " + 
            "BY LAPAROSCOPE ORPCS")
    s4 = ("411&412&413&414&415&416&417&418&419|LAPAROSCOPIC " + 
            "CHOLECYSTECTOMY ORPCS")
    if x[s1] > 0:
        if x[s2] > 0:
            if x["_MCC"] > 0:
                y.append("411")
            elif x["_CC"] > 0:
                y.append("412")
            else:
                y.append("413")
        elif x[s3] > 0:
            if x["_MCC"] > 0:
                y.append("414")
            elif x["_CC"] > 0:
                y.append("415")
            else:
                y.append("416")
        elif x[s4] > 0:
            if x["_MCC"] > 0:
                y.append("417")
            elif x["_CC"] > 0:
                y.append("418")
            else:
                y.append("419")

    if x["420&421&422|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("420")
        elif x["_CC"] > 0:
            y.append("421")
        else:
            y.append("422")

    if x["423&424&425|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("423")
        elif x["_CC"] > 0:
            y.append("424")
        else:
            y.append("425")

    if x["432&433&434|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("432")
        elif x["_CC"] > 0:
            y.append("433")
        else:
            y.append("434")

    if x["435&436&437|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("435")
        elif x["_CC"] > 0:
            y.append("436")
        else:
            y.append("437")

    if x["438&439&440|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("438")
        elif x["_CC"] > 0:
            y.append("439")
        else:
            y.append("440")

    if x["441&442&443|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("441")
        elif x["_CC"] > 0:
            y.append("442")
        else:
            y.append("443")

    if x["444&445&446|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("444")
        elif x["_CC"] > 0:
            y.append("445")
        else:
            y.append("446")

    return y



