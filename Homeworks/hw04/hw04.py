passphrase = 'greensalsa'

def survey(p):
    """
    You do not need to understand this code.
    >>> survey(passphrase)
    '51db82444d12fe719e566c673ac9fcb6639a8ce843aed564978b8501'
    """
    import hashlib
    return hashlib.sha224(p.encode('utf-8')).hexdigest()
