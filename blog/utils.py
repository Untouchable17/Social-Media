
def get_children(qs_child):
    res = []
    for comment in qs_child:
        c = {
            'id': comment.id,
            'text': comment.text,
            'timestamp': comment.timestamp.strftime('%Y-%m-%d > %H:%m'),
            'author': comment.user,
            'is_child': comment.is_child,
            'parent_id': comment.get_parent
        }
        if comment.comment_children.exists():
            c['children'] = get_children(comment.comment_children.all())
        res.append(c)
    return res


def create_comments_tree(qs):
    res = []
    for comment in qs:
        c = {
            'id': comment.id,
            'text': comment.text,
            'timestamp': comment.timestamp.strftime('%Y-%m-%d %H:%m'),
            'author': comment.user,
            'is_child': comment.is_child,
            'parent_id': comment.get_parent
        }
        if comment.comment_children:
            c['children'] = get_children(comment.comment_children.all())
        if not comment.is_child:
            res.append(c)
    return res

