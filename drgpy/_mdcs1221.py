
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

    if ((x["768|SDX"] * x["768|DELIVERY ORPCS"] > 0) or
        (x["768|SDX"] * x["768|NON-ORPCS"] > 0 and 
            x["768|WITH ANY ORPCS EXCEPT"] == 0)):
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

    if x["817&818&819|PDX"] * x["_ORPCS|817"] > 0:
        if x["_MCC"] > 0:
            y.append("817")
        elif x["_CC"] > 0:
            y.append("818")
        else:
            y.append("819")

    if ((x["805&806&807|SDX"] * x["805&806&807|AND ORPCS"] > 0) or
            (x["805&806&807|SDX"] * x["805&806&807|NON-ORPCS"] > 0)):
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
        (x["_NDX1"] + x["_NDX2+"] * x["795|AND NO SDX OR ONLY SDX"]) > 0):
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

    s1 = "794|PSDX"
    if x[s1] > 0 and len(y) == 0: 
        y.append("794")

    return y

def mdc16(x):

    y = []
    if x["_MDC16"] == 0:
        return y

    if x["799&800&801|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("799")
        elif x["_CC"] > 0:
            y.append("800")
        else:
            y.append("801")
    
    if x["802&803&804|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("802")
        elif x["_CC"] > 0:
            y.append("803")
        else:
            y.append("804")

    if x["808&809&810|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("808")
        elif x["_CC"] > 0:
            y.append("809")
        else:
            y.append("810")
    
    if x["811&812|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("811")
        else:
            y.append("812")

    if x["813|PDX"] > 0:
        y.append("813")

    if x["814&815&816|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("814")
        elif x["_CC"] > 0:
            y.append("815")
        else:
            y.append("816")
 
    return y

def mdc17(x):

    y = []
    if x["_MDC17"] == 0:
        return y

    if x["820&821&822|PDX"] * x["820&821&822|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("820")
        elif x["_CC"] > 0:
            y.append("821")
        else:
            y.append("822")

    s1 = ("823&824&825|ANY OTHER ORPCS NOT LISTED IN DRGS 820-822 OR " + 
        "ANY OF THE FOLLOWING NON-ORPCS")
    if (x["823&824&825|PDX"] > 0 and
        ((x["_ORPCS|823"] > 0 and 
            x["820&821&822|ORPCS"] == 0) or 
            x[s1] > 0)):
        if x["_MCC"] > 0:
            y.append("823")
        elif x["_CC"] > 0:
            y.append("824")
        else:
            y.append("825")

    s1 = ("826&827&828|MYELOPROLIFERATIVE DISORDERS OR " + 
            "POORLY DIFFERENTIATED NEOPLASMS PDX")
    s2 = "826&827&828|MAJOR O.R. PROCEDURE ORPCS"
    if x[s1] * x[s2] > 0:
        if x["_MCC"] > 0:
            y.append("826")
        elif x["_CC"] > 0:
            y.append("827")
        else:
            y.append("828")

    s1 = ("829&830|MYELOPROLIFERATIVE DISORDERS OR " + 
            "POORLY DIFFERENTIATED NEOPLASMS PDX")
    s2 = "829&830|NON-ORPCS"
    if x[s1] * (x[s2] + x["_ORPCS|829"]) > 0:
        if x["_MCC"] + x["_CC"] > 0:
            y.append("829")
        else:
            y.append("830")

    if x["834&835&836|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("834")
        elif x["_CC"] > 0:
            y.append("835")
        else:
            y.append("836")

    if x["837&838&839|CHEMOTHERAPY PDX"] > 0:
        if x["837&838&839|ACUTE LEUKEMIA SDX"] > 0:
            if x["_MCC"] > 0:
                y.append("837")
            elif x["_CC"] > 0:
                y.append("838")
            else:
                y.append("839")
        elif x["837&838&839|HIGH DOSE CHEMO AGENT"] > 0:
            if x["_MCC"] > 0:
                y.append("837")
            else:
                y.append("838")

    if x["840&841&842|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("840")
        elif x["_CC"] > 0:
            y.append("841")
        else:
            y.append("842")

    if x["843&844&845|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("843")
        elif x["_CC"] > 0:
            y.append("844")
        else:
            y.append("845")

    if x["846&847&848|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("846")
        elif x["_CC"] > 0:
            y.append("847")
        else:
            y.append("848")

    if x["849|PDX"] > 0:
        y.append("849")

    return y

def mdc18(x):

    y = []
    if x["_MDC18"] == 0:
        return y

    if x["856&857&858|PDX"] > 0:
        if x["_MCC"] * x["_ORPCS|856"] > 0:
            y.append("856")
        elif x["_CC"] * x["_ORPCS|857"] > 0:
            y.append("857")
        elif x["_ORPCS|858"]:
            y.append("858")

    if x["853&854&855|PDX FROM MDC 18 EXCEPT"]==0:
        if x["_MCC"] * x["_ORPCS|853"] > 0:
            y.append("853")
        elif x["_CC"] * x["_ORPCS|854"] > 0:
            y.append("854")
        elif x["_ORPCS|855"]:
            y.append("855")

    if x["862&863|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("862")
        else:
            y.append("863")

    if x["864|PDX"] > 0:
        y.append("864")

    if x["865&866|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("865")
        else:
            y.append("866")

    if x["867&868&869|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("867")
        elif x["_CC"] > 0:
            y.append("868")
        else:
            y.append("869")

    if x["870&871&872|SEPTICEMIA PDX"] > 0:
        if x["870&871&872|MECHANICAL VENTILATION >96 HOURS"] > 0:
            y.append("870")
        elif x["_MCC"] > 0:
            y.append("871")
        else:
            y.append("872")

    return y

def mdc19(x):

    y = []
    if x["_MDC19"] == 0:
        return y

    if x["_ORPCS|876"] > 0:
        y.append("876")

    if x["880|PDX"] > 0:
        y.append("880")

    if x["881|PDX"] > 0:
        y.append("881")

    if x["882|PDX"] > 0:
        y.append("882")

    if x["883|PDX"] > 0:
        y.append("883")

    if x["884|PDX"] > 0:
        y.append("884")

    if x["885|PDX"] > 0:
        y.append("885")

    if x["886|PDX"] > 0:
        y.append("886")

    if x["887|PDX"] > 0:
        y.append("887")

    return y

def mdc20(x):

    y = []
    if x["_MDC20"] == 0:
        return y

    if x["_STATUS07"] > 0:
        y.append("894")

    s1 = ("895&896&897|ALCOHOL/DRUG ABUSE OR DEPENDENCE PDX " + 
            "IN MDC 20 REHABILITATION THERAPY NON-ORPCS")
    if x[s1] > 0:
        y.append("895")
    elif x["_MCC"] > 0:
        y.append("896")
    else:
        y.append("897")

    return y

def mdc21(x):

    y = []
    if x["_MDC21"] == 0:
        return y

    if x["901&902&903|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("901")
        elif x["_CC"] > 0:
            y.append("902")
        else:
            y.append("903")

    if x["904&905|ORPCS"] > 0:
        if x["_MCC"] + x["_CC"] > 0:
            y.append("904")
        else:
            y.append("905")

    if x["906|ORPCS"] > 0:
        y.append("906")

    if x["907&908&909|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("907")
        elif x["_CC"] > 0:
            y.append("908")
        else:
            y.append("909")

    if x["913&914|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("913")
        else:
            y.append("914")

    if x["915&916|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("915")
        else:
            y.append("916")
    
    if x["917&918|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("917")
        else:
            y.append("918")

    if x["919&920&921|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("919")
        elif x["_CC"] > 0:
            y.append("920")
        else:
            y.append("921")

    if x["922&923|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("922")
        else:
            y.append("923")

    return y




