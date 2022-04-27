
def mdc22(x):

    y = []
    if x["_MDC22"] == 0:
        return y

    s1 = "927&933|EXTENSIVE BURNS PSDX"
    s2 = "927&933|FULL THICKNESS BURNS PSDX"
    s3 = "927&933|MECHANICAL VENTILATION >96 HOURS NON-ORPCS"
    s4 = "927&933|SKIN GRAFT PROCEDURE ORPCS"
    if (x[s1] + x[s2]) * x[s3] > 0:
        if x[s4] > 0:
            y.append("927")
        else:
            y.append("933")

    if x["928&929&934|PSDX"] > 0:
        if (x["928&929&934|SKIN GRAFT ORPCS"] +
            x["928&929&934|INHALATION INJURY SDX"] > 0):
            if x["_MCC"] + x["_CC"] > 0:
                y.append("928")
            else:
                y.append("929")
        else:
            y.append("934")
    
    if x["935|PDX"] > 0:
        y.append("935")

    return y

def mdc23(x):

    y = []
    if x["_MDC23"] == 0:
        return y

    if x["_ORPCS|939"] * x["_MCC"] > 0:
        y.append("939")
    elif x["_ORPCS|940"] * x["_CC"] > 0:
        y.append("940")
    elif x["_ORPCS|941"]:
        y.append("941")

    if (x["945&946|PDX"] > 0 or
        (x["945&946|OR FIRST CONDITION - ANY MDC 23 PDX EXCEPT"] == 0 and
            x["945&946|SECOND CONDITION - REHABILITATION PROCEDURE"])):
        if x["_MCC"] + x["_CC"] > 0:
            y.append("945")
        else:
            y.append("946")

    if x["947&948|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("947")
        else:
            y.append("948")

    if x["949&950|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("949")
        else:
            y.append("950")

    if x["951|PDX"] > 0:
        y.append("951") 

    return y

def mdc24(x):

    y = []
    if x["_MDC24"] == 0:
        return y

    if x["955|ORPCS"] > 0:
        y.append("955")

    if x["956|ORPCS"] > 0:
        y.append("956")

    if x["957&958&959|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("957")
        elif x["_CC"] > 0:
            y.append("958")
        else:
            y.append("959")

    if x["_MCC"] > 0:
        y.append("963")
    elif x["_CC"] > 0:
        y.append("964")
    else:
        y.append("965")

    return y

def mdc25(x):

    y = []
    if x["_MDC25"] == 0:
        return y

    if x["_ORPCS*"] > 0:
        if x["_MCC"] > 0:
            y.append("969")
        else:
            y.append("970")

    if (x["974&975&976|PSDX OF HIV INFECTION"] *
        x["974&975&976|AND PSDX OF MAJOR RELATED CONDITION"] > 0):
        if x["_MCC"] > 0:
            y.append("974")
        elif x["_CC"] > 0:
            y.append("975")
        else:
            y.append("976")

    if (x["974&975&976|PSDX OF HIV INFECTION"] > 0 and
        x["974&975&976|AND PSDX OF MAJOR RELATED CONDITION"] == 0):
        y.append("977")


    return y




