import graphene
from graphene_django import DjangoObjectType

from core import models


class SocialNetworkUser(DjangoObjectType):
    class Meta:
        model = models.SocialNetworkUser


class Post(DjangoObjectType):
    class Meta:
        model = models.Post


class UserInput(graphene.InputObjectType):
    name = graphene.String()


class PostInput(graphene.InputObjectType):
    content = graphene.String()
    user_id = graphene.Int()


class CreateUser(graphene.Mutation):
    class Arguments:
        input = UserInput(required=True)


    ok = graphene.Boolean()
    user = graphene.Field(SocialNetworkUser)

    @staticmethod
    def mutate(root, info, input):
        instance = models.SocialNetworkUser(name=input.name)
        try:
            instance.save()

        except Exception:
            return CreateUser(ok=False, user=None)

        return CreateUser(ok=True, user=instance)


class CreatePost(graphene.Mutation):
    class Arguments:
        input = PostInput(required=True)

    ok = graphene.Boolean()
    post = graphene.Field(Post)

    @staticmethod
    def mutate(root, info, input):
        created_by = models.SocialNetworkUser.objects.get(pk=input.user_id)
        instance = models.Post(content=input.content, created_by=created_by)
        try:
            instance.save()

        except Exception:
            return CreatePost(ok=False, post=None)

        return CreatePost(ok=True, post=instance)


class Query(graphene.ObjectType):
    user = graphene.Field(SocialNetworkUser, id=graphene.Int())
    users = graphene.List(SocialNetworkUser)
    post = graphene.Field(Post, id=graphene.Int())

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return models.SocialNetworkUser.objects.get(pk=id)

        return None

    def resolve_users(self, info, **kwargs):
        return models.SocialNetworkUser.objects.all()

    def resolve_post(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return models.Post.objects.get(pk=id)

        return None



class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_post = CreatePost.Field()


schema = graphene.Schema(
    query=Query,
    mutation=Mutation
)