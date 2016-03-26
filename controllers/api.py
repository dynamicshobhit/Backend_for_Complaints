@request.restful()
def get_post():
    def GET(id):
        post=db.post(id)
        return post.as_dict() if post else None
    return locals()

def add_complaint():
    if auth.is_logged_in():
        db.post.insert(
        #catagory=str(request.vars["catagory"]),
        complaint_level=int(request.vars["complaint_level"]),
        title=str(request.vars["title"]),
        Resolved=str(request.vars["resolved"]),
        body=str(request.vars["body"])
        #created_by=str(request.vars["created_by"]),
            )
        return request.vars["body"]

def set_resolved():
    if auth.is_logged_in():
        id = int(request.vars["id"])
        sta = str(request.vars["status"])
        post=db.post(id)
        if post:
            post.update_record(Resolved=sta)
            return dict(success=True,post=post)
    return locals()

def up_downvote():
    if auth.is_logged_in():
        id = int(request.vars["id"])
        vote = int(request.vars["vote"])
        post=db.post(id)
        if post:
            post.update_record(votes=post.votes+vote)
            return dict(success=True,post=post)
    return id
@request.restful()
def post():
    def GET(*args,**vars):
        patterns=['/{post.complaint_level}',
                 '/catagory/id/{catagory.id}',
                 '/by-user/{post.created_by}']
        parsed=db.parse_as_rest(patterns,args,vars)
        if parsed.status==200:return dict(content=parsed.response)
        raise HTTP(parsed.status,parsed.error)
    #def POST(catagory,title,resolved,url,body,votes):
        #return db.post.validate_and_insert(catagory=catagory,title=title,resolved=resolved,url=url if url else None,body=body,votes=votes)
    return locals()
@request.restful()
def auto():
    def GET(*args,**vars):
        parsed=db.parse_as_rest('auto',args,vars)
        if parsed.status==200:return dict(content=parsed.response)
        raise HTTP(parsed.status,parsed.error)
    return locals()
