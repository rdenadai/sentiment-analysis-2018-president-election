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
    Candidate('https://www.youtube.com/user/jbolsonaro/videos', 'Jair Bolsonaro'),
    Candidate('https://www.youtube.com/channel/UCNxCni0Iv9pr7i_pQZ6ijlg/videos', 'Geraldo Alckmin'),
    Candidate('https://www.youtube.com/user/msilvaonline/videos', 'Marina Silva'),
    Candidate('https://www.youtube.com/channel/UCHFO37KCJlMNUXNK21MV8SQ/videos', 'Ciro Gomes'),
]
hashtags = [
    'eleicoes2018',
    'eleições2018',
    'Eleições2018',
    'eleicao2018',
    'Eleição2018',
    'DebateNaBand',
    'DebateRedeTv',
    'CiroNoJornalNacional',
    'CiroNaGloboNews',
]