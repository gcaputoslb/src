def correctLasFamilyNameUnit(lasfilePath, outputfile):
    proba = {}
    lasContent = lasio.read(lasfilePath)
    for ci in lasContent.curves:
        wls = []
        h = lasContent[ci['mnemonic']]
        h = h[np.logical_not(np.isnan(h))]
        counts, bins, bars = plt.hist(h, bins = 20)
        wls.append(np.nanmin(bins))
        wls.append(np.nanmax(bins))
        wls.append(np.mean(bins))
        wls.append(np.median(bins))
        wls.append(np.std(bins))
        predicted = model.predict(wls) 
        predictedprob = model.predict_proba(wls)
        ci.descr = ci.descr + " -- "+ predicted
        ci.descr = ''.join(ci.descr)
        pro = []
        i = 0
        for p in predictedprob[0]:
            if p > 0:
                pro.append([model.classes_[i], p])
            i = i + 1
        proba[ci.descr] = pro
    f = open(outputfile, "w")
    lasContent.write(f)
    return proba