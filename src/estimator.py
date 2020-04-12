from handlers import impactEstimates, severeImpactEstimates


def estimator(data):
    response = {
        "data": data,
        "impact": impactEstimates(data),
        "severeImpact": severeImpactEstimates(data),
    }
    return response
