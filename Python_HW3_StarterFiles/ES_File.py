
import numpy as np

def ES(losses, confidence=None, VaR=None, use_PnL=False):

    if VaR is None:
        VaR = np.percentile(losses, 100 * confidence)

    losses_exceeding_VaR = losses[losses > VaR]

    es_value = np.mean(losses_exceeding_VaR)

    return es_value
