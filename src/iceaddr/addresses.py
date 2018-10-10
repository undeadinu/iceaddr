# -*- encoding: utf-8 -*-
"""
    
    iceaddr: Look up information about Icelandic house addresses
    Copyright (c) 2018 Sveinbjorn Thordarson
    
"""

from .db import shared_db
from .postcodes import postcodes, postcodes_for_placename

def iceaddr_lookup(street_name, number=None, letter=None, postcode=None, placename=None):
    
    db_conn = shared_db.connection()
    c = db_conn.cursor()
    
    # Look up postcodes for placename if no postcode is provided
    pc = [postcode] if postcode else []
    if placename and not postcode:
        pc = postcodes_for_placename(placename)        
        
    q = 'SELECT * FROM stadfong WHERE (heiti_nf=? OR heiti_tgf=?)'
    l = [street_name, street_name]
    if number:
        q += ' AND husnr=? '
        l.append(number)
    if letter:
        q += ' AND bokst=? '
        l.append(letter)
    if len(pc):
        if len(pc) == 1:
            qp = ' postnr=? '
            l.append(pc[0])
        else:
            qp = ' OR '.join([' postnr=?' for p in pc])
            l.extend(p for p in pc)
        q += ' AND (%s) ' % qp
    
    # Ordering by postcode may in fact be a reasonable proxy
    # for delivering by order of match likelihood since the
    # lowest postcodes are generally more densely populated
    q += 'ORDER BY postnr'
    
    res = c.execute(q, l)

    addresses = [row for row in res]
    for a in addresses:
        # Add postcode info
        if a['postnr']:
            pcinfo = postcodes[a['postnr']]
            a['stadur_nf'] = pcinfo['placename_nf']
            a['stadur_tgf'] = pcinfo['placename_tgf']
            a['svaedi'] = pcinfo['area']
            a['tegund'] = pcinfo['type']
    
    return addresses

