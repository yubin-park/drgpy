
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

    return y


