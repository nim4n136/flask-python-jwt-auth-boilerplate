from flask_restful import Resource
from flask import request
from api.v1.repository import PostsRepository
from api.base import rowsTransform, rowTransform
from api.base import Response



class PostListController(Resource):

    """
        Get list collection
    """
    def get(self):
        req = request.args
        repo_post = PostsRepository()

        # Get data & filter limit
        posts = repo_post.get()
        if req.get('limit'):
            posts = posts.limit(int(req.get('limit')))
        
        # Result transform to dict
        data_response = rowsTransform(posts.all(), ['id','title', 'content'])

        # Response json
        return Response(data_response).success()
    

    def post(self):
        try:
            # get request json raw with header Content-type: application/json
            req = request.get_json()

            # create post
            create = PostsRepository()
            created = create.insert(req)

            # response data has created
            show_data = rowTransform(created, ['id', 'title', 'content'])
            
            # response success
            return Response(show_data).success()
        except Exception as e:
            return Response().error(message="Failed to create post", errorMessage=str(e))

    

class PostController(Resource):

    """
        Delete post
    """
    def delete(self, id):
        try:
            # try delete post by id
            repo = PostsRepository()
            repo.detelById(id)

            # response success deleted post
            return Response().success(message="Delete post success")
        except Exception as e:
            # Response failed deleted post
            return Response().error(message="Delete post failed", errorMessage=str(e))
    

    """
        Get post one
    """
    def get(self, id):
        try:
            # Get post by id
            repo = PostsRepository()
            result = repo.firstFilterBy({'id': id})

            # Transform result to dict
            if not result:
                return Response().error(code=404, message="Post id {} not found ".format(id))

            dict_result = rowTransform(result, ['id','title','content'])

            # Response success
            return Response(dict_result).success(message="Success")

        except Exception as e:
            # Response error
            return Response().error(errorMessage=str(e))
    
    """
        Update post
    """
    def patch(self, id):
        try:
            # get request json raw with header Content-type: application/json
            req = request.get_json()

            repo = PostsRepository()
            repo.updateById(id, req)

            req['id'] = id
            return Response(req).success(message="Data updated")
        except Exception as e:
            return Response().error(code=500, message="Failed update database", errorMessage=str(e))

    
