
def mdc12(x):

    y = []
    if x["_MDC12"] == 0:
        return y

    if x["707&708|ORPCS"] > 0:
        if x["_MCC"] + x["_CC"] > 0:
            y.append("707")
        else:
            y.append("708")

    if x["709&710|ORPCS"] > 0:
        if x["_MCC"] + x["_CC"] > 0:
            y.append("709")
        else:
            y.append("710")

    if x["711&712|ORPCS"] > 0:
        if x["_MCC"] + x["_CC"] > 0:
            y.append("711")
        else:
            y.append("712")

    if x["713&714|ORPCS"] > 0:
        if x["_MCC"] + x["_CC"] > 0:
            y.append("713")
        else:
            y.append("714")

    s1 = ("715&716&717&718|OTHER MALE REPRODUCTIVE SYSTEM O.R. " + 
            "PROCEDURE ORPCS")
    s2 = "715&716&717&718|MALIGNANCY PDX"
    if x[s1] > 0:
        if x[s2] > 0:
            if x["_MCC"] + x["_CC"] > 0:
                y.append("715")
            else:
                y.append("716")
        else:
            if x["_MCC"] + x["_CC"] > 0:
                y.append("717")
            else:
                y.append("718")

    if x["722&723&724|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("722")
        elif x["_CC"] > 0:
            y.append("723")
        else:
            y.append("724")

    if x["725&726|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("725")
        else:
            y.append("726")

    if x["727&728|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("727")
        else:
            y.append("728")

    if x["729&730|PDX"] > 0:
        if x["_MCC"] + x["_CC"] > 0:
            y.append("729")
        else:
            y.append("730")

    return y

def mdc13(x):

    y = []
    if x["_MDC13"] == 0:
        return y

    if x["734&735|ORPCS"] > 0:
        if x["_MCC"] + x["_CC"] > 0:
            y.append("734")
        else:
            y.append("735")

    s1 = "736&737&738&739&740&741|UTERINE AND ADNEXAL PROCEDURE ORPCS"
    s2 = "736&737&738&739&740&741|OVARIAN/ADNEXAL MALIGNANCY PDX"
    s3 = "736&737&738&739&740&741|NON-OVARIAN/ADNEXAL MALIGNANCY PDX"
    if x[s1] > 0:
        if x[s2] > 0:
            if x["_MCC"] > 0:
                y.append("736")
            elif x["_CC"] > 0:
                y.append("737")
            else:
                y.append("738")
        elif x[s3] > 0:
            if x["_MCC"] > 0:
                y.append("739")
            elif x["_CC"] > 0:
                y.append("740")
            else:
                y.append("741")

    if x["742&743|ORPCS"] * x["742&743|PDX"] > 0:
        if x["_MCC"] + x["_CC"] > 0:
            y.append("742")
        else:
            y.append("743")

    if x["744&745|ORPCS"] > 0:
        if x["_MCC"] + x["_CC"] > 0:
            y.append("744")
        else:
            y.append("745")

    if x["746&747|ORPCS"] > 0:
        if x["_MCC"] + x["_CC"] > 0:
            y.append("746")
        else:
            y.append("747")

    if x["748|ORPCS"] > 0:
        y.append("748")
        
    if x["749&750|ORPCS"] > 0:
        if x["_MCC"] + x["_CC"] > 0:
            y.append("749")
        else:
            y.append("750")

    if x["754&755&756|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("754")
        elif x["_CC"] > 0:
            y.append("755")
        else:
            y.append("756")

    if x["757&758&759|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("757")
        elif x["_CC"] > 0:
            y.append("758")
        else:
            y.append("759")

    if x["760&761|PDX"] > 0:
        if x["_MCC"] + x["_CC"] > 0:
            y.append("760")
        else:
            y.append("761")

    return y

def mdc14(x):

    y = []
    if x["_MDC14"] == 0:
        return y

    if x["783&784&785|ORPCS"] * x["783&784&785|AND ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("783")
        elif x["_CC"] > 0:
            y.append("784")
        else:
            y.append("785")

    if (x["786&787&788|ORPCS"] > 0 and 
        x["786&787&788|WITHOUT ORPCS"] == 0):
        if x["_MCC"] > 0:
            y.append("786")
        elif x["_CC"] > 0:
            y.append("787")
        else:
            y.append("788")

    if (x["768|SDX"] * x["768|DELIVERY ORPCS"] > 0 and
        x["768|WITH ANY ORPCS EXCEPT"] == 0):
        y.append("768")
        
    if ((x["796&797&798|SDX"] * x["796&797&798|AND ORPCS"] * 
        (x["796&797&798|AND ORPCS*"] + 
            x["796&797&798|OR ORPCS"])) > 0):
        if x["_MCC"] > 0:
            y.append("796")
        elif x["_CC"] > 0:
            y.append("797")
        else:
            y.append("798")

    if x["770|PDX"] * x["770|AND ORPCS"] > 0:
        y.append("770")

    if x["817&818&819|PDX"] * x["_ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("817")
        elif x["_CC"] > 0:
            y.append("818")
        else:
            y.append("819")

    if (x["805&806&807|SDX"] * x["805&806&807|AND ORPCS"] > 0):
        if x["_MCC"] > 0:
            y.append("805")
        elif x["_CC"] > 0:
            y.append("806")
        else:
            y.append("807")

    if x["779|PDX"] > 0:
        y.append("779")

    if x["831&832&833|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("831")
        elif x["_CC"] > 0:
            y.append("832")
        else:
            y.append("833")

    if x["776|PDX"] > 0:
        y.append("776")

    if x["998|PDX"] > 0:
        y.append("998")

    return y

def mdc15(x):

    y = []
    if x["_MDC15"] == 0:
        return y

    # NOTE: DRG 789 skipped

    if (x["795|PDX"] *
        (x["_NDX1"] + x["_NDX2"]*x["795|AND NO SDX OR ONLY SDX"]) > 0):
        y.append("795")

    if x["790|PSDX"] > 0:
        y.append("790")

    if x["791&792|PREMATURITY PSDX"] > 0:
        if x["793|MAJOR PROBLEMS PSDX"] + x["793|OR SDX"] > 0:
            y.append("791")
        else:
            y.append("792")

    if x["793|MAJOR PROBLEMS PSDX"] + x["793|OR SDX"] > 0:
        y.append("793")

    s1 = ("794|Principal or secondary diagnosis of newborn or " + 
        "neonate,with other significant problems, not assigned to " + 
        "DRG 789 through 793 or 795 PSDX")
    if x[s1] > 0 and len(y) == 0: 
        y.append("794")

    return y

def mdc16(x):

    y = []
    if x["_MDC16"] == 0:
        return y

    return y

def mdc17(x):

    y = []
    if x["_MDC17"] == 0:
        return y

    return y

def mdc18(x):

    y = []
    if x["_MDC18"] == 0:
        return y

    return y

def mdc19(x):

    y = []
    if x["_MDC19"] == 0:
        return y

    return y

def mdc20(x):

    y = []
    if x["_MDC20"] == 0:
        return y

    return y

def mdc21(x):

    y = []
    if x["_MDC21"] == 0:
        return y

    return y




