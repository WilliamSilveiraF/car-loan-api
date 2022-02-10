IPCA = 0.1005

def getRates(rawRate, IPCA):
    nominalGrossRate = ((1 + rawRate) * (1 + IPCA)) - 1
    nominalNetRate = nominalGrossRate * 0.85
    yearlyRealNetRate = ((1 + nominalNetRate) / (1 + IPCA)) - 1
    monthlyRealNetRate = ((1 + yearlyRealNetRate) ** (1 / 12)) - 1

    return {
        nominalGrossRate,
        nominalNetRate,
        yearlyRealNetRate,
        monthlyRealNetRate
    }