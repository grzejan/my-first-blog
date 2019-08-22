from .models import Post
import rules

@rules.predicate
def is_post_author(user, post):
    if len(is_post_author.context.args)>1:
        return post.author == user
    return None

rules.add_rule('can_edit_post', is_post_author)
rules.add_rule('can_delete_post', is_post_author)
# rules.add_perm('blog', rules.always_allow) # jak było odremowane, to nie wpuszczało do admina
rules.add_perm('blog.change_post', is_post_author)
rules.add_perm('blog.delete_post', rules.always_false)
# rules.add_perm('blog.view_post', is_post_author)
# rules.add_perm('blog.add_post', is_post_author)