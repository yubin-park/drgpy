
def mdcs00(x):

    y = []

    # 001 - 002
    if (x["001&002|HEART TRANSPLANT ORPCS"] +
        x["001&002|IMPLANT OF HEART ASSIST SYSTEM"] > 0):
        if x["MCC"] > 0:
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
    c3 = (x["ORPCS"] > x["UNRELATED ORPCS"]) 
    if x["003&004|ECMO ORPCS"] > 0:
        y.append("003")
    elif c1 * c2 > 0:
        if c3 > 0:
            y.append("003")
        else:
            y.append("004")

    # 005- 006
    if (x["005&006|LIVER TRANSPLANT ORPCS"]*x["MCC"] +
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
        if x["MCC"] > 0:
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
        if x["MCC"] > 0:
            y.append("011")
        elif x["CC"] > 0:
            y.append("012")
        else:
            y.append("013")

    return y

def mdcs01(x):
    y = []
    if "MDC01" not in x:
        return y

    # 020 - 022
    if (x["020&021&022|INTRACRANIAL VASCULAR PROCEDURE ORPCS"] * 
            x["020&021&022|HEMORRHAGE PDX"] > 0):
        if x["MCC"] > 0:
            y.append("020")
        elif x["CC"] > 0:
            y.append("021")
        else:
            y.append("022")

    # 023 - 024
    c1 = ((x["023&024|CRANIOTOMY ORPCS"] * 
            x["023&024|MAJOR DEVICE IMPLANT"]) + 
            x["023&024|ACUTE COMPLEX CNS PDX"])
    c2 = x["023&024|CHEMOTHERAPY IMPLANT NON-ORPCS"]
    c3 = x["023&024|EPILEPSY PDX"] * x["023&024|NEUROSTIMULATOR"]
    if c1*x["MCC"] + c2 + c3 > 0:
        y.append("023")
    elif c1 > 0:
        y.append("024")

    # 025 - 027
    if x["025&026&027|CRANIOTOMY ORPCS"] > 0:
        if x["MCC"] > 0:
            y.append("025")
        elif x["CC"] > 0:
            y.append("026")
        else:
            y.append("027")

    # 028 - 030
    if x["028&029&030|SPINAL PROCEDURE ORPCS"] > 0:
        if x["MCC"] > 0:
            y.append("028")
        elif x["CC"] > 0:
            y.append("029")
        elif x["028&029&030|SPINAL NEUROSTIMULATORS"] > 0:
            y.append("029")
        else:
            y.append("030")

    # 031 - 033
    if x["031&032&033|ORPCS"] > 0:
        if x["MCC"] > 0:
            y.append("031")
        elif x["CC"] > 0:
            y.append("032")
        else:
            y.append("033")

    # 034 - 036
    if ((x["034&035&036|ORPCS"] + 
        (x["034&035&036|OR ORPCS"] * x["034&035&036|WITH ORPCS"])) > 0):
        if x["MCC"] > 0:
            y.append("034")
        elif x["CC"] > 0:
            y.append("035")
        else:
            y.append("036")

    # 037 - 039
    if x["037&038&039|ORPCS"] > 0:
        if x["MCC"] > 0:
            y.append("037")
        elif x["CC"] > 0:
            y.append("038")
        else:
            y.append("039")
    
    # 040 - 042
    s1 = ("040&041&042|PERIPHERAL / CRANIAL NERVE & " + 
            "OTHER NERVOUS SYSTEM PROCEDURE ORPCS")
    if x[s1] + x["040&041&042|NON-ORPCS"] > 0:
        if x["MCC"] > 0:
            y.append("040")
        elif x["CC"] > 0:
            y.append("041")
        elif x["040&041&042|PERIPHERAL NEUROSTIMULATORS"] > 0:
            y.append("041")
        else:
            y.append("042")

    return y


