
def mdc08(x):

    y = []
    if x["_MDC08"] == 0:
        return y
    
    if (x["453&454&455|ANTERIOR SPINAL FUSION ORPCS"] +
        x["453&454&455|POSTERIOR SPINAL FUSION ORPCS"] > 0):
        if x["_MCC"] > 0:
            y.append("453")
        elif x["_CC"] > 0:
            y.append("454")
        else:
            y.append("455")

    # NOTE IMPORTANT
    # The joint procedure codes for "Extensive Fusions",
    #     such as 0RG7370 + 0RG707J, are not taken into account
    # This will provide different results from the original MS-DRG
    # NEEDS TO BE ADDRESSED BEFORE DEPLOYMENT
    # THIS WILL RESULTS MS-DRG 456/460 to be coded to 456/457/458
    s1 = "456&457&458|SPINAL FUSION EXCEPT CERVICAL ORPCS"
    s2 = "456&457&458|SPINAL CURVATURE / MALIGNANCY / INFECTION PDX"
    s3 = "456&457&458|OR SDX"
    s4 = "456&457&458|EXTENSIVE FUSIONS ORPCS"
    if x[s1] + x[s2] + x[s3] + x[s4] > 0:
        if x["_MCC"] > 0:
            y.append("456")
        elif x["_CC"] > 0:
            y.append("457")
        else:
            y.append("458")

    if x["459&460|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("459")
        else:
            y.append("460")

    s1 = ("461&462|To qualify as bilateral or multiple joint " +
            "procedures you must have at least one code from " + 
            "two different lower extremity sites as listed below. " + 
            "Examples: left hip and right hip - bilateral; left hip " + 
            "and left knee - multiple; left hip and right ankle - " + 
            "multiple; left knee and right knee - bilateral RIGHT HIP")
    s2 = "461&462|LEFT HIP"
    s3 = "461&462|RIGHT KNEE"
    s4 = "461&462|LEFT KNEE"
    s5 = "461&462|RIGHT ANKLE"
    s6 = "461&462|LEFT ANKLE"
    z = [x[s1], x[s2], x[s3], x[s4], x[s5], x[s6]]
    z = [int(z_i > 0) for z_i in z]
    if sum(z) > 1:
        if x["_MCC"] > 0:
            y.append("461")
        else:
            y.append("462")

    if x["463&464&465|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("463")
        elif x["_CC"] > 0:
            y.append("464")
        else:
            y.append("465")

    if x["466&467&468|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("466")
        elif x["_CC"] > 0:
            y.append("467")
        else:
            y.append("468")

    if x["469&470|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("469")
        else:
            y.append("470")

    if x["471&472&473|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("471")
        elif x["_CC"] > 0:
            y.append("472")
        else:
            y.append("473")

    if x["474&475&476|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("474")
        elif x["_CC"] > 0:
            y.append("475")
        else:
            y.append("476")

    if x["477&478&479|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("477")
        elif x["_CC"] > 0:
            y.append("478")
        else:
            y.append("479")

    if x["480&481&482|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("480")
        elif x["_CC"] > 0:
            y.append("481")
        else:
            y.append("482")

    if x["483|ORPCS"] > 0:
        y.append("483")

    if x["485&486&487&488&489|KNEE PROCEDURE ORPCS"] > 0:
        if x["485&486&487&488&489|INFECTION PDX"] > 0:
            if x["_MCC"] > 0:
                y.append("485")
            elif x["_CC"] > 0:
                y.append("486")
            else:
                y.append("487")
        else:
            if x["_MCC"] + x["_CC"] > 0:
                y.append("488")
            else:
                y.append("489")

    if x["518&519&520|BACK & NECK EXCEPT DISC DEVICES ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("518")
        elif x["_CC"] > 0:
            y.append("519")
        else:
            y.append("520")
    elif (x["518&519&520|DISC DEVICES ORPCS"] + 
            x["518&519&520|NEUROSTIMULATORS"] > 0):
        y.append("518")

    if x["492&493&494|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("492")
        elif x["_CC"] > 0:
            y.append("493")
        else:
            y.append("494")

    if x["495&496&497|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("495")
        elif x["_CC"] > 0:
            y.append("496")
        else:
            y.append("497")

    if x["498&499|ORPCS"] > 0:
        if x["_MCC"] + x["_CC"] > 0:
            y.append("498")
        else:
            y.append("499")

    if x["500&501&502|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("500")
        elif x["_CC"] > 0:
            y.append("501")
        else:
            y.append("502")

    if x["503&504&505|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("503")
        elif x["_CC"] > 0:
            y.append("504")
        else:
            y.append("505")

    if x["506|ORPCS"] > 0:
        y.append("506")

    if x["507&508|ORPCS"] > 0:
        if x["_MCC"] + x["_CC"] > 0:
            y.append("507")
        else:
            y.append("508")

    if x["509|ORPCS"] > 0:
        y.append("509")

    if x["510&511&512|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("510")
        elif x["_CC"] > 0:
            y.append("511")
        else:
            y.append("512")

    if x["513&514|ORPCS"] > 0:
        if x["_MCC"] + x["_CC"] > 0:
            y.append("513")
        else:
            y.append("514")

    if x["515&516&517|ORPCS"] > 0:
        if x["_MCC"] > 0:
            y.append("515")
        elif x["_CC"] > 0:
            y.append("516")
        else:
            y.append("517")

    if x["533&534|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("533")
        else:
            y.append("534")

    if x["535&536|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("535")
        else:
            y.append("536")

    if x["537&538|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("537")
        else:
            y.append("538")

    if x["539&540&541|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("539")
        elif x["_CC"] > 0:
            y.append("540")
        else:
            y.append("541")

    if x["542&543&544|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("542")
        elif x["_CC"] > 0:
            y.append("543")
        else:
            y.append("544")

    if x["545&546&547|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("545")
        elif x["_CC"] > 0:
            y.append("546")
        else:
            y.append("547")

    if x["548&549&550|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("548")
        elif x["_CC"] > 0:
            y.append("549")
        else:
            y.append("550")

    if x["551&552|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("551")
        else:
            y.append("552")

    if x["553&554|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("553")
        else:
            y.append("554")

    if x["555&556|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("555")
        else:
            y.append("556")

    if x["557&558|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("557")
        else:
            y.append("558")

    if x["559&560&561|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("559")
        elif x["_CC"] > 0:
            y.append("560")
        else:
            y.append("561")

    if x["562&563|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("562")
        else:
            y.append("563")

    if x["564&565&566|PDX"] > 0:
        if x["_MCC"] > 0:
            y.append("564")
        elif x["_CC"] > 0:
            y.append("565")
        else:
            y.append("566")

    return y

def mdc09(x):

    y = []
    if x["_MDC09"] == 0:
        return y

    return y

def mdc10(x):

    y = []
    if x["_MDC10"] == 0:
        return y

    return y

def mdc11(x):

    y = []
    if x["_MDC11"] == 0:
        return y

    return y




