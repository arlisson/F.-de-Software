from instaloader import *

L = Instaloader()

L.login('Username', 'Password')  # -> Email/usuario e senha para fazer login

PROFILE = ''  # -> Coloque o nome do perfil a ser procurado

profile = Profile.from_username(L.context, PROFILE)


posts_sorted_by_likes = sorted(
    profile.get_posts(), key=lambda post: post.likes, reverse=True)


print('\nPost com mais likes: {}\nNúmero de likes -> {}'.format(
    posts_sorted_by_likes[0].url, posts_sorted_by_likes[0].likes))
