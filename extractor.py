from clients.cfacebook import FacebookClient
from clients.ctwitter import TwitterClient
from clients.cinstagram import InstagramClient
from clients.cyoutube import YouTubeClient

if __name__ == '__main__':
    instagram_names = ['jairmessiasbolsonaro', 'geraldoalckmin_', 'fernandohaddadoficial', '_marinasilva_', 'cirogomes']
    facebook_names = ['jairmessias.bolsonaro']#, 'geraldoalckmin', 'fernandohaddad', 'marinasilva.oficial', 'cirogomesoficial']
    twitter_names = ['jairbolsonaro', 'geraldoalckmin', 'haddad_fernando', 'marinasilva', 'cirogomes']
    youtube_names = ['jbolsonaro', 'UCNxCni0Iv9pr7i_pQZ6ijlg', 'msilvaonline', 'UCHFO37KCJlMNUXNK21MV8SQ']

    clients = [
        FacebookClient(names=facebook_names, np_posts=1, np_comments=1),
        #TwitterClient(names=twitter_names, np_posts=1, np_comments=1),
        #InstagramClient(names=instagram_names, np_posts=1, np_comments=1),
        #YouTubeClient(names=youtube_names, np_posts=2, np_comments=1)
    ]

    for client in clients:
        client.start()
        print(client.results)
