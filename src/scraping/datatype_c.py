from collections import namedtuple


Candidate = namedtuple('Candidate', ['uuid', 'name'])

facebook_names = [
    Candidate('jairmessias.bolsonaro', 'Jair Bolsonaro'),
    Candidate('geraldoalckmin', 'Geraldo Alckmin'),
    Candidate('fernandohaddad', 'Fernando Haddad'),
    Candidate('marinasilva.oficial', 'Marina Silva'),
    Candidate('cirogomesoficial', 'Ciro Gomes'),
]
twitter_names = [
    Candidate('jairbolsonaro', 'Jair Bolsonaro'),
    Candidate('geraldoalckmin', 'Geraldo Alckmin'),
    Candidate('haddad_fernando', 'Fernando Haddad'),
    Candidate('marinasilva', 'Marina Silva'),
    Candidate('cirogomes', 'Ciro Gomes'),
]
instagram_names = [
    Candidate('jairmessiasbolsonaro', 'Jair Bolsonaro'),
    Candidate('geraldoalckmin_', 'Geraldo Alckmin'),
    Candidate('fernandohaddadoficial', 'Fernando Haddad'),
    Candidate('_marinasilva_', 'Marina Silva'),
    Candidate('cirogomes', 'Ciro Gomes'),
]
youtube_names = [
    Candidate('jbolsonaro', 'Jair Bolsonaro'),
    Candidate('UCNxCni0Iv9pr7i_pQZ6ijlg', 'Geraldo Alckmin'),
    Candidate('msilvaonline', 'Marina Silva'),
    Candidate('UCHFO37KCJlMNUXNK21MV8SQ', 'Ciro Gomes'),
]